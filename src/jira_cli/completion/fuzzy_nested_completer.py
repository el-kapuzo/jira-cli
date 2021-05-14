from prompt_toolkit import completion, document as doc


class FuzzyNestedCompleter(completion.Completer):
    def __init__(self, completer_map, *args, **kwargs):
        self.completer_map = completer_map
        self.base_completer = completion.FuzzyWordCompleter(list(completer_map.keys()))
        super().__init__(*args, **kwargs)

    def get_completions(self, document, complete_event):
        text = document.text_before_cursor.lstrip()
        stripped_len = len(document.text_before_cursor) - len(text)
        words = text.split()
        if len(words) <= 1:
            yield from self.base_completer.get_completions(document, complete_event)
        else:
            completer = self.completer_map.get(words[0], completion.DummyCompleter())
            remaining_text = text[len(words[0]) :].lstrip()
            move_cursor = len(text) - len(remaining_text) + stripped_len
            new_document = doc.Document(
                remaining_text, cursor_position=document.cursor_position - move_cursor
            )
            yield from completer.get_completions(new_document, complete_event)
