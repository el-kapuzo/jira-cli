from jira_cli.commands.resource import Resource
from jira_cli.decorators import resource


@resource
class Worklog(Resource):
    command_handlers = {}
    completion_providers = {}
