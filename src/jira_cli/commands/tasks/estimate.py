from prompt_toolkit import prompt
from jira_cli.completion import IssueCompleter

from .task import Task


NAME = "estimate"


@Task.command(NAME)
def add_estimate(application, issuekKey, estimate=None):
    issue = application.jira.issue(issuekKey)
    if estimate is None:
        estimate = prompt("estimate:  ")
    fields = {"timetracking": {"orignialEstimate": estimate}}
    issue.update(fields=fields)
    return issuekKey


@Task.completion_provider(NAME)
def add_task_completion_provider(application):
    return IssueCompleter.subtask_completer(
        application, ignore_statuses=["In Progress", "Done"]
    )


def _transform_estimate(estimate):
    time, unit = float(estimate[:-1]), estimate[-1]
    if unit == "m":
        time = time * 60
    elif unit == "h":
        time = time * 60 * 60
    else:
        raise ValueError("Unknown time unit")
    return int(time)
