import prompt_toolkit.completion as completion
from .issue_completer import IssueCompleter

from jira_cli.queries import all_subtasks


class HistoryAwareIssueCompleter(completion.Completer):
    def __init__(self, issues, history):
        self.issues = list(issues)
        self.issuekeys = set(issue.issuekey for issue in self.issues)
        self.history = history

    def get_completions(self, document, completion_event):
        issues = self._sort_issues_based_on_history()
        issue_completer = IssueCompleter(issues)
        yield from issue_completer.get_completions(document, completion_event)

    def _sort_issues_based_on_history(self):
        rankedIssues = []
        issues = list(self.issues)
        for issue in all_subtasks(self.history.last_used_stories):
            if issue.issuekey in self.issuekeys:
                rankedIssues.append(issue)
                issues.remove(issue)
        rankedIssues.extend(issues)
        return rankedIssues
