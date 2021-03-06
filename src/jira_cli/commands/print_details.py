import click


from jira_cli.decorators import command, completion_provider
from jira_cli.queries import all_stories
from jira_cli.completion import IssueCompleter

NAME = "details"


@command(NAME)
def print_details(application, issueKey):
    click.echo_via_pager(application.jira.issue(issueKey).fields.description)


@completion_provider(NAME)
def details_completion_provider(application):
    issues = all_stories(application.issues)
    return IssueCompleter(issues)
