from jira_cli.application import Application


def jira():
    Application.buildFromTomlFilePath().run()


if __name__ == "__main__":
    jira()
