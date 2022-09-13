from .command_handler import JiraCommandHandler
from .application import Application
from .completion import JiraCompleter


def resource(cls):
    command = cls.__name__.lower()
    JiraCommandHandler.resource_builder[command] = cls
    Application.resources[command] = cls
    JiraCompleter.completion_factories[command] = cls
    return cls
