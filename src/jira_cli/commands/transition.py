import click

from prompt_toolkit.completion import Completion

from jira_cli.decorators import command, completion_provider
from jira_cli.queries import all_subtasks
from jira_cli.completion import completions_from_issues


NAME = "update"


@command(NAME)
def transition_issue(application, issuekey, *resolution_names):
    resolution_name = " ".join(resolution_names)
    jira = application.jira
    issue = jira.issue(issuekey)
    transition_name_to_id = {t["name"]: t["id"] for t in jira.transitions(issue)}
    resolution_id = transition_name_to_id.get(resolution_name)
    if resolution_id:
        jira.transition_issue(issue, resolution_id)
    else:
        click.echo("[WARN]: Transition not possible", color="red")


@completion_provider(NAME)
def transitions_completions(application, word_before_cursor):
    issues = all_subtasks(application.issues)
    yield from completions_from_issues(issues)
