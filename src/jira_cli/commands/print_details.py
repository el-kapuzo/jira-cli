import click

from prompt_toolkit.completion import Completion

from jira_cli.decorators import command, completion_provider
from jira_cli.queries import all_stories


NAME = "details"


@command(NAME)
def print_details(application, issueKey):
    click.echo_via_pager(application.jira.issue(issueKey).fields.description)


@completion_provider(NAME)
def details_completion_provider(application, word_before_cursor):
    for issue in all_stories(application.issues):
        if issue.key.startswith(word_before_cursor):
            yield Completion(
                issue.key,
                start_position=-len(word_before_cursor),
                display=f"{issue.key}: {issue.fields.summary}",
            )
