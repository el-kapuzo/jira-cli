import collections
import prompt_toolkit.completion as completion
import prompt_toolkit


def get_dummy_provider(*args, **kwargs):
    return completion.DummyProvider()


class JiraCompleter(completion.Completer):
    completion_factories = collections.defaultdict(default_factor=get_dummy_provider)

    def __init__(self, application, *args, **kwargs):
        self.application = application
        self.completors = {
            command: completion_factory(application)
            for command, completion_factory in self.completion_factories.items()
        }
        self.command_completer = completion.FuzzyCompleter(
            completion.WordCompleter(list(self.completors.keys()), ignore_case=False)
        )
        super().__init__(*args, **kwargs)

    def get_completions(self, document, complete_event):
        text = document.text_before_cursor
        if " " not in text:
            yield from self.command_completer.get_completions(document, complete_event)
        else:
            command = text.split()[0]
            completer = self.completors[command]
            remaining_text = text[len(command) :].lstrip()
            move_cursor = len(text) - len(remaining_text)
            remaining_document = prompt_toolkit.Document(remaining_text, move_cursor)
            yield from completer.get_completions(remaining_document, complete_event)
