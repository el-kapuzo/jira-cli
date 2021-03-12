from jira_cli.decorators import command


@command("exit")
def exit(application):
    application.running = False
