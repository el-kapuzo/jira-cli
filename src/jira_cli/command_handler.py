from prompt_toolkit.shortcuts import clear
from jira_cli.completion.jira_completer import JiraCompleter


def buildCommandDispatcher(application):
    handler = CommandDispatcher(application.config.aliases)
    handler.add_observer(JiraCommandHandler(application))
    handler.add_observer(ApplicationCommandHandler(application))
    return handler


class CommandDispatcher:
    def __init__(self, aliases):
        self.observers = []
        self.aliases = aliases

    def dispatch_command(self, command, *args):
        command, *alias_args = self.aliases.resolve_alias(command)
        for observer in self.observers:
            observer.dispatch_command(command, *alias_args, *args)

    def add_observer(self, observer):
        self.observers.append(observer)


class JiraCommandHandler:
    resource_builder = {}

    def __init__(self, application):
        self.resources = {
            name: builder(application.jiraTasks)
            for name, builder in self.resource_builder.items()
        }
        self.application = application

    def dispatch_command(self, command, *args):
        handler = self.resources.get(command, None)
        if handler:
            handler.dispatch_command(*args)


class ApplicationCommandHandler:
    JiraCompleter.addCommand("sync")
    JiraCompleter.addCommand("exit")
    JiraCompleter.addCommand("clear")

    def __init__(self, application):
        self.application = application

    def dispatch_command(self, command, *_):
        application = self.application
        if command == "exit":
            application.running = False
        if command == "sync":
            application.sync()
        if command == "clear":
            clear()
