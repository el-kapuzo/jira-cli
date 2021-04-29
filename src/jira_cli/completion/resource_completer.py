from prompt_toolkit import completion


class RecourceCompleter(completion.Completer):
    def __init__(self, resource, *args, **kwargs):
        self.resource = resource
        self.command_completer = completion.FuzzyCompleter(list(self.cls.command_handlers.keys())
