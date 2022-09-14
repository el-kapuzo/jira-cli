import dataclasses
from typing import Dict

import jira as jira_api
import toml


@dataclasses.dataclass
class Server:
    url: str
    user: str
    token: str
    _connection = None

    def connect(self):
        if self._connection is None:
            self._connection = jira_api.JIRA(
                server=self.url,
                basic_auth=(self.user, self.token),
            )
        return self._connection


@dataclasses.dataclass
class Settings:
    jql: str
    prompt: str


@dataclasses.dataclass
class Aliases:
    aliases: Dict

    def items(self):
        return self.aliases.items()

    def get(self, key, default=None):
        return self.aliases.get(key, default)

    def __iter__(self):
        return iter(self.aliases)

    def __getitem__(self, key):
        return self.aliases[key]

    def resolve_alias(self, key):
        return self.get(key, key).split()


@dataclasses.dataclass
class Config:
    server: Server
    settings: Settings
    aliases: Aliases

    @classmethod
    def fromDict(cls, configDict):
        server = Server(**configDict["server"])
        settings = Settings(**configDict["settings"])
        aliases = Aliases(configDict["aliases"])
        return cls(server=server, settings=settings, aliases=aliases)

    @classmethod
    def fromFilePath(cls, filePath):
        with open(filePath, "r") as f:
            return cls.fromDict(toml.loads(f.read()))
