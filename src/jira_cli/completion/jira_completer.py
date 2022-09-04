import collections
import prompt_toolkit.completion as completion


def get_dummy_provider(*args, **kwargs):
    return completion.DummyCompleter()


class JiraCompleter(completion.Completer):
    completion_factories = collections.defaultdict(default_factor=get_dummy_provider)

    def __init__(self, jira_tasks, *args, **kwargs):
        self.completors = None
        self.command_completer = completion.FuzzyCompleter(
            completion.WordCompleter(
                list(self.application.commands.keys()),
                ignore_case=True,
            ),
        )
        self.sync()
        super().__init__(*args, **kwargs)

    def sync(self):
        self.completors = {
            command: completion_factory(self.application)
            for command, completion_factory in self.completion_factories.items()
        }

    def get_completions(self, document, complete_event):
        text = document.text_before_cursor
        if " " not in text:
            yield from self.command_completer.get_completions(document, complete_event)
        else:
            command = text.split(" ")[0]
            completer = self.completors.get(command, completion.DummyCompleter())
            yield from completer.get_completions(document, complete_event)
