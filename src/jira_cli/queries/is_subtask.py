def is_subtask(issue):
    return str(issue.fields.issuetype) in {"Sub-task"}
