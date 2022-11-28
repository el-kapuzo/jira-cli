from prompt_toolkit import prompt
from jira_cli.completion import IssueCompleter

from .task import Task


NAME = "estimate"


@Task.command(NAME)
def add_estimate(self: Task, issuekKey, estimation=None):
    if estimation is None:
        estimation = prompt("estimate:  ")
    task = self.jiraTasks.task_for(issuekKey)
    task.estimate(estimation)
    return issuekKey


@Task.completion_provider(NAME)
def add_task_completion_provider(application):
    return IssueCompleter.subtask_completer(
        application.jiraTasks,
        ignore_statuses=["In Progress", "Done"],
    )
