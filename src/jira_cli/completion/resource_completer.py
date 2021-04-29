from prompt_toolkit import completion
from prompt_toolkit.document import Document


class RecourceCompleter(completion.Completer):
    def __init__(self, resource):
        self.command_completer = completion.FuzzyWordCompleter(
            list(resource.command_handlers.keys())
        )
        self.completers = {
            name: completion_provider()
            for name, completion_provider in resource.completion_providers.items()
        }

    def get_completions(self, document, complete_event):
        text = document.text_before_cursor.lstrip()
        stripped_len = len(document.text_before_cursor) - len(text)
        words = text.split(" ")
        if len(words) <= 1:
            yield from self.command_completer
        else:
            remaining_text = text[len(words[0]) :].lstrip()
            move_cursor = len(text) - len(remaining_text) + stripped_len
            new_document = Document(
                remaining_text, cursor_position=document.cursor_position - move_cursor
            )
            completer = self.completers.get(words[0], completion.DummyCompleter())
            yield from completer.get_completions(new_document, complete_event)
