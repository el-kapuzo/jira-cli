from prompt_toolkit import print_formatted_text, HTML


class IssuePresenter:
    def __init__(self):
        self.color_map = {
            "Bug": ("<ansired>", "</ansired>"),
            "In Progress": ("<ansiblue>", "</ansiblue>"),
            "Done": ("<ansigreen>", "</ansigreen>"),
        }

    def print_issue(self, issue):
        startColor, endColor = "", ""
        issue_status = issue.fields.status.name
        issue_type = str(issue.fields.issuetype)
        if issue_status == "Done":
            startColor, endColor = self.color_map.get("Done", ("", ""))
        else:
            startColor, endColor = self.color_map.get(issue_status, ("", ""))
            if issue_type == "Bug":
                startColor, endColor = self.color_map.get(issue_type, ("", ""))
        print_formatted_text(
            HTML(
                f"    {startColor}<b>{issue.key}</b>: {issue.fields.summary}{endColor}",
            ),
        )
