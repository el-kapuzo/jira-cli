from prompt_toolkit import prompt
from jira_cli.completion import IssueCompleter
from .comments import Comments

NAME = "new"


@Comments.command(NAME)
def add_comment(application, issuekey):
    # TODO: maybe
    body = prompt("#   ", multiline=True)
    application.jira.add_comment(issuekey, body)
    return issuekey


@Comments.completion_provider(NAME)
def add_comment_completer(application):
    return IssueCompleter(application.issues)
