from prompt_toolkit import print_formatted_text, HTML


color_map = {
    "Bug": ("<ansired>", "</ansired>"),
    "In Progress": ("<ansiblue>", "</ansiblue>"),
    "Done": ("<ansigreen>", "</ansigreen>"),
}


def print_issue(issue):
    issue_status = issue.status
    issue_type = str(issue.issue_type)
    if issue_status == "Done":
        startColor, endColor = color_map.get("Done", ("", ""))
    else:
        startColor, endColor = color_map.get(issue_status, ("", ""))
        if issue_type == "Bug":
            startColor, endColor = color_map.get(issue_type, ("", ""))
    print_formatted_text(
        HTML(
            f"    {startColor}<b>{issue.key}</b>: {issue.summary}{endColor}",
        ),
    )
