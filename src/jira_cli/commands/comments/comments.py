from jira_cli.decorators import resource
from ..resource import ResourceMixin


@resource
class Comments(ResourceMixin):
    command_handlers = {}
    completion_providers = {}
