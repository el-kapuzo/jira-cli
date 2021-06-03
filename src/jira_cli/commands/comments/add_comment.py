from prompt_toolkit import prompt
from jira_cli.completion import IssueCompleter
from jira_cli.queries import all_stories
from .comments import Comment

NAME = "new"


@Comment.command(NAME)
def add_comment(application, issuekey):
    # TODO: maybe
    body = prompt("#   ", multiline=True)
    application.jira.add_comment(issuekey, body)
    return issuekey


@Comment.completion_provider(NAME)
def add_comment_completer(application):
    return IssueCompleter(all_stories(application.issues))
