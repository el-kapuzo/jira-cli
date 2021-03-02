import click


def list_subtasks(application, issueKey):
    story = application.jira.issue(issueKey)
    for issue in story.fields.subtasks:
        click.echo(f"{issue.key}: {issue.fields.summary}")
