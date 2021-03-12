import collections

from jira_cli.queries import is_story, is_subtask, get_story_of_subtask

HistoryRecord = collections.namedtuple("HistoryRecord", "command,args")


class CommandHistory:
    def __init__(self):
        self.history = []
        self.last_used_story = None
        self.stories_ranking = collections.defaultdict(int)

    def add_command(self, command_string, issue, *args):
        self.history.append(HistoryRecord(command_string, args))
        if is_story(issue):
            self.stories_ranking[issue.issuekey] += 1
            self.last_used_story = issue
        if is_subtask(issue):
            story = get_story_of_subtask(issue)
            self.stories_ranking[story.issuekey] += 1
            self.last_used_story = story
