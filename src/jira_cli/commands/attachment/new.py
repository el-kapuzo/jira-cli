from jira_cli.completion import IssueCompleter
from jira_cli.queries import all_stories

from .attachment import Attachment


NAME = "new"


@Attachment.command(NAME)
def add_attachment(app, issuekey, path):
    app.jira.add_attachment(issuekey, path)


@Attachment.completion_provider(NAME)
def new_attachment_completion_provider(app):
    return IssueCompleter(all_stories(app.issues))
