import prompt_toolkit.completion as completion


def no_completions_provider(*_args, **_kwargs):
    yield from []


class JiraCompleter(completion.Completer):
    completion_providers = {
        "stories": no_completions_provider,
        "subtasks": no_completions_provider,
        "details": no_completions_provider,
        "worklog": no_completions_provider,
        "update": no_completions_provider,
        "track": no_completions_provider,
        "exit": no_completions_provider,
    }

    def __init__(self, application, *args, **kwargs):
        self.application = application
        super().__init__(*args, **kwargs)

    def get_completions(self, document, complete_event):
        word_before_cursor = document.get_word_before_cursor()
        document_text_list = document.text.split(" ")
        if len(document_text_list) < 2:
            yield from self._base_command_completions(word_before_cursor)
        else:
            yield from self.completion_providers.get(
                document_text_list[0], no_completions_provider
            )(self.application)

    def _base_command_completions(self, word_before_cursor):
        commands = list(self.completion_providers.keys())
        for command_string in commands:
            if command_string.startswith(word_before_cursor):
                yield completion.Completion(
                    command_string, start_position=-len(word_before_cursor)
                )
