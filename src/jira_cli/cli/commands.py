import pathlib

import click
import toml
import jira as jira_api


def getConfig():
    path = pathlib.Path.home() / "jira-cli" / "jira.config"
    with open(path, "r") as f:
        return toml.loads(f.read())


def getJira():
    serverSettings = getConfig()["server"]
    return jira_api.JIRA(
        server=serverSettings["server"],
        basic_auth=(serverSettings["user"], serverSettings["api_token"]),
    )


def getJql():
    return getConfig()["settings"]["jql"]


@click.group()
def jira():
    pass


@jira.command()
@click.option(
    "--jql",
    default=None,
    type=click.STRING,
    help="List keys and summary of result of JQL.",
)
@click.option("--all", "-a", is_flag=True)
def ls(jql, all):
    jqlToPerforme = jql or getJql()
    colorMap = {"Bug": "red", "Sub-task": "blue"}
    ignoreIssueTypes = {"Sub-task"}
    for issue in getJira().search_issues(jqlToPerforme, maxResults=False):
        issueType = str(issue.fields.issuetype)
        if all or issueType not in ignoreIssueTypes:
            click.secho(
                f"{issue.key}: {issue.fields.summary}", fg=colorMap.get(issueType)
            )


@jira.command()
@click.argument("issuekey")
def details(issuekey):
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
