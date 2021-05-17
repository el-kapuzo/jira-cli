from jira_cli.queries import all_stories

from .story import Story


@Story.command("list")
def list_stories(application):
    presenter = application.presenter
    for issue in all_stories(application.issues):
        presenter.print_issue(issue)
