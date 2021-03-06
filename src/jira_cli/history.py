import collections

from jira_cli.queries import is_story, is_subtask

HistoryRecord = collections.namedtuple("HistoryRecord", "command,args")


class CommandHistory:
    def __init__(self):
        self.history = []
        self.last_used_story = None
        self.last_used_subtask = None

    def add_command(self, command_string, issue, *args):
        self.history.append(HistoryRecord(command_string, args))
        if is_story(issue):
            self.last_used_story = issue
        if is_subtask(issue):
            self.last_used_subtask = issue
