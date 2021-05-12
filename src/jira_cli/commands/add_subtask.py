from prompt_toolkit import prompt
from jira_cli.decorators import command, completion_provider
from jira_cli.completion import IssueCompleter
from jira_cli.queries import all_stories


NAME = "addtask"


@command(NAME)
def add_subtask(application, storyKey):
    summary = prompt("title:  ")
    estimate = prompt("estimate:  ")
    if estimate == "" or estimate is None:
        estimate = "0m"
    time = _transform_estimate(estimate)
    fields = {
        "project": {"key": "PYT"},
        "summary": summary,
        "issuetype": "Sub-task",
        "parent": {"key": storyKey},
    }
    application.jira.create_issue(fields=fields)


@completion_provider(NAME)
def add_task_completion_provider(application):
    return IssueCompleter(all_stories(application.issues))


def _transform_estimate(estimate):
    time, unit = float(estimate[:-1]), estimate[-1]
    if unit == "m":
        time = time * 60
    elif unit == "h":
        time = time * 60 * 60
    else:
        raise ValueError("Unknown time unit")
    return int(time)
