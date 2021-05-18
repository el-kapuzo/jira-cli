from jira_cli.queries import all_stories, all_attachments
from jira_cli.completion import IssueCompleter
from .attachment import Attachment

NAME = "list"


@Attachment.command(NAME)
def list_subtasks(application, issuekey=None):
    if issuekey is None:
        issues = application.issues
    else:
        issues = application.jira.issue(issuekey)
    for attachment in all_attachments(issues):
        print("Id: {att.id}; Filename {att.filename} ")


@Attachment.completion_provider(NAME)
def completion_provieder_list_stories(application):
    return IssueCompleter(all_stories(application.issues), ignore_statuses=["Done"])
