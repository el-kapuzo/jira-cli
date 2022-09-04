from .command_handler import JiraCommands
from .application import Application
from .completion import JiraCompleter


def resource(cls):
    command = cls.__name__.lower()
    JiraCommands.resource_builder[command] = cls
    Application.resources[command] = cls
    JiraCompleter.completion_factories[command] = cls
    return cls
