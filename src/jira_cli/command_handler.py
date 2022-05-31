from prompt_toolkit.shortcuts import clear


class CommandHandler:
    def __init__(self):
        self.observers = []

    def dispatch_command(self, command, *args):
        for observer in self.observers:
            observer.dispatch_command(command, *args)

    def add_observer(self, observer):
        self.observers.append(observer)


class JiraCommands:
    def __init__(self, resources, aliases):
        self.resources = resources
        self.aliases = aliases

    def dispatch_command(self, command, *args):
        command, *alias_args = self.resolve_alias(command)
        handler = self.resources.get(command, None)
        if handler:
            handler.dispatch_command(*alias_args, *args)

    def resolve_alias(self, command):
        return self.aliases.get(command, (command,))


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
