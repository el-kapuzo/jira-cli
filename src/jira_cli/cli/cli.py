import click
from prompt_toolkit import PromptSession

from jira_cli.application import Application


def getApplication():
    return Application.buildFromTomlFilePath()


@click.group()
def jira():
    print("Hello, I am jira")


@jira.command()
def prompt():
    app = getApplication()
    app.run()


@jira.command()
def ls():
    getApplication().dispatch_command("stories")


@jira.command()
@click.argument("issue-key")
def subtasks(issue_key):
    getApplication().dispatch_command("subtasks", issue_key)


@jira.command()
@click.argument("issue-key")
def details(issue_key):
    getApplication().dispatch_command("details", issue_key)


@jira.command()
@click.argument("issueKey", type=str)
@click.argument("time", type=str)
def logtime(issuekey, time):
    getApplication().dispatch_command("worklog", issuekey, time)
