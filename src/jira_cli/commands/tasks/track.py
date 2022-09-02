import time

from prompt_toolkit import HTML, print_formatted_text, prompt

from jira_cli.completion import IssueCompleter
from .task import Task

NAME = "track"


@Task.command(NAME)
def track_task(self: Task, issuekey):
    jira_task = self.jiraTasks.task_for(issuekey)
    jira_task.start_working()
    print_formatted_text(
        HTML(f"    Working on <b>{jira_task.key}</b>: {jira_task.summary}..."),
    )

    start_time = time.perf_counter()
    pressed_button = _wait_for_resolution()
    stop_time = time.perf_counter()

    elapsed_time = stop_time - start_time
    worklog_time = _elapsed_time_to_jira_time(elapsed_time)
    jira_task.add_worklog(worklog_time)
    if pressed_button == "F":
        jira_task.close()
    return issuekey


def _wait_for_resolution():
    pressed_button = None
    print_formatted_text(
        HTML("Print <i>(P)</i> for pause  or <i>(F)</i> to finish work"),
    )
    while pressed_button not in ["P", "F"]:
        value = prompt("(P) / (F) > ")
        pressed_button = value.upper()[0]
    return pressed_button


def _elapsed_time_to_jira_time(elapsed_time_in_s):
    elapsed_time = int(elapsed_time_in_s)
    elapsed_time_in_min = elapsed_time // 60
    return f"{elapsed_time_in_min}m"


@Task.completion_provider(NAME)
def track_task_completions(application):
    return IssueCompleter.subtask_completer(application, ignore_statuses=["Done"])
