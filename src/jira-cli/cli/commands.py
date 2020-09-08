import pathlib

import click
import toml


def getConfig():
    path = pathlib.Path.home() / 'jira-cli' / 'jira.config'
    with open(path, 'r') as f:
        return toml.loads(f.read())


@click.group
def jira():
    pass

@jira.command
def ls():
    pass

