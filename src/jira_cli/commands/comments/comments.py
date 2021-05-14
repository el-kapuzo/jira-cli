from jira_cli.decorators import resource
from ..resource import ResourceMixin


@resource
class Comment(ResourceMixin):
    command_handlers = {}
    completion_providers = {}
