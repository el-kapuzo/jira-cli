from prompt_toolkit import HTML, print_formatted_text, prompt

from jira_cli.completion import IssueCompleter
from jira_cli.jira_issues.pendingWorklog import PendingWorklog
from .task import Task

NAME = "track"


@Task.command(NAME)
def track_task(self: Task, issuekey):
    jira_task = self.jiraTasks.task_for(issuekey)
    jira_task.start_working()
    try:
        print_formatted_text(
            HTML(f"    Working on <b>{jira_task.key}</b>: {jira_task.summary}..."),
        )
    except Exception:
        print(f"    Working on {jira_task.key}: {jira_task.summary}...")
    # TODO: this can be done with some generator magic
    # or even with a context-manager just for the fun :D
    worklog = PendingWorklog()
    pressed_button = _wait_for_resolution()
    worklog.commit(jira_task)
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


@Task.completion_provider(NAME)
def track_task_completions(application):
    return IssueCompleter.subtask_completer(
        application.jiraTasks,
        ignore_statuses=["Done"],
    )
