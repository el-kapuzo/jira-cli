import pathlib
import click
import toml
import prompt_toolkit
import jira as jira_api

from .completion import JiraCompleter
from jira_cli.commands import (
    list_stories,
    list_subtasks,
    print_details,
    log_time,
    transition_issue,
    track_task,
)


class Application:
    commands = {
        "stories": list_stories,
        "subtasks": list_subtasks,
        "details": print_details,
        "worklog": log_time,
        "update": transition_issue,
        "track": track_task,
    }

    def __init__(self, jira, jql):
        self.jira = jira
        self.issues = jira.search_issues(jql, maxResults=False)
        self._debugging = True

    def dispatch_command(self, command_string, *args):
        try:
            self.commands[command_string](self, *args)
        except Exception as e:
            click.echo(f"Command {command_string} not known", color="red")
            if self._debugging:
                print(e)

    def run(self):
        session = prompt_toolkit.PromptSession(
            "PYT >>> ", completer=JiraCompleter(self)
        )
        running = True
        while running:
            inputs = session.prompt().split()
            if len(inputs) == 0:
                continue
            if len(inputs) > 1:
                command, args = inputs[0], inputs[1:]
            else:
                command = inputs[0]
                args = []
            if command == "exit":
                running = False
            else:
                self.dispatch_command(command, *args)

    @classmethod
    def buildFromSettings(cls, settings):
        serverSettings = settings["server"]
        jira = jira_api.JIRA(
            server=serverSettings["server"],
            basic_auth=(serverSettings["user"], serverSettings["api_token"]),
        )
        return cls(jira, settings["settings"]["jql"])

    @classmethod
    def buildFromTomlFilePath(cls, tomlFilePath=None):
        path = tomlFilePath or pathlib.Path.home() / "jira-cli" / "jira.config"
        with open(path, "r") as f:
            return cls.buildFromSettings(toml.loads(f.read()))
