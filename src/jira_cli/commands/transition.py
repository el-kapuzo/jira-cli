import click


def transition_issue(application, issuekey, resolution_name):
    jira = application.jira
    issue = jira.issue(issuekey)
    transition_name_to_id = {t["name"]: t["id"] for t in jira.transitions(issue)}
    resolution_id = transition_name_to_id.get(resolution_name)
    if resolution_id:
        jira.transition_issue(issue, resolution={"id": resolution_id})
    else:
        click.echo("[WARN]: Transition not possible", color="red")
