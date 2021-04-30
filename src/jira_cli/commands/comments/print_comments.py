from jira_cli.completion import IssueCompleter
import click

from .comments import Comments

NAME = "show"


@Comments.command(NAME)
def print_comments(application, issuekey):
    jira = application.jira
    comments = jira.comments(issuekey)
    for comment in comments:
        author = comment.author.displayName
        body = comment.body
        click.secho(f"Author: {author}", fg="blue", bold=True)
        click.echo(f"\n\n{body}\n\n")
    return issuekey


@Comments.completion_provider(NAME)
def print_comments_completer(application):
    return IssueCompleter(application.issues)
