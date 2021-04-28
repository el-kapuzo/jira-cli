## Implement the following commands
+ [x] Transition Task
+ [x] Work on task -> maybe transition to active and track time
+ [x] Add time estimate to subtask
+ [x] Add comment to issue
+ [x] List all comments on an issue
+ [x] Add subtask to story
  + [x] Completer: IssueCompleter for all stories
  + [x] Include estimate
+ [x] Add estimate
+ [ ] Download all attachments
+ [ ] Add a attachment
+ [ ] Set JQL
  + [ ] shortcuts for current sprint, all future sprints

## Refactor: Resource Based commands
+ [ ] Subcomand completer
+ [ ] (Sub)task
  + [ ] list
  + [ ] new
  + [ ] update 
  + [ ] track
  + [ ] worklog
  + [ ] ...
  + [ ] comment
  + [ ] list comments

## Autocompletion Features
+ [x] For initial commands
+ [x] For arguments to commands
+ [x] Refactor: create utilites to generate completions from a list of issues
+ [x] Autocompletion based on summary (title) of tasks
  + [x] Implement basic autocompletieon
  + [x] Make it case insensitve
  + [x] Add option to ignore tasks based on their status
  + [x] _smart case_
+ [x] Fuzzy completion for commands
+ [ ] Options to sort subtaks by last viewed userstory (via details / subtasks command)
+ [ ] Options to sort subtaks by last worked on userstory (via track / worklog command)
+ [ ] Different Handling of PR Review tasks in history
+ [ ] Ignore Commands in History:
  + [ ] Comment (add / view)
  + [ ] Transition
+ [ ] Options to sort by type
+ [ ] Make history persistent over sessions?
+ [ ] Fuzzy matching against title of issue?
+ [x] Auto-completions for transitions
+ [ ] Include basic JQL completion engine?
+ [ ] Display Meta: Issue-Type (or Parent Story)?

## House-Keeping
+ [x] Auto-import all commands files to apply decorators
+ [ ] install dependencies
+ [ ] maybe do not use click and colorama
  + [ ] all output is handled by prompt_toolkit
  + [ ] startup is done without click (optional)


## Make it look nicer
+ [ ] Colorful prompt
+ [ ] Presenter
  + [x] Issue Presenter
  + [ ] Detail Presenter
  + [ ] Comment Presenter
  + [ ] Render richText (maybe try `pip install rich` and a rst->md converter)

## Configuration
+ [ ] Colormaps
+ [ ] Presenter Options (once presenter are implemented)
+ [ ] Define available Transitions
+ [ ] Define available Story-Types
