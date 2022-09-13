import pathlib

import prompt_toolkit
import prompt_toolkit.completion

import jira_cli.jira_issues.jiraTasks
from jira_cli.completion import JiraCompleter
from .command_handler import buildCommandDispatcher
from .config import Config


class Application:
    aliases = {
        "ls": ("story", "list"),
        "t": ("task", "track"),
        "lt": ("task", "list"),
        "tm": ("task", "move"),
    }
    resources = {}

    def __init__(self, config: Config):
        self.config = config
        self.jira = config.server.connect()
        self.jql = config.settings.jql
        self.jiraTasks = jira_cli.jira_issues.jiraTasks.JiraTasks.fromConfig(config)
        self.issues = []
        self.resources = {
            name: cls(self.jiraTasks) for name, cls in self.resources.items()
        }
        self.running = False
        self.command_handler = buildCommandDispatcher(self)
        self.session = prompt_toolkit.PromptSession(
            prompt_toolkit.HTML("<ansiblue><b>[PYT]</b></ansiblue> ❯ "),
            completer=prompt_toolkit.completion.DummyCompleter(),
        )

    def sync(self):
        self.issues = list(
            self.jira.search_issues(
                self.jql,
                fields=["attachment", "status", "summary", "issuetype", "parent"],
                maxResults=False,
            ),
        )
        self.session.completer = JiraCompleter(self)

    def dispatch_command(self, command_string, *args):
        try:
            self.command_handler.dispatch_command(command_string, *args)
        except Exception as e:
            print(e)

    def run(self):
        self.sync()
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
    def buildFromTomlFilePath(cls, tomlFilePath=None):
        path = tomlFilePath or pathlib.Path.home() / "jira-cli" / "jira.config"
        return cls(Config.fromFilePath(path))
