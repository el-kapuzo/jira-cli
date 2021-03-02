import pathlib
import toml
import jira as jira_api


class Application:
    commands = {}

    def __init__(self, jira, jql):
        self.jira = jira
        self.issues = jira.search_issues(jql, maxResults=False)

    def dispatch_command(self, command_string, *args):
        self.commands[command_string](self, *args)

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
