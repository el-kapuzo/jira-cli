import pathlib
import click
import toml
import prompt_toolkit
import jira as jira_api

from jira_cli.completion import FuzzyNestedCompleter
from jira_cli.issue_presenter import IssuePresenter


class Application:
    resources = {}

    def __init__(self, jira, jql):
        self.jira = jira
        self.jql = jql
        self.issues = jira.search_issues(jql, maxResults=False)
        self.resources = {name: cls() for name, cls in self.resources}
        self.presenter = IssuePresenter()
        self.completer = self.build_completer()
        self.running = False
        self._debugging = True

    def build_completer(self):
        completer_dict = {
            name: resource.get_completer(self)
            for name, resource in self.resources.items()
        }
        completer_dict["exit"] = prompt_toolkit.completion.DummyCompleter()
        completer_dict["sync"] = prompt_toolkit.completion.DummyCompleter()
        return FuzzyNestedCompleter()

    def sync(self):
        self.issues = self.jira.search_issues(self.jql, maxResults=False)
        self.completer = self.build_completer()

    def dispatch_command(self, command_string, *args):
        if command_string == "exit":
            self.running = False
            return
        if command_string == "sync":
            self.sync()
            return
        try:
            self.resources[command_string].dispatch_command(self, *args)
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

    def run(self):
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
