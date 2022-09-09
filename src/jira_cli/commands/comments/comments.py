from jira_cli.decorators import resource
from ..resource import Resource


@resource
class Comment(Resource):
    pass
