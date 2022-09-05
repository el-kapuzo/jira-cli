from prompt_toolkit.completion import PathCompleter
from jira_cli.completion import IssueCompleter, ChainCompleter

from .attachment import Attachment


NAME = "new"


@Attachment.command(NAME)
def add_attachment(self: Attachment, issuekey, path):
    self.jiraTasks.task_for(issuekey).add_attachment(path)


@Attachment.completion_provider(NAME)
def new_attachment_completion_provider(app):
    issue_completer = IssueCompleter.story_completer(app.jiraTasks)
    path_completer = PathCompleter()
    return ChainCompleter(issue_completer, path_completer)
