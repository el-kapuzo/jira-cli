import datetime
import functools
from jira import JIRA, Issue
from typing import Any, Generator, Iterable, List, Optional

from .jiraAttachments import JiraAttachment
from .pendingWorklog import PendingWorklog
from .jiraWorklog import JiraWorklog


class JiraTask:
    NOT_A_STORY_TYPE = {"Sub-task"}
    SUBTASK_TYPES = {"Sub-task", "Task"}

    def __init__(self, jira: JIRA, issue: Issue):
        self.jira = jira
        self.issue = issue
        self._attachments = None
        self._transition_map = None
        self._worklogs = None

    @property
    def transition_map(self) -> dict[str, Any]:
        if self._transition_map is None:
            self._transition_map = {
                t["name"]: t["id"] for t in self.jira.transitions(self.issue)
            }
        return self._transition_map

    @property
    def available_transitions(self) -> Iterable[str]:
        return self.transition_map.keys()

    @functools.cached_property
    def descriptions(self) -> str:
        return self.jira.issue(self.issue.key).fields.description

    @property
    def key(self) -> str:
        return self.issue.key

    @property
    def parent_key(self):
        return self.issue.fields.parent.key

    @property
    def summary(self) -> str:
        return self.issue.fields.summary

    @property
    def status(self) -> str:
        return self.issue.fields.status.name

    @property
    def issue_type(self) -> str:
        return self.issue.fields.issuetype

    @property
    def is_story(self) -> bool:
        return str(self.issue_type) not in self.NOT_A_STORY_TYPE

    @property
    def is_subtask(self) -> bool:
        return str(self.issue_type) in self.SUBTASK_TYPES

    @property
    def attachments(self) -> List[JiraAttachment]:
        if self._attachments is None:
            self._attachments = [
                JiraAttachment(self.jira, att) for att in self.issue.fields.attachment
            ]
        return self._attachments

    @functools.cached_property
    def original_estimate(self):
        return self.issue.fields.timeoriginalestimate

    @property
    def worklogs(self):
        if self._worklogs is None:
            self._worklogs = [
                JiraWorklog(worklog) for worklog in self.jira.worklogs(self.key)
            ]
        return self._worklogs

    def add_attachment(self, path) -> JiraAttachment:
        attachment = self.jira.add_attachment(self.key, path)
        self.attachments.append(JiraAttachment(self.jira, attachment))
        return attachment

    def iter_subtasks(self) -> Iterable["JiraTask"]:
        try:
            yield from map(lambda x: JiraTask(self.jira, x), self.issue.fields.subtasks)
        except Exception:
            yield from ()

    def estimate(self, estimation) -> None:
        fields = {"timetracking": {"originalEstimate": estimation}}
        self.issue.update(fields=fields)

    def add_task(self, summary, estimate) -> "JiraTask":
        assert self.is_story  # noqa: S101
        fields = {
            "project": {"key": "PYT"},
            "summary": summary,
            "issuetype": 10003,
            "timetracking": {"originalEstimate": estimate},
            "parent": {"key": self.key},
        }
        new_issue = self.jira.create_issue(fields=fields)
        return JiraTask(self.jira, new_issue)

    def add_worklog(
        self,
        time: str,
        started: Optional[datetime.datetime] = None,
    ) -> JiraWorklog:
        try:
            worklog = self.jira.add_worklog(
                self.issue,
                timeSpent=time,
                reduceBy=time,
                started=started,
            )
        except Exception:
            worklog = self.jira.add_worklog(self.issue, timeSpent=time, started=started)
        wrappedWorklog = JiraWorklog(worklog)
        self.worklogs.append(wrappedWorklog)
        return wrappedWorklog

    def delete_worklog(self, worklog_id: str):
        itemToRemove = None
        for idx, worklog in enumerate(self.worklogs):
            if worklog.id == worklog_id:
                worklog.delete()
                itemToRemove = idx
        self.worklogs.pop(itemToRemove)

    def change_lane(self, new_lane) -> None:
        resolution_id = self.transition_map[new_lane]
        self.jira.transition_issue(self.issue, resolution_id)
        self._transition_map = None
        self.issue = self.jira.issue(self.key)

    def close(self) -> None:
        self.change_lane("Done")

    def start_working(self) -> None:
        if self.status == "To Do":
            # If a task has not been estimated, we can not start working on it
            if not self._has_been_estimated():
                self.estimate("1m")
            try:
                self.change_lane("In Progress")
            except KeyError:
                pass

    def track(self) -> Generator[PendingWorklog, bool, Any]:
        def _track():
            self.start_working()
            worklog = PendingWorklog()
            shouldClose = yield worklog
            worklog = worklog.commit(self)
            if shouldClose:
                self.close()
            return worklog

        generator = _track()
        # Prime the generator!
        generator.send(None)
        return generator

    def _has_been_estimated(self) -> bool:
        return self.original_estimate and self.original_estimate > 0

    @functools.cached_property
    def comments(self):
        # TODO: (maybe?) wrap jira comment in JiraComment class
        return self.jira.comments(self.key)

    def add_comment(self, body):
        self.jira.add_comment(self.key, body)
