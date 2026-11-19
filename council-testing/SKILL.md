---
name: council-testing
description: "Run a council: several capable agents, each in its own private copy of the project, each taking a different route toward one hard measured goal by building, running and measuring; the orchestrator stacks the working results, measures again, and has attackers try to break the combined result. Use when the owner says \"run a council\", \"council this\", \"put a council on it\", \"council after the panel\", or wants competing experimental approaches to one measurable target (speed, cost, size, pass rate, error count, accuracy). Also use to propose a council when a panel has produced an actionable direction, or when small step-by-step improvement has stopped paying. Not for thinking or review without building (that is a panel), not for an edit, a survey or a reading (one agent), and not for a subject where nothing can be run or measured."
---

# Council testing

A council is several capable agents, each in a private copy of the project,
each given a different route to the same goal. They build, run and measure.
You, the orchestrator, set it up, stack the working results, measure again,
send attackers at the combined result, and report.

Before you edit this skill, read `design/council-testing/PHILOSOPHY.md` in the
repository this skill came from. You do not need it to run
a council.

## What it is for

A council finds out what is possible by doing it. Use it for two kinds of
work:

- **A hard optimisation**, where the answer is a better version of a real
  thing and a command can say how much better.
- **A leap.** The usual loop of "do this, a little better" has stopped
  paying, and you or the owner believe a different way of doing the thing
  exists. A council tries several different ways at once, so that later
  small steps start from a better base.

Three ideas hold it together:

- **One goal, several routes.** Every member owns the same number. They
  differ in how they go after it. Members that only hold different chores
  are ordinary subagents at a higher price.
- **Evidence is a measurement.** A claim with no before and after number
  from the measure is not a result.
- **Builders do not certify their own work.** Attackers who built none of
  it try to break it before anyone trusts it.

| The need | The instrument |
|---|---|
| A fact about the project | A command |
| An edit, a survey, a reading | One agent |
| Different ways of thinking about a subject, then a synthesis | A panel (`panel-review`) |
| Different ways of building toward one measured goal | **A council** |

A council can start from anything: the owner's idea, a measurement, a
failure, research, a panel. When it starts from a panel, the panel reaches
the council through its **synthesis** only. One panelist's report is bent on
purpose and must not become a builder's route.

## Who starts it

The owner. A council costs real money and time.

- Without a request, propose one in a line or two: the goal number, the
  routes, the expected cost, and why one agent will not do. Say also if
  the measure exists yet, what was already tried on the number, and how
  many agents will share the machine while the council runs. Then wait. Be
  ready to propose one when a panel has just given an actionable result.
- If the owner said in advance "council after the panel", go from the
  synthesis to dispatch without a stop. Show the goal, the routes, the
  measure, the expected cost and the number of agents that will share the
  machine in chat as you start.

## Procedure

### 1. Fix the goal and the measure

**The goal** is one number, set high: beyond what the first good idea will
reach. State it with a guard clause that says what must not be traded away
("with every case the suite checks still checked"). A guard is what stops a
number from being won by cheating.

**The measure** is one command that prints the number on its last line. It
is fixed before any member starts, it is the same for everyone, and members
cannot change it. Keep it as fast as it can be and still be true: every
member runs it many times, and slow measures cost more than anything else in
a council. If the full measure is slow, give members a fast partial measure
for their own loop and keep the full one for integration.

When no direct number exists, read `references/measures.md` and choose a
proxy number, a fixed case set, blind graders, or a replay of history. The
less direct the measure, the more you tell the owner before you start: what
will actually be measured, why it stands for the goal, and how it can
mislead. If none of the four can be defined, this is not a council. Say so,
and suggest a panel.

### 2. Run the baseline, alone

Run the measure on the unchanged project with nothing else running. Then
find where the number comes from: which parts, steps or cases make up most
of it. One council once chased a few files that held a small part of the total; no
effort there could have reached its goal.

Write a facts file: each base number with the command that produced it.
Facts only; no ranking, no candidate change, no estimate of what is
possible. Members get this file.

Use the breakdown to draw routes where the number actually is. Do not use
it to lower the goal.

