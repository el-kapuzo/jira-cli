import click

from jira_cli.application import Application


def getApplication():
    return Application.buildFromTomlFilePath()


@click.group()
def jira():
    pass


@jira.command()
def ls():
    getApplication().dispatch_command("stories")


@jira.command()
@click.argument("issue-key")
def subtasks(issue_key):
    getApplication().dispatch_command("subtasks", issue_key)


@jira.command()
def details(issuekey):
    getApplication().dispatch_command("details", issue_key)
    click.echo_via_pager(getJira().issue(issuekey).fields.description)


@jira.command()
@click.argument("issueKey", type=str)
@click.argument("timeInHours", type=str)
def logtime(issuekey, timeinhours):
    jira = getJira()
    jira.add_worklog(issuekey, timeSpent=timeinhours)


if __name__ == "__main__":
    print(dir(getJira().issue("DP-1000").fields))
    # for issue in getJira().search_issues(getJql()):
    #     print(issue.fields.issuetype)
    #     print(type(issue.fields.issuetype))
