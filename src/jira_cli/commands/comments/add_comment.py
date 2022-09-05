from prompt_toolkit import prompt
from jira_cli.completion import IssueCompleter
from .comments import Comment

NAME = "new"


@Comment.command(NAME)
def add_comment(self: Comment, issuekey):
    body = prompt("#   ", multiline=True)
    self.jiraTasks.task_for(issuekey).add_comment(body)
    return issuekey


@Comment.completion_provider(NAME)
def add_comment_completer(application):
    return IssueCompleter.story_completer(application.jiraTasks)
