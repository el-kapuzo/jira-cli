import functools

import jira_cli.config
import jira_cli.jira_issues.jiraTask


class JiraTasks:
    def __init__(self, jira, jql):
        self.jira = jira
        self.jql = jql
        self._tasks = self.fetch_tasks()

    def task_for(self, issuekey):
        return self._tasks[issuekey]

    def fetch_tasks(self):
        return {
            issue.key: jira_cli.jira_issues.jiraTask.JiraTask(self.jira, issue)
            for issue in self.jira.search_issues(
                self.jql,
                fields=["attachment", "status", "summary", "issuetype", "parent"],
                maxResults=False,
            )
        }

    def iter_subtasks(self):
        yield from filter(lambda x: x.is_subtask, self._tasks.values())

    def iter_stories(self):
        yield from filter(lambda x: x.is_story, self._tasks.values())

    @classmethod
    def fromConfig(cls, config: jira_cli.config.Config):
        jira = config.server.connect()
        jql = config.settings.jql
        return cls(jira=jira, jql=jql)
