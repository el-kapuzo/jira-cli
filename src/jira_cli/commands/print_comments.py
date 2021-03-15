from jira_cli.decorators import command, completion_provider
from jira_cli.completion import IssueCompleter

NAME = "comments"


@command(NAME)
def print_comments(application, issuekey):
    pass


@completion_provider(NAME)
def print_comments_completer(application):
    return IssueCompleter(application.issues)
