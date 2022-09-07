import pathlib

from prompt_toolkit.completion import PathCompleter

from jira_cli.queries import all_attachments
from jira_cli.completion import AttachmentCompleter, ChainCompleter


from .attachment import Attachment


NAME = "download"


@Attachment.command(NAME)
def download_attachment(self: Attachment, attachment_id, path=None):
    # TODO: how to best get the attachment?
    attachment = self.jiraTasks.attachment_for(attachment_id)
    if path:
        path = pathlib.Path(path)
    else:
        path = pathlib.Path.cwd()
    if not path.is_dir():
        print("    You need to provide a directory")
        return
    attachment.download()


@Attachment.completion_provider(NAME)
def download_attachment_completer(application):
    att_completer = AttachmentCompleter(all_attachments(application.issues))
    return ChainCompleter(att_completer, PathCompleter())
