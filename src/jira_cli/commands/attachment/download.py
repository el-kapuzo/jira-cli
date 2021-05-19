import pathlib

from jira_cli.queries import all_attachments
from jira_cli.completion import AttachmentCompleter


from .attachment import Attachment


NAME = "download"


@Attachment.command(NAME)
def download_attachment(application, attachment_id):
    attachment = application.jira.attachment(attachment_id)
    target_path = pathlib.Path.cwd() / attachment.filename
    with open(target_path, "wb+") as f:
        for chunk in attachment.iter_content():
            f.write(chunk)


@Attachment.completion_provider(NAME)
def download_attachment_completer(application):
    return AttachmentCompleter(all_attachments(application.issues))
