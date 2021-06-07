from prompt_toolkit.completion import FuzzyWordCompleter
from prompt_toolkit import print_formatted_text, HTML
from jira_cli.completion import ChainCompleter, IssueCompleter

from .task import Task

NAME = "move"


@Task.command(NAME)
def transition_issue(application, issuekey, *resolution_names):
    resolution_name = " ".join(resolution_names)
    jira = application.jira
    issue = jira.issue(issuekey)
    transition_name_to_id = {t["name"]: t["id"] for t in jira.transitions(issue)}
    resolution_id = transition_name_to_id.get(resolution_name)
    if resolution_id:
        jira.transition_issue(issue, resolution_id)
    else:
        print_formatted_text(
            HTML("<ansired><b>[WARN]:</b> Transition not possible</ansired>")
        )
    return issue


@Task.completion_provider(NAME)
def transitions_completions(application):
    return ChainCompleter(
        IssueCompleter.subtask_completer(application),
        FuzzyWordCompleter(["To-Do", "In Progress", "Done"]),
    )
