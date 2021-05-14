from jira_cli.queries import all_stories, subtasks_of_issue
from jira_cli.completion import IssueCompleter
from .story import Story

NAME = "tasks"


@Story.command(NAME)
def list_subtasks(application, issuekey):
    story = application.jira.issue(issuekey)
    presenter = application.presenter
    for issue in subtasks_of_issue(story):
        presenter.print_issue(issue)
    return issuekey


@Story.completion_provider(NAME)
def completion_provieder_list_stories(application):
    return IssueCompleter(all_stories(application.issues), ignore_statuses=["Done"])
