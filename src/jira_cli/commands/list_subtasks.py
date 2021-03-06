import click
from jira_cli.queries import all_stories
from jira_cli.decorators import command, completion_provider
from jira_cli.completion import IssueCompleter

NAME = "subtasks"


@command(NAME)
def list_subtasks(application, issueKey):
    story = application.jira.issue(issueKey)
    for issue in story.fields.subtasks:
        click.echo(f"{issue.key}: {issue.fields.summary}")


@completion_provider(NAME)
def completion_provieder_list_stories(application):
    return IssueCompleter(all_stories(application.issues))
