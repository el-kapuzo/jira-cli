from jira_cli.completion import IssueCompleter

from .worklog import Worklog


NAME = "new"


@Worklog.command(NAME)
def log_time(self: Worklog, issuekey, time):
    task = self.jiraTasks.task_for(issuekey)
    task.add_worklog(time)


@Worklog.completion_provider(NAME)
def log_time_completions(application):
    return IssueCompleter.subtask_completer(
        application.jiraTasks,
        ignore_statuses=["Done"],
    )
