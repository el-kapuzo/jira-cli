## Bugs

## Completion
+ [x] Alternative contructor for IssueCompleter for _all subtasks_ and _all stories_ from application
+ [ ] Rank completion options for subtasks higher, if its parent was recently used
  + [ ] Implement the possibility to track the last used stories
    + [ ] Maybe use a kind of Observer-Pattern???
  + [ ] The _list subtasks, worklog new, track_ commands publish the events
  + [ ] Unless the the subtask was a _PR review_
  + [ ] Or the parent was _Timetracking_
+ [ ] Include basic JQL completion engine?

## Make it look nicer
+ [ ] Render richText (maybe try `pip install rich` and a rst-> md converter)
  + [ ] There is a `pygments` lexer for rst (for syntax highlighting)
  + [ ] Implement a small rst renderer

## Resources
+ [x] Story: `close`
+ [ ] Config
  + [ ] Update JQL
  + [ ] shortcut for current sprint
  + [ ] shortcut for next sprint?
  + [ ] shortcut for all future sprints
+ [ ]
+ [ ] Sprint
  + [ ] `show` current sprint (_rich_ can render tables)
  + [ ] `add` a story / bug to the current sprint

## House-Keeping
+ [ ] maybe do not use click and colorama
  + [ ] all output is handled by `prompt_toolkit` and `rich`
+ [ ] there is a pager implemented on top of `prompt_toolkit`


## Configuration
+ [ ] Colormaps
+ [ ] Define available Transitions
+ [ ] Define available Story-Types
