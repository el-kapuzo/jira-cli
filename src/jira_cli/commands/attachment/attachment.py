from jira_cli.commands.resource import Resource
from jira_cli.decorators import resource


@resource
class Attachment(Resource):

    # TOOD: remove this, when every cli-resource is refactored
    def dispatch_command(self, application, command, *args):
        return self.command_handlers[command](self, *args)
