from jira_cli.completion import IssueCompleter
from .worklog import Worklog

NAME = "list"


@Worklog.command(NAME)
def list_worklogs(self: Worklog, issuekey=None):
    if issuekey is None:
        print("Not yet implemented. Please provide an issuekey.")
    else:
        for worklog in self.jiraTasks.task_for(issuekey).worklogs():
            print(f"    Id: {worklog.id}, {worklog.author}, {worklog.timeSpent}")


@Worklog.completion_provider(NAME)
def list_worklog_completion_provider(app):
    return IssueCompleter.subtask_completer(app.jiraTasks)
