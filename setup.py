import os
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

with open(
    os.path.join(os.path.dirname(os.path.abspath(__file__)), "requirements.txt"), "r"
) as requirementsFile:
    requirements = [line for line in requirementsFile]

setuptools.setup(
    name="jira_cli",  # TODO find good name
    version="0.0.1a",
    author="el-kap",
    author_email="cherrybomb@up2parts.com",
    python_requires=">=3.6,<3.9",
    description="CL-Commands to interact with jira",
    package_dir={"": "src"},
    packages=setuptools.find_packages("src"),
    entry_points="""
        [console_scripts]
        jira=jira_cli.cli.commands:jira
        """,
)
