import jira_cli.config
from jira_cli.jira_issues.jiraTask import JiraTask


class JiraTasks:
    def __init__(self, jira, jql):
        self.jira = jira
        self.jql = jql
        self._tasks = self.fetch_tasks()

    def task_for(self, issuekey) -> JiraTask:
        return self._tasks[issuekey]

    def fetch_tasks(self):
        return {
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
                ],
                maxResults=False,
            )
        }

    def add_sub_task(self, story_key, summary, estimation):
        new_issue = self.task_for(story_key).add_task(summary, estimation)
        self._tasks[new_issue.key] = JiraTask(self.jira, new_issue)

    def iter_subtasks(self):
        yield from filter(lambda x: x.is_subtask, self)

    def iter_stories(self):
        yield from filter(lambda x: x.is_story, self)

    def __iter__(self):
        yield from self._tasks.values()

    @classmethod
    def fromConfig(cls, config: jira_cli.config.Config):
        jira = config.server.connect()
        jql = config.settings.jql
        return cls(jira=jira, jql=jql)
