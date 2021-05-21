from prompt_toolkit.completion import PathCompleter
from jira_cli.completion import IssueCompleter, ChainCompleter
from jira_cli.queries import all_stories

from .attachment import Attachment


NAME = "new"


@Attachment.command(NAME)
def add_attachment(app, issuekey, path):
    app.jira.add_attachment(issuekey, path)


@Attachment.completion_provider(NAME)
def new_attachment_completion_provider(app):
    issue_completer = IssueCompleter(all_stories(app.issues))
    path_completer = PathCompleter()
    return ChainCompleter(issue_completer, path_completer)
