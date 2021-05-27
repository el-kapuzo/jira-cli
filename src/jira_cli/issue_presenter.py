import rich


class IssuePresenter:
    def __init__(self):
        self.color_map = {"Bug": "red", "In Progress": "blue", "Done": "green"}

    def print_issue(self, issue):
        color = "white"
        issue_status = issue.fields.status.name
        issue_type = str(issue.fields.issuetype)
        if issue_status == "Done":
            color = self.color_map.get("Done", "white")
        else:
            color = self.color_map.get(issue_status, "white")
            if issue_type == "Bug":
                color = self.color_map.get(issue_type, "white")
        rich.print(f"    [{color}][bold]{issue.key}[/bold]: {issue.fields.summary}")
