import click


def list_stories(application):
    colorMap = {"Bug": "red", "Sub-task": "blue"}
    ignoreIssueTypes = {"Sub-task"}
    for issue in application.issues:
        issueType = str(issue.fields.issuetype)
        if issueType not in ignoreIssueTypes:
            click.secho(
                f"{issue.key}: {issue.fields.summary}", fg=colorMap.get(issueType)
            )
