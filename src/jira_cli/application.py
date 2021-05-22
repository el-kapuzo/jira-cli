import pathlib
import click
import toml
import prompt_toolkit
import jira as jira_api

from jira_cli.completion import FuzzyNestedCompleter
from jira_cli.issue_presenter import IssuePresenter


class Application:
    aliases = {
        "ls": ("story", "list"),
        "track": ("task", "track"),
        "la": ("task", "list"),
    }
    resources = {}

    def __init__(self, jira, jql):
        self.jira = jira
        self.jql = jql
        # TODO: use a dict?
        self.issues = list(
            jira.search_issues(
                jql,
                fields=["attachment", "status", "summary", "issuetype"],
                maxResults=False,
            )
        )
        self.resources = {name: cls() for name, cls in self.resources.items()}
        self.presenter = IssuePresenter()
        self.running = False
        self.session = prompt_toolkit.PromptSession(
            "PYT >>> ", completer=self.build_completer()
        )

    def build_completer(self):
        completer_dict = {
            name: resource.get_completer(self)
            for name, resource in self.resources.items()
        }

        def get_completer_for_alias(resource, action):
            resource_completer = completer_dict[resource]
            return resource_completer.completer_map[action]

        alias_completer = {
            alias: get_completer_for_alias(*commands)
            for alias, commands in self.aliases.items()
        }
        completer_dict.update(alias_completer)

        completer_dict["exit"] = prompt_toolkit.completion.DummyCompleter()
        completer_dict["sync"] = prompt_toolkit.completion.DummyCompleter()
        return FuzzyNestedCompleter(completer_dict)

    def sync(self):
        self.issues = list(
            self.jira.search_issues(
                self.jql,
                fields=["attachment", "status", "summary", "issuetype"],
                maxResults=False,
            )
        )
        self.session.completer = self.build_completer()

    def dispatch_command(self, command_string, *args):
        resolved_command = self.aliases.get(command_string)
        if resolved_command:
            command_string = resolved_command[0]
            args = tuple(resolved_command[1:] + list(args))
        if command_string == "exit":
            self.running = False
            return
        if command_string == "sync":
            self.sync()
            return
        try:
            self.resources[command_string].dispatch_command(self, *args)
        except Exception as e:
            print(e)

    def run(self):
        self.running = True
        while self.running:
            inputs = self.session.prompt().split()
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
