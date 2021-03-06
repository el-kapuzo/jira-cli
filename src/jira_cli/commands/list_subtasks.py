import click
from jira_cli.queries import all_stories, subtasks_of_issue
from jira_cli.decorators import command, completion_provider
from jira_cli.completion import IssueCompleter

NAME = "subtasks"


@command(NAME)
def list_subtasks(application, issuekey):
    story = application.jira.issue(issuekey)
    for issue in subtasks_of_issue(story):
        click.echo(f"{issue.key}: {issue.fields.summary}")
    return issuekey


@completion_provider(NAME)
def completion_provieder_list_stories(application):
    return IssueCompleter(all_stories(application.issues))
