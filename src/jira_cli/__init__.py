import importlib
import os
import pkgutil

# Import all commands
# is executed for each policy
# This way, you can just add or delete policies
# this snipped will manage this automatically for you
for module in pkgutil.iter_modules(
    [os.path.join(os.path.abspath(os.path.dirname(__file__)), "commands")]
):
    if not (module.ispkg):
        importlib.import_module(".commands.{}".format(module.name), package=__name__)
