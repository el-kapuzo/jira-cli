import functools


class JiraTask:
    NOT_A_STORY_TYPE = {"Sub-task"}
    SUBTASK_TYPES = {"Sub-task"}

    def __init__(self, jira, issue):
        self.jira = jira
        self.issue = issue

    @functools.cached_property
    def transition_map(self):
        return {t["name"]: t["id"] for t in self.jira.transitions(self.issue)}

    @functools.cached_property
    def descriptions(self):
        return self.jira.issue(self.issue.key).fields.description

    @property
    def issue_key(self):
        return self.issue.key

    @property
    def is_story(self):
        return str(self.issue.fields.issuetype) not in self.NOT_A_STORY_TYPE

    @property
    def is_subtask(self):
        return str(self.issue.fields.issuetype) in self.SUBTASK_TYPES

    def associated_story(self):
        if self.is_story:
            return self
        return JiraTask(self.issue.fields.parent)

    def iter_subtasks(self):
        try:
            yield from map(lambda x: JiraTask(self.jira, x), self.issue.subtasks)
        except Exception:
            yield from ()

    def close(self):
        resolution_id = self.transition_map.get("Done")
        self.jira.transition_issue(self.issue, resolution_id)
