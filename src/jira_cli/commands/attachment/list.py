from jira_cli.queries import all_stories
from jira_cli.completion import IssueCompleter
from .attachment import Attachment

NAME = "list"


@Attachment.command(NAME)
def list_subtasks(application, issuekey=None):
    if issuekey is None:
        _list_all_attachments(application)
    else:
        story = application.jira.issue(issuekey)
        _list_attachments(story)


def _list_all_attachments(application):
    issues = application.issues
    presenter = application.presenter
    for issue in all_stories(issues):
        _list_all_attachments(issue)


def _list_attachments(story):
    print(f"Attachments of {story.key}")
    for att in story.fields.attachment:
        print("   Id: {att.id}; Filename {att.filename} ")


@Attachment.completion_provider(NAME)
def completion_provieder_list_stories(application):
    return IssueCompleter(all_stories(application.issues), ignore_statuses=["Done"])
