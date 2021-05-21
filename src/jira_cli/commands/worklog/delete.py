from jira_cli.queries import all_subtasks
from jira_cli.completion import IssueCompleter

from .worklog import Worklog


NAME = "delete"


@Worklog.command(NAME)
def log_time(application, issuekey, worklog_id):
    jira = application.jira
    jira.worklog(issuekey, worklog_id).delete()


@Worklog.completion_provider(NAME)
def log_time_completions(application):
    issues = all_subtasks(application.issues)
    return IssueCompleter(issues, ignore_statuses=["Done"])
