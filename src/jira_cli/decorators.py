from .command_handler import JiraCommands
from .application import Application


def resource(cls):
    JiraCommands.resource_builder[cls.__name__.lower()] = cls
    Application.resources[cls.__name__.lower()] = cls
    return cls
