from prompt_toolkit import print_formatted_text, HTML
from jira_cli.completion import IssueCompleter
from .attachment import Attachment

NAME = "list"


@Attachment.command(NAME)
def list_subtasks(self: Attachment, issuekey=None):
    attachments = self.jiraTasks.task_for(issuekey).attachments
    for att in attachments:
        print_formatted_text(
            HTML(f"    <b>Id: {att.id}</b>; Filename: {att.filename} "),
        )


@Attachment.completion_provider(NAME)
def completion_provieder_list_stories(application):
    return IssueCompleter.subtask_completer(application.jiraTasks)
