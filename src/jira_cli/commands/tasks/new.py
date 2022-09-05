from prompt_toolkit import prompt

from jira_cli.completion import IssueCompleter

from .task import Task

NAME = "new"


@Task.command(NAME)
def add_subtask(self: Task, storyKey):
    summary = prompt("title:  ")
    estimation = prompt("estimate:  ")
    if estimation == "" or estimation is None:
        estimation = "0m"
    self.jiraTasks.add_sub_task(storyKey, summary, estimation)


@Task.completion_provider(NAME)
def add_task_completion_provider(application):
    return IssueCompleter.story_completer(application.jiraTasks)


def _transform_estimate(estimate):
    time, unit = float(estimate[:-1]), estimate[-1]
    if unit == "m":
        time = time * 60
    elif unit == "h":
        time = time * 60 * 60
    else:
        raise ValueError("Unknown time unit")
    return int(time)
