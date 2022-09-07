import functools
from .jiraAttachments import JiraAttachment


class JiraTask:
    NOT_A_STORY_TYPE = {"Sub-task"}
    SUBTASK_TYPES = {"Sub-task"}

    def __init__(self, jira, issue):
        self.jira = jira
        self.issue = issue
        self._attachments = None

    @functools.cached_property
    def transition_map(self):
        return {t["name"]: t["id"] for t in self.jira.transitions(self.issue)}

    @functools.cached_property
    def descriptions(self):
        return self.jira.issue(self.issue.key).fields.description

    @property
    def key(self):
        return self.issue.key

    @property
    def summary(self):
        return self.issue.fields.summary

    @property
    def status(self):
        return self.issue.fields.status.name

    @property
    def issue_type(self):
        return self.issue.fields.issuetype

    @property
    def is_story(self):
        return str(self.issue_type) not in self.NOT_A_STORY_TYPE

    @property
    def is_subtask(self):
        return str(self.issue_type) in self.SUBTASK_TYPES

    @property
    def attachments(self):
        if self._attachments is None:
            self._attachments = [
                JiraAttachment(self.jira, att) for att in self.issue.fields.attachment
            ]
        return self._attachments

    def add_attachment(self, path):
        attachment = self.jira.add_attachment(self.key, path)
        self.attachments.append(JiraAttachment(self.jira, attachment))

    def iter_attachments(self):
        yield from self.attachments

    def associated_story(self):
        if self.is_story:
            return self
        return JiraTask(self.jira, self.issue.fields.parent)

    def iter_subtasks(self):
        try:
            yield from map(lambda x: JiraTask(self.jira, x), self.issue.fields.subtasks)
        except Exception:
            yield from ()

    def estimate(self, estimation):
        fields = {"timetracking": {"originalEstimate": estimation}}
        self.issue.update(fields=fields)

    def add_task(self, summary, estimate):
        assert self.is_story  # noqa: S101
        fields = {
            "project": {"key": "PYT"},
            "summary": summary,
            "issuetype": "Sub-task",
            "timetracking": {"originalEstimate": estimate},
            "parent": {"key": self.key},
        }
        return self.jira.create_issue(fields=fields)

    def add_worklog(self, time):
        try:
            self.jira.add_worklog(self.issue, timeSpent=time, reduceBy=time)
        except Exception:
            self.jira.add_worklog(self.issue, timeSpent=time)

    def iter_worklogs(self):
        # TODO: wrap worklogs with own class
        # TODO: cache result?
        yield from self.jira.worklogs(self.key)

    def change_lane(self, new_lane):
        resolution_id = self.transition_map[new_lane]
        self.jira.transition_issue(self.issue, resolution_id)

    def close(self):
        self.change_lane("Done")

    def maybe_start_working(self):
        try:
            self.change_lane("In Progress")
        except KeyError:
            pass

    @functools.cached_property
    def comments(self):
        # TODO: (maybe?) wrap jira comment in JiraComment class
        return self.jira.comments(self.key)

    def add_comment(self, body):
        self.jira.add_comment(self.key, body)
