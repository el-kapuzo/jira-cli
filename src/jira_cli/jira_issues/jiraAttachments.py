import pathlib

import jira


class JiraAttachment:
    def __init__(self, jira: jira.JIRA, attachment):
        self.jira = jira
        self.attachment = attachment

    @property
    def id(self) -> str:
        return self.attachment.id

    @property
    def filename(self) -> str:
        return self.attachment.filename

    def download(self, path: pathlib.Path):
        assert path.is_dir()  # noqa:
        target_path = path / self.filename
        with open(target_path, "wb+") as f:
            for chunk in self.attachment.iter_content():
                f.write(chunk)
