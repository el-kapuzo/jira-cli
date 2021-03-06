from jira_cli.queries import all_subtasks
from jira_cli.decorators import command, completion_provider
from jira_cli.completion import IssueCompleter

NAME = "worklog"


@command(NAME)
def log_time(application, issuekey, time):
    jira = application.jira
    try:
        jira.add_worklog(issuekey, timeSpent=time, reduceBy=time)
    except Exception:
        jira.add_worklog(issuekey, timeSpent=time)


@completion_provider(NAME)
def log_time_completions(application):
    issues = all_subtasks(application.issues)
    return IssueCompleter(issues)
