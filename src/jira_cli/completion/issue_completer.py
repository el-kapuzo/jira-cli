from prompt_toolkit.completion import Completion, Completer


class IssueCompleter(Completer):
    def __init__(self, issues, *args, **kwargs):
        self.issues = issues
        super().__init__(*args, **kwargs)

    # TODO: refine for better completion
    def get_completions(self, document, completion_event):
        already_typed_text = document.text_before_cursor
        issues = self.issues
        for issue in issues:
            issuekey = issue.key
            summary = issue.fields.summary
            if _is_completion(issuekey, summary, already_typed_text):
                yield Completion(
                    issuekey,
                    start_position=-len(already_typed_text),
                    display=f"{issuekey}: {summary}",
                )


def _is_completion(issuekey, summary, already_typed_text):
    return (already_typed_text in issuekey) or summary.startswith(already_typed_text)
