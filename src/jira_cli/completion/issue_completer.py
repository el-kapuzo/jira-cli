from prompt_toolkit.completion import Completion, Completer


class IssueCompleter(Completer):
    def __init__(self, issues, *args, **kwargs):
        self.issues = issues
        super().__init__(*args, **kwargs)

    # TODO: refine for better completion
    def get_completions(self, document, completion_event):
        word_before_cursor = document.word_before_cursor
        issues = self.issues
        for issue in issues:
            issuekey = issue.key
            summary = issue.fields.summary
            if _is_completion(issuekey, summary, word_before_cursor):
                yield Completion(
                    issuekey,
                    start_position=-len(word_before_cursor),
                    display=f"{issuekey}: {summary}",
                )


def _is_completion(issuekey, summary, word_before_cursor):
    return issuekey.startswith(word_before_cursor) or summary.startswith(
        word_before_cursor
    )
