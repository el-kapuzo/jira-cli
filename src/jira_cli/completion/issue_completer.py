from prompt_toolkit.completion import Completion, Completer


class IssueCompleter(Completer):
    def __init__(self, issues, *args, ignore_statuses=None, **kwargs):
        self.issues = list(issues)
        if ignore_statuses is None:
            self.ignore_status = set()
        else:
            self.ignore_status = set(ignore_statuses)
        super().__init__(*args, **kwargs)

    def get_completions(self, document, completion_event):
        already_typed_text = document.text_before_cursor
        typed_command = already_typed_text.split(" ")[0]
        text_for_completion = already_typed_text[len(typed_command) :].lstrip()
        issues = self.issues
        for issue in issues:
            issuekey = issue.key
            summary = issue.fields.summary
            issue_status = issue.fields.status.name
            if issue_status not in self.ignore_status:
                if _is_completion(issuekey, summary, text_for_completion):
                    yield Completion(
                        issuekey,
                        start_position=-len(text_for_completion),
                        display=f"{issuekey}: {summary}",
                    )


def _is_completion(issuekey, summary: str, already_typed_text: str):
    if already_typed_text.islower():
        return (already_typed_text in issuekey) or summary.lower().startswith(
            already_typed_text.lower()
        )
    else:
        return (already_typed_text in issuekey) or summary.startswith(
            already_typed_text
        )
