from prompt_toolkit import prompt
from jira_cli.completion import IssueCompleter
from jira_cli.decorators import command, completion_provider

NAME = "comment"


@command(NAME)
def add_comment(application, issuekey):
    # TODO: maybe
    body = prompt("#", multiline=True)
    application.jira.add_comment(issuekey, body)
    return issuekey


@completion_provider(NAME)
def add_comment_completer(application):
    return IssueCompleter(application.issues)
