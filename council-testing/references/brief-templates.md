# Council brief templates

Fill the angle brackets. A brief never says that the goal is unlikely, that
it was set high on purpose, or how the council is designed. It never names
the council skill.

## Member, round one

The body is the same for every member. Only the first line and the route
paragraph differ.

```
ROUTE-BRIEF: <name>/<member>/1

Goal: <the number, with its unit>, measured by `<measure command>`.
It is <base number> now. Guard: <what must not be traded away>.
This is a hard target and it can be reached.

Your copy: <path>. It is yours alone. Work only there. Commit there. Do not
push. Do not touch <measure files>; they define the goal.

Your route: <DIRECTION>. <Two or three sentences: the direction of attack
and why the baseline says there is something there. A direction, not a list
of steps.> If you find a very different way that the measure shows is
better and the guard holds, take it.
Not yours: <the one central lever of each sibling>.

Facts: <path to the facts file>. Each number there has its command. If one
does not reproduce, say so first.

Skills: use only <named skills, or none>.

Rules:
- A claim carries a before and an after from the measure. A change with no
  measured effect is not a result.
- Use `<fast measure>` in your own loop. Run the full measure at most <N>
  times. A third identical full run is a loop: stop and report.
- Limits: <wall-clock / runs / tokens>. At the limit, stop and report.
- Commit each change that helps as its own commit, with its number in the
  message. Revert what does not help.
- Keep the project's own tests passing, or say exactly which fail and why.

Report, at most <N> words:
1. Number: before, after, command.
2. What you changed (commits) and what each one gave.
3. What you tried that did not work, with its number.
4. What blocks more gain.
5. Optional: up to <3> research questions that would let you go further.
```

## Member, continuation

```
ROUTE-BRIEF: <name>/<member>/2

<Research packets attached, if requested.>
Continue toward the goal in your copy. The same rules and limits apply.

If you judge that no more gain is available on your route, stop. Then your
report must list your last attempts with their measurements and name what
blocks more.
```

## Attacker

```
STRESS-BRIEF: <name>/<attacker>

Your copy: <path>. It holds the combined result of several builders. You
built none of it. The builders report: <number, command>.

Your ground: <claims and checks | break and scale>. Your targets: <files,
checks, claims>. Another attacker has: <its targets>. Leave those.

Make it fail, or make its numbers untrue. For each finding give a
reproduction: the command and its output. Give a fix as a commit in your
copy where the fix is clear. Do not touch <measure files>.

Rank each finding: breaks (wrong result or damage), misleads (a number or a
check that says more than is true), gaps (not covered). Say how likely a
normal user is to meet it. A report of "nothing found" is acceptable; say
what you tried.

Limits: <wall-clock / runs / tokens>.
```

## Integrator (only on a conflict)

```
INTEGRATE-BRIEF: <name>

Copy: <path of combined>. `<integrate command>` stopped at <member> on
<files>. Policy: <for example: where two members add different things to
one file, keep both; where they change the same line, stop and report both
versions>.

Resolve only what the policy decides. Commit. Run `<measure command>` and
report the number. Do not choose between two designs; report them.
```

## Notes

- The first line is a literal marker. It makes dispatches easy to find in a
  transcript. It does not contain the word council, and the `Skills:` line
  names what a member may load, so that a member does not load this skill
  and read how the goal was set.
- State every base number in a brief with the command that produced it. A
  briefed number that does not reproduce costs every member a run.
- Do not copy a panelist's lens into a route. A route is a direction for a
  capable builder; it does not tell the builder what to ignore.
