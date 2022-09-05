import click

from jira_cli.completion import IssueCompleter
from .story import Story

NAME = "show"


@Story.command(NAME)
def print_details(self: Story, issuekey):
    jiraTask = self.jiraTasks.task_for(issuekey)
    click.echo_via_pager(jiraTask.descriptions)
    return issuekey


@Story.completion_provider(NAME)
def details_completion_provider(application):
    return IssueCompleter.story_completer(application.jiraTasks)
