import prompt_toolkit.completion as completion
from .fuzzy_nested_completer import FuzzyNestedCompleter


class JiraCompleter(completion.Completer):
    completion_factories = {}

    def __init__(self, application, *args, **kwargs):
        completor_map = {
            name: builder(application)
            for name, builder in self.completion_factories.items()
        }
        self.completor = FuzzyNestedCompleter(completor_map)
        super().__init__(*args, **kwargs)

    def get_completions(self, document, complete_event):
        yield from self.completor.get_completions(document, complete_event)

    @classmethod
    def addCommand(cls, command, completer=None):
        completer = completer or completion.DummyCompleter()
        cls.completion_factories[command] = lambda x: completer
