import time

import click
from prompt_toolkit import prompt

from jira_cli.decorators import command, completion_provider
from jira_cli.queries import all_subtasks
from jira_cli.completion import IssueCompleter

from .transition import transition_issue
from .log_time import log_time


NAME = "track"


@command(NAME)
def track_task(application, issuekey):
    issue = application.jira.issue(issuekey)
    transition_issue(
        application, issuekey, "In Progress"
    )  # TODO: what is the name of the transition target
    click.echo(f"    Working on {issuekey}: {issue.fields.summary}...")

    start_time = time.perf_counter()
    pressed_button = _wait_for_resolution()
    stop_time = time.perf_counter()

    elapsed_time = stop_time - start_time
    worklog_time = _elapsed_time_to_jira_time(elapsed_time)
    log_time(application, issuekey, worklog_time)
    if pressed_button == "F":
        transition_issue(application, issuekey, "Done")
    return issuekey


def _wait_for_resolution():
    pressed_button = None
    click.echo("Print (P) for pause  or (F) to finish work")
    while pressed_button not in ["P", "F"]:
        value = prompt("(P) / (F) > ")
        pressed_button = value.upper()[0]
    return pressed_button


def _elapsed_time_to_jira_time(elapsed_time_in_s):
    elapsed_time = int(elapsed_time_in_s)
    elapsed_time_in_min = elapsed_time // 60
    return f"{elapsed_time_in_min}m"


@completion_provider(NAME)
def track_task_completions(application):
    issues = all_subtasks(application.issues)
    return IssueCompleter(issues, ignore_statuses=["Done"])
