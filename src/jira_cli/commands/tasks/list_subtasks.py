import jira_cli.issue_presenter
import jira_cli.jira_issues.jiraTask
from jira_cli.queries import subtasks_of_issue, all_subtasks
from jira_cli.completion import IssueCompleter
from .task import Task

NAME = "list"


@Task.command(NAME)
def list_subtasks(application, issuekey=None):
    if issuekey is None:
        _list_all_tasks(application)
    else:
        _list_subtasks(application, issuekey)


def _list_all_tasks(application):
    issues = application.issues
    for issue in all_subtasks(issues):
        jira_cli.issue_presenter.print_issue(
            jira_cli.jira_issues.jiraTask.JiraTask(application.jira, issue),
        )


def _list_subtasks(application, issuekey):
    story = application.jira.issue(issuekey)
    for issue in subtasks_of_issue(story):
        jira_cli.issue_presenter.print_issue(
            jira_cli.jira_issues.jiraTask.JiraTask(application.jira, issue),
        )
    return issuekey


@Task.completion_provider(NAME)
def completion_provieder_list_stories(application):
    return IssueCompleter.story_completer(application, ignore_statuses=["Done"])
