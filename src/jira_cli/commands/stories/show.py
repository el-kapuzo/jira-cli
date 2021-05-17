import click

from jira_cli.completion import IssueCompleter
from jira_cli.queries import all_stories
from .story import Story


NAME = "show"


@Story.command(NAME)
def print_details(application, issuekey):
    click.echo_via_pager(application.jira.issue(issuekey).fields.description)
    return issuekey


@Story.completion_provider(NAME)
def details_completion_provider(application):
    issues = all_stories(application.issues)
    return IssueCompleter(issues)
