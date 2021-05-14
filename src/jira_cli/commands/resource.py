from jira_cli.completion import FuzzyNestedCompleter


class ResourceMixin:
    def dispatch_command(self, app, command, *args):
        command_handler = self.command_handlers.get(command, self.default_handler)
        return command_handler(app, *args)

    def default_handler(self, app, *args):
        self.help()

    def get_completer(self, app):
        completer_map = {
            name: completion_provider(app)
            for name, completion_provider in self.completion_providers.items()
        }
        return FuzzyNestedCompleter(completer_map)

    def help(self):
        # TODO: implement something
        pass

    @classmethod
    def command(cls, name):
        def decorator(func):
            cls.command_handlers[name] = func
            return func

        return decorator

    @classmethod
    def completion_provider(cls, name):
        def decorator(func):
            cls.completion_providers[name] = func
            return func

        return decorator
