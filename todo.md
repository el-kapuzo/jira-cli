## Bugs
+ [x] add estimate to subtask (both on create and on its own) does not work
  + Possible solution: there might be a `timetracking` sub-object.
+ [x] issue completer does not work after refactoring
+ [x] resource.commands without completion do not show up in autocompletion

## Refactor: Resource Based commands
+ [x] Implement a suitable completion engine
  + [x] Fuzzy nested completer
  + [x] Resource can create its completer
  + [x] Attachment id completer
  + [ ] Worklog id completer
  + [ ] Comment id completer
  + [ ] merge to "id" completer?
+ [ ] Add possibility to define aliases
+ [ ] Implement the following resources with commands / queries
  + [x] (Sub)task
    + [x] list
    + [x] new
    + [x] update
    + [x] track
    + [x] estimate
  + [x] comment
    + [x] new
    + [x] list comments
    + [x] print
  + [x] stories
    + [x] list all subtasks
    + [x] list
    + [x] new
    + [x] print details
  + [x] attachment
    + [x] list
    + [x] new
    + [x] download
  + [x] worklog
    + [x] new
    + [x] list
    + [x] delete

## Configuration
...

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
+ [x] install dependencies
+ [ ] maybe do not use click and colorama
  + [ ] all output is handled by `prompt_toolkit`
  + [ ] use `richt` to render colorful text
  + [ ] startup is done without click (optional)


## Make it look nicer
+ [ ] Colorful prompt
+ [ ] Render richText (maybe try `pip install rich` and a rst-> md converter)
  + [ ] Maybe rich can render (a subset of) rst markup directly?
  + [ ] Implement a simple rst -> md converter

## Configuration
+ [ ] Colormaps
+ [ ] Presenter Options (once presenter are implemented)
+ [ ] Define available Transitions
+ [ ] Define available Story-Types
