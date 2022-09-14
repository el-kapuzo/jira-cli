## Bugs
+ [ ] Aliases do not trigger completion
+ [x] If task has no estimation, it can not be moved to "In Progress". This lead to a discrepancy between the board and the actual status :-O

## Completion
+ [ ] Rank completion options for subtasks higher, if its parent was recently used
  + [ ] IssueCompleter can register itself to the command-dispatcher
  + [ ] Then the issue completer can implement internal Ranking logic
+ [ ] Include basic JQL completion engine?

## Make it look nicer
+ [ ] Render richText (maybe try `pip install rich` and a rst-> md converter)
  + [ ] There is a `pygments` lexer for rst (for syntax highlighting)
  + [ ] Implement a small rst renderer

## Resources
+ [ ] Config
  + [ ] Update JQL
  + [ ] shortcut for current sprint
  + [ ] shortcut for next sprint?
  + [ ] shortcut for all future sprints
+ [ ] Sprint
  + [ ] `show` current sprint (_rich_ can render tables)
  + [ ] `add` a story / bug to the current sprint

## House-Keeping
+ [ ] Refactor to new JiraTasks class



## Configuration
+ [ ] Colormaps
+ [ ] Define available Transitions
+ [ ] Define available Story-Types
