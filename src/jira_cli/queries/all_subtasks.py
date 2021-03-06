from .is_subtask import is_subtask


def all_subtasks(issues):
    for issue in issues:
        if is_subtask(issue):
            yield issue
