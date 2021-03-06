def is_story(issue):
    ignoreIssueTypes = {"Sub-task"}
    return str(issue.fields.issuetype) not in ignoreIssueTypes
