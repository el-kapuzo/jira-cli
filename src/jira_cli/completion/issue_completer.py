from prompt_toolkit.completion import Completion, Completer


class IssueCompleter(Completer):
    def __init__(
        self,
        jiraTasks,
        *args,
        ignore_statuses=None,
        parent_in_meta=False,
        **kwargs,
    ):
        self.jira_tasks = jiraTasks
        if ignore_statuses is None:
            self.ignore_status = set()
        else:
            self.ignore_status = set(ignore_statuses)
        self.parent_in_meta = parent_in_meta
        super().__init__(*args, **kwargs)

    def get_completions(self, document, completion_event):
        already_typed_text = document.text_before_cursor
        for task in self._iter_tasks():
            issuekey = task.key
            summary = task.summary
            issue_status = task.status
            if self.parent_in_meta:
                parent = self.jira_tasks.associated_story(issuekey)
                display_meta = (
                    f"{parent.key}: {' '.join(parent.summary.split()[:2])}..."  # noqa
                )
            else:
                display_meta = None
            if issue_status not in self.ignore_status:
                if _is_completion(issuekey, summary, already_typed_text):
                    yield Completion(
                        issuekey,
                        start_position=-len(already_typed_text),
                        display=f"{issuekey}: {summary}",
                        display_meta=display_meta,
                    )

    def _iter_tasks(self):
        yield from self.jira_tasks

    @classmethod
    def subtask_completer(cls, jira_tasks, ignore_statuses=None):
        return SubtaskCompleter(
            jira_tasks,
            ignore_statuses=ignore_statuses,
            parent_in_meta=True,
        )

    @classmethod
    def story_completer(cls, jira_tasks, ignore_statuses=None):
        return StoryCompleter(jira_tasks, ignore_statuses=ignore_statuses)


class StoryCompleter(IssueCompleter):
    def _iter_tasks(self):
        yield from self.jira_tasks.iter_stories()


class SubtaskCompleter(IssueCompleter):
    def _iter_tasks(self):
        yield from self.jira_tasks.iter_subtasks()


def _is_completion(issuekey, summary: str, already_typed_text: str):
    if already_typed_text.islower():
        return (already_typed_text in issuekey) or summary.lower().startswith(
            already_typed_text.lower(),
        )
    else:
        return (already_typed_text in issuekey) or summary.startswith(
            already_typed_text,
        )
