from jira import JIRA
import jira_cli.config
from .jiraAttachments import JiraAttachment
from .jiraTask import JiraTask
from .jiraWorklog import JiraWorklog
from typing import Iterable


class JiraTasks:
    def __init__(self, jira: JIRA, jql: str):
        self.jira = jira
        self.jql = jql
        self._tasks = None
        self.fetch_tasks()

    @property
    def worklogs(self) -> Iterable[JiraWorklog]:
        for task in self:
            yield from task.worklogs

    def task_for(self, issuekey: str) -> JiraTask:
        return self._tasks[issuekey]

    def fetch_tasks(self) -> None:
        self._tasks = {
            issue.key: JiraTask(self.jira, issue)
            for issue in self.jira.search_issues(
                self.jql,
                fields=[
                    "attachment",
                    "status",
                    "summary",
                    "issuetype",
                    "parent",
                    "subtasks",
                    "timeoriginalestimate",
                ],
                maxResults=False,
            )
        }

    def associated_story(self, issue_key: str) -> "JiraTask":
        task = self.task_for(issue_key)
        if task.is_story:
            return task
        return self.task_for(task.parent_key)

    def add_sub_task(self, story_key: str, summary: str, estimation: str) -> JiraTask:
        new_task = self.task_for(story_key).add_task(summary, estimation)
        self._tasks[new_task.key] = new_task
        return new_task

    def attachment_for(self, attachment_id: str) -> JiraAttachment:
        for attachment in self.iter_attachments():
            if attachment.id == attachment_id:
                return attachment

    def iter_attachments(self) -> Iterable[JiraAttachment]:
        for story in self.iter_stories():
            yield from story.attachments

    def iter_subtasks(self) -> Iterable[JiraTask]:
        yield from filter(lambda x: x.is_subtask, self)

    def iter_stories(self) -> Iterable[JiraTask]:
        yield from filter(lambda x: x.is_story, self)

    def __iter__(self) -> Iterable[JiraTask]:
        yield from self._tasks.values()

    @classmethod
    def fromConfig(cls, config: jira_cli.config.Config):
        jira = config.server.connect()
        jql = config.settings.jql
        return cls(jira=jira, jql=jql)
