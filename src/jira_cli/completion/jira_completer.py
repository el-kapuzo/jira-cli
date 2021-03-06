import collections
import prompt_toolkit.completion as completion


def get_dummy_provider(*args, **kwargs):
    return completion.DummyProvider()


class JiraCompleter(completion.Completer):
    completion_factories = collections.defaultdict(default_factor=get_dummy_provider)

    def __init__(self, application, *args, **kwargs):
        self.application = application
        self.completors = {
            command: completion_factory(application)
            for command, completion_factory in self.completion_factories.items()
        }
        self.command_completer = completion.FuzzyCompleter(
            completion.WordCompleter(list(self.completors.keys()), ignore_case=False)
        )
        super().__init__(*args, **kwargs)

    def get_completions(self, document, complete_event):
        document_text_list = document.text.split(" ")
        if len(document_text_list) < 2:
            yield from self.command_completer.get_completions(document, complete_event)
        else:
            command = document_text_list[0]
            yield from self.completors[command].get_completions(
                document, complete_event
            )
