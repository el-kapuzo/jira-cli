from prompt_toolkit.completion import Completion


def completions_from_issues(issues, word_before_cursor):
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
