import datetime


class PendingWorklog:
    def __init__(self):
        self.startedAt = datetime.datetime.now()

    @property
    def timeSpent(self):
        timeDelta: datetime.timedelta = datetime.datetime.now() - self.startedAt
        timeInSeconds = timeDelta.total_seconds()
        return f"{timeInSeconds // 60}m"

    def commit(self, jiraTask):
        return jiraTask.add_worklog(self.timeSpent, self.startedAt)
