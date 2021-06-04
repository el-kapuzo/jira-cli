from jira_cli.completion import IssueCompleter

from .worklog import Worklog


NAME = "new"


@Worklog.command(NAME)
def log_time(application, issuekey, time):
    jira = application.jira
    issue = jira.issue(issuekey)
    try:
        jira.add_worklog(issue, timeSpent=time, reduceBy=time)
    except Exception:
        jira.add_worklog(issue, timeSpent=time)
    return issue


@Worklog.completion_provider(NAME)
def log_time_completions(application):
    return IssueCompleter.subtask_completer(application, ignore_statuses=["Done"])