Then compare the largest parts of the number with the owner's recorded
decisions: the spec, the ticket, the project's decision record. A part
that a recorded decision governs is not a defect, and work on it undoes
the decision. Take that part out of the measure now, write the source of
the decision in the facts file, and run the baseline again. This corrects
the measure. It does not move the goal. In the dispatch message, list the
large parts for which you found no recorded decision.

### 3. Draw the routes

A route is a wide lane: a direction of attack with real room to experiment
inside it. Three members is the default. Use two to five by the size of the
subject, and say the count and the expected cost before you dispatch. More
than five needs the owner's word.

- **Different enough.** Ask of every pair: could these two hand back the
  same change? If so, redraw. Duplicate work is the main waste in a
  council, and you do not need overlap for safety, because stacking the
  results is what makes sure no improvement is missed.
- **Wide enough.** A route names a direction ("run less", "run faster",
  "run at a better time"), not a list of steps. A member may leave the
  expected method of its lane for a very different one if the measure shows
  it is better and the guard holds.
- **Fence only the neighbour's main lever.** Each brief says what belongs
  to a sibling. Name the one central thing, never a whole area.
- **Split by component only when components are small.** If a component is
  large enough that two routes could attack it differently, keep it whole
  and give it routes. Do not give a member something too small to explore.
- **Routes from elsewhere are candidates.** Routes, a member count or an
  attack list that arrive in a ticket, a plan or a hand-off were written
  before the baseline. Test them as you test your own: with the pair
  question above, and against the breakdown from step 2. Redraw those that
  fail, and say in the dispatch message what you changed and why. Where a
  route came from gives it no authority over the measure.

Members are capable generalists. A route aims a member; it does not bend
its judgement. Do not give a member a lens that tells it to discount other
concerns. What it returns must work as a whole.

### 4. Create the copies and write the briefs

```
python <skill>/scripts/council.py new NAME --members a,b,c \
    --measure "<command>" --protect "<measure script>" --protect "<its cases>"
```

This makes one private worktree per member and one named `combined`, beside
the project. A project that is not in git is copied and committed first.

`--protect` names the files that define the measure: its script, its
checks, its cases, its settings. Give the flag once for each glob. The
script then does two things with those files:

- It refuses to integrate a member that changed them.
- At each measurement it compares them with the base, in the copy and in
  the project checkout, and prints `MEASURE CHANGED` with the files that
  differ. That number is not from the measure the council started with. Do
  not put it in a table beside numbers that are, and do not correct it by
  hand. If the measure must change during a council, tell the owner, then
  measure the base and every copy with the new command:
  `council.py measure NAME --in all --with "<new command>"`.

The script sees only the files you name. A measure file that is not under
`--protect` can change with no report.

Write one brief per member from `references/brief-templates.md`. The shared
body carries the goal with its guard, the measure, the facts file, the
rules and the limits. The route paragraph differs.

**What a member must believe.** The goal is hard and it can be reached. Do
not write that it is unlikely, that it was set high on purpose, that
falling short is acceptable, or anything about how the council is designed.
Do not name this skill in a brief, and give each brief a `Skills:` line that
lists what the member may load, so that it does not load this one. Do not
pretend the goal is easy. A
member that thinks the target is theatre stops at the first respectable
gain; a member that thinks it is real keeps looking where the obvious ideas
end.

**Limits.** Set them before dispatch, in the unit that fits this project:
full-measure runs per member, wall-clock, or tokens. Projects differ. One
has a ten-second measure and one a ten-minute one; one is mostly tool use
and one mostly reasoning. Choose limits that would catch a loop and would
not stop good work, and tell the owner what you chose and the expected
cost. A limit here is a loop detector. Hard problems sometimes need a
member to hit the wall many times; they never need it to repeat the same
run a third time.

### 5. Round one: members work alone

Dispatch all members in one message. Each is a general agent with write
tools, model `opus`, effort `medium`, named on the dispatch. A higher or
lower setting is the owner's choice.

Members do not see each other's work in this round. Each commits in its own
copy and reports: measured before and after, what it tried that failed,
what blocks further gain.

After its first report a member may request a small number of research
packets (facts and sources, produced by you, no ranking), and then
continues once. A member may also stop: if it has honestly run out of
gain, it says so, and its report must then list its last attempts with
their measurements and name what blocks more. A stop with no such evidence
is sent back.

