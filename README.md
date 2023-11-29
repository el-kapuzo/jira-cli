# JIRA-Cli

An interactive prompt to manage my daily JIRA-workflow inside my terminal.

## Install

1. Clone this repsotiroy: `git clone https://codeberg.org/dapo/jira-cli.git
2. (Optionally) Create a python venv, and activate it
3. Run `pip install <path/to/jira-cli>`
4. Create an API-Token for the JIRA REST-api

## Usage
You have to add a config file at `<path/to/jira-cli>/jira.config`.
Then, (activate the venv you created earlier and) run `jira`.
The programm will fetch all tasks and start an interactive prompt.
The prompt has decent autocompletion and the individual actions should be discoverable.

## Config
Befor you can write the config file, you need an API-token for your JIRA-instance.
The config file must be a .toml file with the following structure
```
[server]
url = <URL>
user = <username>
token = <API-Token>

[settings]
jql = <the JQL-query to fetch the tasks>
prompt = <a prompt>

[aliases]
alias = <expansion>
# more aliases
```
