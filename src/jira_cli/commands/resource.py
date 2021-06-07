from prompt_toolkit.completion import DummyCompleter
from jira_cli.completion import FuzzyNestedCompleter


class ResourceMixin:
    def get_completer(self, application):
        completer_map = {
            name: completion_provider(application)
            for name, completion_provider in self.completion_providers.items()
        }
        for name in self.command_handlers.keys():
            if not name in completer_map:
                completer_map[name] = DummyCompleter()
        return FuzzyNestedCompleter(completer_map)

    def dispatch_command(self, application, command, *args):
        self.command_handlers[command](application, *args)

    @classmethod
    def command(cls, name):
        def decorator(fun):
            cls.command_handlers[name] = fun
            return fun

        return decorator

    @classmethod
    def completion_provider(cls, name):
        def decorator(fun):
            cls.completion_providers[name] = fun
            return fun

        return decorator
