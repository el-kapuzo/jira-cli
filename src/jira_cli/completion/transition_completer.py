from prompt_toolkit import completion
from .issue_completer import IssueCompleter


class TransitionCompleter(completion.Completer):
    def __init__(self, issues, *args, **kwargs) -> None:
        self.issueCompleter = IssueCompleter(issues)
        self.transitions = ["To-Do", "In Progress", "Done"]
        super().__init__(*args, **kwargs)

    def get_completions(self, document, complete_event):
        already_typed_text = document.text_before_cursor
        typed_words = already_typed_text.split(" ")
        if len(typed_words) < 3:
            yield from self.issueCompleter.get_completions(document, complete_event)
        else:
            typed_for_transition = " ".join(typed_words[2:])
            for word in self.transitions:
                if word.startswith(typed_for_transition):
                    yield completion.Completion(
                        word, start_position=-len(typed_for_transition)
                    )
