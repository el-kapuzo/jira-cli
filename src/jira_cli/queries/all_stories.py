from .is_story import is_story


def all_stories(issues):
    for issue in issues:
        if is_story(issue):
            yield issue
