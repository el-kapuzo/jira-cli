import jira_cli.issue_presenter
import jira_cli.jira_issues.jiraTask
from jira_cli.completion import IssueCompleter
from .task import Task

NAME = "list"


@Task.command(NAME)
def list_subtasks(self: Task, issuekey=None):
    if issuekey:
        sub_task_iterator = self.jiraTasks.task_for(issuekey).iter_subtasks()
    else:
        sub_task_iterator = self.jiraTasks.iter_subtasks()
    for task in sub_task_iterator:
        jira_cli.issue_presenter.print_issue(task)


@Task.completion_provider(NAME)
def add_task_completion_provider(application):
    return IssueCompleter.story_completer(application)
