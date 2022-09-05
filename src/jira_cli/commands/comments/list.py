import itertools

from jira_cli.completion import IssueCompleter
from .comments import Comment


NAME = "list"


@Comment.command(NAME)
def list_comments(self: Comment, issuekey=None):
    if issuekey:
        comments = self.jiraTasks.task_for(issuekey).comments
    else:
        comments = itertools.chain(
            *(task.comments for task in self.jiraTasks.iter_stories()),
        )
    print_comment_meta(comments)
    return issuekey


def print_comment_meta(comments):
    for comment in comments:
        id = comment.id
        author = comment.author.displayName
        time = comment.created
        print(f"    {id}: by {author}, {time}")


@Comment.completion_provider(NAME)
def print_comments_completer(application):
    return IssueCompleter.story_completer(application.jiraTasks)
