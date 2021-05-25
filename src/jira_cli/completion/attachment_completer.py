from prompt_toolkit.completion import Completer, Completion


class AttachmentCompleter(Completer):
    def __init__(self, attachments, *args, **kwargs):
        self.attachments = list(attachments)
        super().__init__(*args, **kwargs)

    def get_completions(self, document, completion_event):
        already_typed_text = document.text_before_cursor
        for attachment in self.attachments:
            if is_completion(attachment, already_typed_text):
                yield Completion(
                    attachment.id,
                    start_position=-len(already_typed_text),
                    display=attachment.id,
                    display_meta=attachment.filename,
                )


def is_completion(attachment, already_typed_text):
    text = already_typed_text.lower()
    return attachment.id.startswith(text) or attachment.filename.lower().startswith(
        text
    )
