import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

requirements = ["prompt_toolkit", "click", "colrama", "jira", "rich"]

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
        jira=jira_cli.cli.cli:jira
        """,
)
