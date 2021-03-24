import pathlib
import click
import toml
import prompt_toolkit
import jira as jira_api

from jira_cli.issue_presenter import IssuePresenter

from .completion import JiraCompleter
from .history import CommandHistory


class Application:
    commands = {}

    def __init__(self, jira, jql):
        self.jira = jira
        self.jql = jql
        self.issues = jira.search_issues(jql, maxResults=False)
        self.history = CommandHistory()
        self.presenter = IssuePresenter()
        self.running = False
        self.completer = JiraCompleter(self)
        self._debugging = True

    def sync(self):
        self.issues = self.jira.search_issues(self.jql, maxResults=False)
        self.completer.sync()

    def dispatch_command(self, command_string, *args):
        # issue = None
        try:
            self.commands[command_string](self, *args)
        except KeyError as e:
            click.secho(f"Command {command_string} not known", color="red")
            if self._debugging:
                print(e)
        except Exception as e:
            click.secho(
                f"Invalid arguments {args} for command {command_string}", color="red"
            )
            if self._debugging:
                print(e)
        # else:
        # self.history.add_command(command_string, self.jira.issue(issue), *args)

    def run(self):
        self.sync()
        session = prompt_toolkit.PromptSession("PYT >>> ", completer=self.completer)
        self.running = True
        while self.running:
            inputs = session.prompt().split()
            if len(inputs) == 0:
                continue
            if len(inputs) > 1:
                command, args = inputs[0], inputs[1:]
            else:
                command = inputs[0]
                args = []
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