If a member reaches the limit you set, stop it and report that. Do not
extend a limit silently.

When the first member reports, run `status`. Files that more than one
member changed show early if the routes will stack or are alternatives
(step 6).

### 6. Integrate by stacking

```
python <skill>/scripts/council.py status NAME
python <skill>/scripts/council.py integrate NAME --order a,b,c [--each]
```

`status` shows what each member changed and which files more than one
member touched. `integrate` applies each member's commits to `combined` in
order, stops cleanly at a conflict, and runs the measure. `--each` measures
after every member, which shows what each route adds on top of the others;
use it when the measure is fast.

Gains from different routes do not simply add, and they sometimes collide.
The combined number is the result; the members' own numbers are not.

Each measurement the script takes records the commit, the machine load and
the number of cores. `MACHINE LOADED` means the load was more than the
cores when the measurement started: a time, or a count that depends on a
timeout, is not reliable from that run. Measure again on a quiet machine
before you report the number.

You are not bound to take a route whole. Keep it, drop it, or take only the
part that pays. A member can be right on the measure and wrong for reasons
it could not know; that is your call, or the owner's.

When `status` shows that the members changed the same files, the routes
are alternatives: you will take one and not stack them. A pick between
alternatives that you make here is provisional. The stress round can
remove the part of the number that the pick stands on (step 7).

On a conflict, dispatch one integrator at `sonnet` to resolve it under a
policy you state (for example "where two members add different things to
one file, keep both"). A choice between two valid designs is not the
integrator's and not yours. Put it to the owner.

### 7. The stress round

Nothing a council built is done until attackers have tried to break it.
Builders test what they meant to build, so their checks pass.

```
python <skill>/scripts/council.py add NAME attack-claims
python <skill>/scripts/council.py add NAME attack-break
```

Two attackers by default, each in its own copy of `combined`, at `opus`,
effort `medium`:

- **Claims and checks**: do the reported numbers hold when measured another
  way, and can any new check pass while the thing it guards is broken?
- **Break and scale**: inputs, sizes, orderings and environments the
  builders did not try.

Give each attacker its own targets and name the other's, so they do not
find the same defect twice. Add a third only for a large or risky change,
and more only at the owner's word. An attacker returns a reproduction for
each finding, and a fix where one is clear.

Sort the findings with sense:

- **Fix**: anything about security or data loss; anything that makes a
  reported number or a check untrue; any break a normal user would meet.
- **Record and leave**: a rare, harmless edge case with no security side.
  List these for the owner. Do not spend a council's money on a stray
  pixel.

Integrate the fixes and measure again. `status` and `close` print
`NO FINAL NUMBER` while `combined` has a commit that was not measured. If
the fixes go to later work and not into `combined`, the report says that
the council has no final number.

**Then look at the routes again.** If the stress round showed that part of
a number was not true, measure every route without that part:

```
python <skill>/scripts/council.py measure NAME --in all \
    --with "<the measure without the disproved part>" --label corrected
```

A pick between routes stands only if the corrected numbers still separate
them. If they do not, what remains is a choice between valid designs, and
that choice is the owner's.

### 8. Report and save

Report to the owner in chat, as a numbered list:

1. **Result**: before and after on the measure, with the command; the goal;
   the distance that remains and what blocks it.
2. **Routes**: each route's number as measured and, where the stress round
   disproved part of a number, as corrected; what each added in the stack;
   what you kept, dropped or took in part, and why.
3. **Stress round**: what broke, what was fixed, what was recorded and left.
4. **How far to trust the number**: required whenever the measure was a
   proxy, a case set, graders or a replay.
5. **Open choices**: each with the options and your recommendation on its
   own line.
6. **Cost**: tokens or money, wall time, model and effort, and any limit
   that was reached.

A goal that was not reached is a normal outcome. Report the distance
plainly, without apology and without calling the council a failure: what
remains and why is part of what the owner paid for.

The result stays on the branch `council/NAME/combined`. Do not merge it
into the owner's branch; that is the owner's decision. Save the reports and
the facts file the way the project keeps records; if it has no way, make a
council results directory with one folder per council, named for the
subject. `council.py close NAME` removes the copies and keeps the branches.

Incidents behind these rules: `references/origins.md`.
