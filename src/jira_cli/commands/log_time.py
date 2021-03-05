from prompt_toolkit.completion import Completion
from jira_cli.queries import all_subtasks
from jira_cli.decorators import command, completion_provider

NAME = "worklog"


@command(NAME)
def log_time(application, issuekey, time):
    jira = application.jira
    try:
        jira.add_worklog(issuekey, timeSpent=time, reduceBy=time)
    except Exception:
        jira.add_worklog(issuekey, timeSpent=time)


@completion_provider(NAME)
def log_time_completions(application, word_before_cursor):
    for issue in all_subtasks(application.issues):
        if issue.key.startswith(word_before_cursor):
            yield Completion(
                issue.key,
                start_position=-len(word_before_cursor),
                display=f"{issue.key}: {issue.fields.summary}",
            )
