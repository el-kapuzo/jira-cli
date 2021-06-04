from jira_cli.completion import IssueCompleter
from .worklog import Worklog

NAME = "list"


@Worklog.command(NAME)
def list_worklogs(app, issuekey=None):
    if issuekey is None:
        print("Not yet implemented")
    else:
        worklogs = app.jira.worklogs(issuekey)
        for worklog in worklogs:
            print(f"    Id: {worklog.id}, {worklog.author}, {worklog.timeSpent}")


@Worklog.completion_provider(NAME)
def list_worklog_completion_provider(app):
    return IssueCompleter.subtask_completer(app)
