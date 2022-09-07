class JiraAttachment:
    def __init__(self, jira, attachment):
        self.jira = jira
        self.attachment = attachment

    @property
    def id(self):
        return self.attachment.id

    @property
    def filename(self):
        return self.attachment.filename

    def download(self, path):
        target_path = path / self.filename
        with open(target_path, "wb+") as f:
            for chunk in self.attachment.iter_content():
                f.write(chunk)
