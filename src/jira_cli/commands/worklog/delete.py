from jira_cli.completion import IssueCompleter

from .worklog import Worklog


NAME = "delete"


@Worklog.command(NAME)
def log_time(self: Worklog, issuekey, worklog_id):
    self.jiraTasks.task_for(issuekey).delete_worklog(worklog_id)


@Worklog.completion_provider(NAME)
def log_time_completions(application):
    return IssueCompleter.subtask_completer(
        application.jiraTasks,
        ignore_statuses=["Done"],
    )
