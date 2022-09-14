import prompt_toolkit.completion as completion
from .fuzzy_nested_completer import FuzzyNestedCompleter


class JiraCompleter(completion.Completer):
    completion_factories = {}

    def __init__(self, application, *args, **kwargs):
        completer_map = {
            name: builder(application)
            for name, builder in self.completion_factories.items()
        }
        _resolve_aliases(application.config.aliases, completer_map)
        self.completer = FuzzyNestedCompleter(completer_map)
        super().__init__(*args, **kwargs)

    def get_completions(self, document, complete_event):
        yield from self.completer.get_completions(document, complete_event)

    @classmethod
    def addCommand(cls, command, completer=None):
        completer = completer or completion.DummyCompleter()
        cls.completion_factories[command] = lambda x: completer


def _resolve_aliases(aliases, completer_map):
    alias_completer_map = {}
    for alias, expansion in aliases.items():
        _completer_map = completer_map
        for part in expansion.split():
            completer = _completer_map.get(part, completion.DummyCompleter())
            if isinstance(completer, FuzzyNestedCompleter):
                _completer_map = completer.completer_map
        alias_completer_map[alias] = completer
    completer_map.update(alias_completer_map)
