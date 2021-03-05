def all_subtasks(issues):
    for issue in issues:
        if str(issue.fields.issuetype) in {"Sub-taks"}:
            yield issue
