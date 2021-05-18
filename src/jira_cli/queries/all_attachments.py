def all_attachments(issues):
    for issue in issues:
        yield from issue.fields.attachment
