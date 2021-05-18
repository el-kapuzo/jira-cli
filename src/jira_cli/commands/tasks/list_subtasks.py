from jira_cli.queries import all_stories, subtasks_of_issue, all_subtasks
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
    presenter = application.presenter
    for issue in all_subtasks(issues):
        presenter.print_issue(issue)


def _list_subtasks(application, issuekey):
    story = application.jira.issue(issuekey)
    presenter = application.presenter
    for issue in subtasks_of_issue(story):
        presenter.print_issue(issue)
    return issuekey


@Task.completion_provider(NAME)
def completion_provieder_list_stories(application):
    return IssueCompleter(all_stories(application.issues), ignore_statuses=["Done"])
