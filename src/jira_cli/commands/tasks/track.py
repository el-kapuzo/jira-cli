from prompt_toolkit import HTML, print_formatted_text, prompt

from jira_cli.completion import IssueCompleter
from .task import Task

NAME = "track"


@Task.command(NAME)
def track_task(self: Task, issuekey):
    jira_task = self.jiraTasks.task_for(issuekey)
    try:
        print_formatted_text(
            HTML(f"    Working on <b>{jira_task.key}</b>: {jira_task.summary}..."),
        )
    except Exception:
        print(f"    Working on {jira_task.key}: {jira_task.summary}...")

    tracker = jira_task.track()
    tracker.send(None)
    tracker.send(_wait_for_resolution())


def _wait_for_resolution():
    pressed_button = None
    print_formatted_text(
        HTML("Print <i>(P)</i> for pause  or <i>(F)</i> to finish work"),
    )
    while pressed_button not in ["P", "F"]:
        value = prompt("(P) / (F) > ")
        pressed_button = value.upper()[0]
    task_finished = pressed_button == "F"
    return task_finished


@Task.completion_provider(NAME)
def track_task_completions(application):
    return IssueCompleter.subtask_completer(
        application.jiraTasks,
        ignore_statuses=["Done"],
    )
