from typing import Dict
import dataclasses

import toml
import jira as jira_api


@dataclasses.dataclass
class Server:
    url: str
    user: str
    token: str

    def connect(self):
        return jira_api.JIRA(server=self.url, basic_auth=(self.user, self.token))


@dataclasses.dataclass
class Settings:
    jql: str
    prompt: str


@dataclasses.dataclass
class Aliases:
    aliases: Dict

    def get(self, key, default=None):
        return self.aliases.get(key, default)

    def __getitem__(self, key):
        return self.aliases[key]


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
