from jira_cli.completion import IssueCompleter
from .comments import Comment


NAME = "list"


@Comment.command(NAME)
def list_comments(app, issuekey=None):
    if issuekey is None:
        for issue in app.issues:
            print_comment_meta(issue)
    else:
        print_comment_meta(app.jira.comments(issuekey))


def print_comment_meta(issue):
    for comment in issue.fields.comment.comments:
        id = comment.id
        author = comment.author.displayName
        time = comment.created
        print(f"    {id}: by {author}, {time}")


@Comment.completion_provider(NAME)
def print_comments_completer(application):
    return IssueCompleter.story_completer(application)
