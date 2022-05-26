from prompt_toolkit import completion, document as doc
from .issue_completer import IssueCompleter


class ChainCompleter(completion.Completer):
    def __init__(self, first_completer, second_completer, *args, **kwargs):
        self.first_completer = first_completer
        self.second_completer = second_completer
        super().__init__(*args, **kwargs)

    def get_completions(self, document, complete_event):
        text = document.text_before_cursor.lstrip()
        stripped_len = len(document.text_before_cursor) - len(text)
        if self.should_yield_from_second(text):
            words = text.split()
            remaining_text = text[len(words[0]) :].lstrip()  # noqa E203
            move_cursor = len(text) - len(remaining_text) + stripped_len
            new_document = doc.Document(
                remaining_text,
                cursor_position=document.cursor_position - move_cursor,
            )
            yield from self.second_completer.get_completions(
                new_document,
                complete_event,
            )
        else:
            yield from self.first_completer.get_completions(document, complete_event)

    def should_yield_from_second(self, text):
        if isinstance(self.first_completer, IssueCompleter):
            return text.startswith("PYT") and " " in text
        else:
            return " " in text
