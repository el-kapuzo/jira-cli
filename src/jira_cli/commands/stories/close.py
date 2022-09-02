from .story import Story

from jira_cli.completion import IssueCompleter


NAME = "close"


@Story.command(NAME)
def close_story(self: Story, issuekey):
    self.jiraTasks.task_for(issuekey).close()


@Story.completion_provider(NAME)
def close_story_completion_provider(application):
    return IssueCompleter.story_completer(
        application,
        ignore_statuses=["To-Do", "Done"],
    )
