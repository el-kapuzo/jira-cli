from prompt_toolkit.completion import Completion


def completions_from_issues(issues, word_before_cursor):
    for issue in issues:
        if issue.key.startswith(word_before_cursor):
            yield Completion(
                issue.key,
                start_position=-len(word_before_cursor),
                display=f"{issue.key}: {issue.fields.summary}",
            )
