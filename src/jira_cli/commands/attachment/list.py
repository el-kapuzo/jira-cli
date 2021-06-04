from prompt_toolkit import print_formatted_text, HTML
from jira_cli.queries import all_attachments
from jira_cli.completion import IssueCompleter
from .attachment import Attachment

NAME = "list"


@Attachment.command(NAME)
def list_subtasks(application, issuekey=None):
    if issuekey is None:
        issues = application.issues
    else:
        issues = [application.jira.issue(issuekey)]
    for att in all_attachments(issues):
        print_formatted_text(
            HTML(f"    <b>Id: {att.id}</b>; Filename: {att.filename} ")
        )


@Attachment.completion_provider(NAME)
def completion_provieder_list_stories(application):
    return IssueCompleter.subtask_completer(application)
