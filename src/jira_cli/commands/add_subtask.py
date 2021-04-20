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
    fields = {
        "project": {"key": "PYT"},
        "summary": summary,
        "timeoriginalestimate": estimate,
        "timeestimate": estimate,
        "issuetype": "Sub-task",
        "parent": {"key": storyKey},
    }
    application.jira.create_issue(fields=fields)


@completion_provider(NAME)
def add_task_completion_provider(application):
    return IssueCompleter(all_stories(application.issues))
