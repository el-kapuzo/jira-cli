import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

requirements = ["prompt_toolkit", "click", "colorama", "jira", "rich", "toml"]

setuptools.setup(
    name="jira_cli",
    version="0.1.0",
    author="el-kap",
    author_email="el.kapuzo@mailbox.com",
    python_requires=">=3.6",
    description="A interactive terminal prompt to manage jira issues",
    package_dir={"": "src"},
    install_requires=requirements,
    packages=setuptools.find_packages("src"),
    entry_points="""
        [console_scripts]
        jira=jira_cli.cli.cli:jira
        """,
)
