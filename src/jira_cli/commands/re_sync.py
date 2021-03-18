from jira_cli.decorators import command


@command("sync")
def sync(application):
    application.sync()
