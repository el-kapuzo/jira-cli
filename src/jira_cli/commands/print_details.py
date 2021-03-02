import click


def print_details(application, issueKey):
    click.echo_via_pager(application.jira.issue(issueKey).fields.description)
