import click
from jira_cli.queries import all_stories
from jira_cli.decorators import command


@command("stories")
def list_stories(application):
    colorMap = {"Bug": "red", "Sub-task": "blue"}
    for issue in all_stories(application.issues):
        issueType = str(issue.fields.issuetype)
        click.secho(f"{issue.key}: {issue.fields.summary}", fg=colorMap.get(issueType))
