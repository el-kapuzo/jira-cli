from prompt_toolkit import print_formatted_text, HTML

import jira_cli.completion

from .task import Task

NAME = "move"


@Task.command(NAME)
def transition_issue(self: Task, issuekey, *resolution_names):
    resolution_name = " ".join(resolution_names)
    jira_task = self.jiraTasks.task_for(issuekey)
    try:
        jira_task.change_lane(resolution_name)
    except KeyError:
        print_formatted_text(
            HTML("<ansired><b>[WARN]:</b> Transition not possible</ansired>"),
        )


@Task.completion_provider(NAME)
def transitions_completions(application):
    return jira_cli.completion.TransitionCompleter(application.jiraTasks)
