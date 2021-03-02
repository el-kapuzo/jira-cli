import click


def list_subtasks(application, issueKey):
    story = None
    for issue in application.issues:
        for issue in application.issues:
            if issue.key == issueKey:
                story = issue
                break
    for issue in story.fields.subtasks:
        click.echo(f"{issue.key}: {issue.fields.summary}")
