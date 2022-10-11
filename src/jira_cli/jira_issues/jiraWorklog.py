import jira


class JiraWorklog:
    def __init__(self, worklog: jira.Worklog):
        self.worklog = worklog

    @property
    def id(self):
        return self.worklog.id

    @property
    def author(self):
        return self.worklog.author

    @property
    def timeSpent(self):
        return self.worklog.timeSpent

    def delete(self):
        self.worklog.delete()
