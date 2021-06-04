## Bugs

## Make it look nicer
+ [ ] Render richText (maybe try `pip install rich` and a rst-> md converter)
  + [ ] There is a `pygments` lexer for rst (for syntax highlighting)
  + [ ] Implement a small rst -> md converter


## Completion
+ [x] Alternative contructor for IssueCompleter for _all subtasks_ and _all stories_ from application
+ [ ] Comment id completer
+ [ ] Worklog id completer
+ [ ] Options to sort subtaks by last viewed userstory (via details / subtasks command)
+ [ ] Options to sort subtaks by last worked on userstory (via track / worklog command)
+ [ ] Different Handling of PR Review tasks in history
+ [ ] Ignore Commands in History:
  + [ ] Comment (add / view)
  + [ ] Transition
+ [ ] Options to sort by type
+ [ ] Make history persistent over sessions?
+ [ ] Include basic JQL completion engine?

## House-Keeping
+ [ ] maybe do not use click and colorama
  + [ ] all output is handled by `prompt_toolkit` and `rich`
  + [ ] startup is done without click (optional)


## Configuration
+ [ ] Colormaps
+ [ ] Define available Transitions
+ [ ] Define available Story-Types
