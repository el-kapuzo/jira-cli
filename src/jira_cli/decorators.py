from .application import Application
from .completion import JiraCompleter


def command(name):
    def decorator(fun):
        Application.commands[name] = fun
        return fun


def completion_provider(name):
    def decorator(fun):
        JiraCompleter.completion_factories[name] = fun
        return fun
