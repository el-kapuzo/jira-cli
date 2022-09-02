import jira_cli.issue_presenter

from .story import Story


@Story.command("list")
def list_stories(self: Story):
    for story in self.jiraTasks.iter_stories():
        jira_cli.issue_presenter.print_issue(story)
