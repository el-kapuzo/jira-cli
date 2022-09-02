from jira_cli.decorators import resource
from ..resource import Resource


@resource
class Comment(Resource):

    # TOOD: remove this, when every cli-resource is refactored
    def dispatch_command(self, application, command, *args):
        return self.command_handlers[command](self, *args)
