from prompt_toolkit.shortcuts import clear


def buildCommandHandler(application):
    handler = CommandHandler()
    handler.add_observer(JiraCommands(application))
    handler.add_observer(ApplicationCommands(application))
    return handler


class CommandHandler:
    def __init__(self):
        self.observers = []

    def dispatch_command(self, command, *args):
        for observer in self.observers:
            observer.dispatch_command(command, *args)

    def add_observer(self, observer):
        self.observers.append(observer)


class JiraCommands:
    resource_builder = {}

    def __init__(self, application):
        self.aliases = application.config.aliases
        self.resources = {
            name: builder() for name, builder in self.resource_builder.items()
        }
        self.application = application

    def dispatch_command(self, command, *args):
        command, *alias_args = self.aliases.resolve_alias(command)
        handler = self.resources.get(command, None)
        if handler:
            handler.dispatch_command(self.application, *alias_args, *args)


class ApplicationCommands:
    def __init__(self, application):
        self.application = application

    def dispatch_command(self, command):
        application = self.application
        if command == "exit":
            application.running = False
        if command == "sync":
            application.sync()
        if command == "clear":
            clear()
