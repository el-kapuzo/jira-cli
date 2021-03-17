import click


class IssuePresenter:
    def __init__(self):
        self.color_map = {"Bug": "red", "In Progress": "blue", "Done": "green"}

    def print_issue(self, issue):
        color = None
        issue_status = issue.fields.status.name
        issue_type = str(issue.fields.issuetype)
        if issue_status == "Done":
            color = self.color_map.get("Done")
        else:
            color = self.color_map.get(issue_status)
            if issue_type == "Bug":
                color = self.color_map.get(issue_type)
        click.secho(f"    {issue.key}: {issue.fields.summary}", fg=color)
