from jira_cli.completion import IssueCompleter

from .worklog import Worklog


NAME = "delete"


@Worklog.command(NAME)
def log_time(self: Worklog, issuekey, worklog_id):
    # TODO: this is kind of ugly... but to tidy up we need to wrap JiraWorklogs
    jira = self.jiraTasks.jira
    jira.worklog(issuekey, worklog_id).delete()


@Worklog.completion_provider(NAME)
def log_time_completions(application):
    return IssueCompleter.subtask_completer(application, ignore_statuses=["Done"])
