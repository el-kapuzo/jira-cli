from .application import Application
from .completion import JiraCompleter


def resource(cls):
    Application.resources[cls.__name__.lower()] = cls
    return cls


def command(name):
    def decorator(fun):
        Application.commands[name] = fun
        return fun

    return decorator


def completion_provider(name):
    def decorator(fun):
        JiraCompleter.completion_factories[name] = fun
        return fun

    return decorator
