import importlib
import os
import pkgutil


def _importModules(*path):
    for module in pkgutil.iter_modules(
        [os.path.join(os.path.abspath(os.path.dirname(__file__)), *path)]
    ):
        if not (module.ispkg):
            importlib.import_module(
                f".{'.'.join(path)}.{module.name}", package=__name__
            )


# Import all commands
# is executed for each policy
# This way, you can just add or delete policies
# this snipped will manage this automatically for you
for path in (
    ("commands", "stories"),
    ("commands", "tasks"),
    ("commands", "comments"),
    ("commands", "attachment"),
    ("commands", "worklog"),
):
    _importModules(*path)
