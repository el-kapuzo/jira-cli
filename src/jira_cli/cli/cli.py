import click

from jira_cli.application import Application


def getApplication():
    return Application.buildFromTomlFilePath()


@click.command()
def jira():
    app = getApplication()
    app.run()
