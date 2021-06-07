from .story import Story

from jira_cli.completion import IssueCompleter


NAME = "close"


@Story.command(NAME)
def close_story(application, issuekey):
    jira = application.jira
    issue = jira.issue(issuekey)
    transition_name_to_id = {t["name"]: t["id"] for t in jira.transitions(issue)}
    resolution_id = transition_name_to_id.get("Done")
    jira.transition_issue(issue, resolution_id)


@Story.completion_provider(NAME)
def close_story_completion_provider(application):
    return (
        IssueCompleter.story_completer(application, ignore_statuses=["To-Do", "Done"]),
    )
