import click
from jira_cli.completion import TransitionCompleter


from jira_cli.decorators import command, completion_provider
from jira_cli.queries import all_subtasks


NAME = "update"


@command(NAME)
def transition_issue(application, issuekey, *resolution_names):
    resolution_name = " ".join(resolution_names)
    jira = application.jira
    issue = jira.issue(issuekey)
    transition_name_to_id = {t["name"]: t["id"] for t in jira.transitions(issue)}
    resolution_id = transition_name_to_id.get(resolution_name)
    if resolution_id:
        jira.transition_issue(issue, resolution_id)
    else:
        click.echo("[WARN]: Transition not possible", color="red")
    return issue


@completion_provider(NAME)
def transitions_completions(application):
    issues = all_subtasks(application.issues)
    return TransitionCompleter(issues)
