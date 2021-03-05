import time

import click
from prompt_toolkit import prompt

from .transition import transition_issue
from .log_time import log_time


def track_task(application, issuekey):
    transition_issue(
        application, "In Progress"
    )  # TODO: what is the name of the transition target
    click.echo("Press (P) to pause work, or (F) to finish work")

    start_time = time.perf_counter()
    pressed_button = _work_on(issuekey)
    stop_time = time.perf_counter()

    elapsed_time = stop_time - start_time
    worklog_time = _elapsed_time_to_jira_time(elapsed_time)
    log_time(application, issuekey, worklog_time)
    if pressed_button == "F":
        transition_issue(
            application, "Done"
        )  # TODO: what is the name of the transition target


def _work_on(issuekey):
    pressed_button = None
    while pressed_button not in ["P", "F"]:
        value = prompt(f"Working on {issuekey}... ")
        pressed_button = value.upper()[0]
    return pressed_button


def _elapsed_time_to_jira_time(elapsed_time_in_s):
    elapsed_time = int(elapsed_time_in_s)
    elapsed_time_in_min = elapsed_time // 60
    return f"{elapsed_time_in_min}m"
