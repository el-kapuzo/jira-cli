import click
from jira_cli.queries import is_story, is_subtask


class IssuePresenter:
    def __init__(self):
        self.color_map = {"Bug": "red", "In Progress": "blue", "Done": "green"}

    def print_issue(self, issue):
        color = None
        if is_story(issue):
            color = self.color_map.get(str(issue.fields.issuetype))
        if is_subtask(issue):
            color = self.color_map.get(issue.fields.status.name)
        click.secho(f"    {issue.key}: {issue.fields.summary}", fg=color)
