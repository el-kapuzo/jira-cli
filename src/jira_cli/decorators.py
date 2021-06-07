from .application import Application


def resource(cls):
    Application.resources[cls.__name__.lower()] = cls
    return cls
