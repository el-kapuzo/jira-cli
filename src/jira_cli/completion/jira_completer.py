import collections
import prompt_toolkit.completion as completion
import prompt_toolkit


def get_dummy_provider(*args, **kwargs):
    return completion.DummyCompleter()


class JiraCompleter(completion.Completer):
    completion_factories = collections.defaultdict(default_factor=get_dummy_provider)

    def __init__(self, application, *args, **kwargs):
        self.application = application
        self.completors = {
            command: completion_factory(application)
            for command, completion_factory in self.completion_factories.items()
        }
        self.command_completer = completion.FuzzyCompleter(
            completion.WordCompleter(
                list(self.application.commands.keys()), ignore_case=True
            )
        )
        super().__init__(*args, **kwargs)

    def get_completions(self, document, complete_event):
        text = document.text_before_cursor
        if " " not in text:
            yield from self.command_completer.get_completions(document, complete_event)
        else:
            command = text.split(" ")[0]
            completer = self.completors.get(command, completion.DummyCompleter())
            yield from completer.get_completions(document, complete_event)
