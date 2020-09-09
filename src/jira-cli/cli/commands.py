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
def ls():
    for issue in getJira().search_issues(getJql()):
        click.echo(f"{issue.key}: {issue.fields.summary}")


if __name__ == "__main__":
    for issue in getJira().search_issues(getJql()):
        pass
    print(dir(issue))
