from prompt_toolkit.completion import DummyCompleter
from jira_cli.completion import FuzzyNestedCompleter


class Resource:
    def __init__(self, jiraTasks):
        self.jiraTasks = jiraTasks

    @property
    def completion_providers(self):
        return getattr(self.__class__, "_completion_providers", dict())

    @property
    def command_handlers(self):
        return getattr(self.__class__, "_command_handlers", dict())

    def get_completer(self, application):
        completer_map = {
            name: completion_provider(application)
            for name, completion_provider in self.completion_providers.items()
        }
        for name in self.command_handlers.keys():
            if name not in completer_map:
                completer_map[name] = DummyCompleter()
        return FuzzyNestedCompleter(completer_map)

    # TOOD: remove this, when every cli-resource is refactored
    def dispatch_command(self, application, command, *args):
        return self.command_handlers[command](self, *args)

    @classmethod
    def buildCompleter(cls, application):
        completer_factories = getattr(cls, "_completion_providers", {})
        completer_map = {
            name: completion_provider(application)
            for name, completion_provider in completer_factories.items()
        }
        return FuzzyNestedCompleter(completer_map)

    @classmethod
    def command(cls, name):
        def decorator(fun):
            if not hasattr(cls, "_command_handlers"):
                cls._command_handlers = {}
            cls._command_handlers[name] = fun
            cls.completion_provider(name)(lambda x: DummyCompleter())
            return fun

        return decorator

    @classmethod
    def completion_provider(cls, name):
        def decorator(fun):
            if not hasattr(cls, "_completion_providers"):
                cls._completion_providers = {}
            cls._completion_providers[name] = fun
            return fun

        return decorator

    @classmethod
    def presenter(cls, name):
        def decorator(fun):
            if not hasattr(cls, "presenters"):
                cls.presenters = {}
            cls.presenter[name] = fun
            return fun
