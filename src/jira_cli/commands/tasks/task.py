from jira_cli.commands.resource import Resource
from jira_cli.decorators import resource


@resource
class Task(Resource):
    pass
