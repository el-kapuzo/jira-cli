from jira_cli.queries import all_subtasks
from jira_cli.decorators import command, completion_provider
from jira_cli.completion import IssueCompleter

NAME = "worklog"


@command(NAME)
def log_time(application, issuekey, time):
    jira = application.jira
    issue = jira.issue(issuekey)
    try:
        jira.add_worklog(issue, timeSpent=time, reduceBy=time)
    except Exception:
        jira.add_worklog(issue, timeSpent=time)
    return issue


@completion_provider(NAME)
def log_time_completions(application):
    issues = all_subtasks(application.issues)
    return IssueCompleter(issues, ignore_statuses=["Done"])
