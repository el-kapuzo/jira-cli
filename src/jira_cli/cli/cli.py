from jira_cli.application import Application


def getApplication():
    return Application.buildFromTomlFilePath()


def jira():
    getApplication().run()


if __name__ == "__main__":
    jira()
