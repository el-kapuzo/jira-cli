def all_stories(issues):
    ignoreIssueTypes = {"Sub-task"}
    for issue in issues:
        if str(issue.fields.issuetype) not in ignoreIssueTypes:
            yield issue
