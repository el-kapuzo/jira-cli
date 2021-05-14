from jira_cli.commands.resource import ResourceMixin
from jira_cli.decorators import resource


@resource
class Task(ResourceMixin):
    command_handlers = {}
    completion_providers = {}
