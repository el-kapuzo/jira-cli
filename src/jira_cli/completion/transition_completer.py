from prompt_toolkit import completion
from .issue_completer import IssueCompleter


class TransitionCompleter(completion.Completer):
    def __init__(self, jiraTasks, *args, **kwargs) -> None:
        self.issueCompleter = IssueCompleter.subtask_completer(jiraTasks)
        self.jiraTasks = jiraTasks
        super().__init__(*args, **kwargs)

    def get_completions(self, document, complete_event):
        already_typed_text = document.text_before_cursor
        typed_words = already_typed_text.split(" ")
        if len(typed_words) < 1 or not typed_words[0].startswith("PYT-"):
            yield from self.issueCompleter.get_completions(document, complete_event)
        else:
            typed_for_transition = " ".join(typed_words[1:])
            transitions = list(
                self.jiraTasks.task_for(typed_words[0]).available_transitions,
            )
            for word in transitions:
                if word.lower().startswith(typed_for_transition.lower()):
                    yield completion.Completion(
                        word,
                        start_position=-len(typed_for_transition),
                    )
