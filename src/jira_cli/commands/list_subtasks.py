import click
from prompt_toolkit.completion import Completion
from jira_cli.queries import all_stories
from jira_cli.decorators import command, completion_provider

NAME = "subtasks"


@command(NAME)
def list_subtasks(application, issueKey):
    story = application.jira.issue(issueKey)
    for issue in story.fields.subtasks:
        click.echo(f"{issue.key}: {issue.fields.summary}")


@completion_provider(NAME)
def completion_provieder_list_stories(application, word_before_cursor):
    issues = application.issues
    for issue in all_stories(issues):
        if issue.key.startswith(word_before_cursor):
            yield Completion(
                issue.key,
                start_position=-len(word_before_cursor),
                display=f"{issue.key}: {issue.fields.summary}",
            )
