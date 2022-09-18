# JIRA-Cli

An interactive prompt to manage my daily JIRA-workflow inside my terminal.

## Install

1. Clone this repsotiroy:
```sh
git clone https://github.com/el-kapuzo/jira-cli
```
2. (Optionally) Create a python venv, and activate it
3. Run `pip install <path/to/jira-cli>`

## Usage
You have to add a config file at `<path/to/jira-cli>/jira.config`.
Then, if you have the venv actiavted run `jira`.
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
