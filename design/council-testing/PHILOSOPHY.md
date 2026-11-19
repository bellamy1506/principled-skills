# The philosophy of the council

For whoever changes this skill. It is not loaded when the skill runs. Read
it before you edit SKILL.md or a brief template, so that a change made in a
fresh context does not pull the skill off its purpose.

This is a distillate of the session that wrote the skill, of the councils
run before it, and of the first field run after it. The reason behind
each rule is in the skill's `references/origins.md`. The script's checks
are in `test_council.py`.
The companion skill is `panel-review`; its own PHILOSOPHY.md is the other
half of this picture.

## The one idea

A council finds out what is possible by attempting it. Several capable
builders, each alone with a real copy of the thing, each on a different
road, all trying to reach a mark that looks out of reach. What comes back is
not opinion. It is working change and a number.

## Why the mark is out of reach

A comfortable target is met by the first good idea, and then the work
stops. Most of what is worth finding lies past that point. A mark set
beyond what seems possible keeps a capable builder searching after the
obvious is used up, and that is where a different way of doing the thing,
not a better version of the same way, gets found. The impossible is only
impossible until it is not; a great deal of progress, in people and in
models, came from someone refusing a limit that everyone assumed.

Two things follow, and they pull against each other.

- **The builder must believe the mark can be reached.** Not that it is
  easy. That it is real. A builder who learns the target is a device, or
  that falling short is expected, will stop at the first respectable gain,
  and the council becomes an expensive way to get an ordinary result. So
  the design is hidden from the members. Even this skill's public
  description says only "hard", because a member can see it.
- **The orchestrator must not need the mark to be reached.** The distance
  that remains, and what blocks it, is part of the product. A council that
  gained forty percent toward an eighty percent mark has not failed.

## Why several roads

Nobody knows in advance which road pays. Running several at once finds out,
and the best parts of several can be stacked into something none reached
alone.

Roads must differ, or the money buys the same work twice. They must also be
wide, or there is no room for the leap the council exists for. A road is a
direction, with freedom inside it, including the freedom to leave the
expected method when the number says so. Splitting by component is right
only when components are small; a large component deserves several roads,
and a tiny one deserves none.

## Who the builders are

Whole craftsmen. A panelist is bent on purpose, gives up balance for reach,
and is unsafe to build with. A council member is aimed, not bent: it is
told where to dig and keeps all of its judgement while digging, because
what it hands back must work as a whole.

This is the line between the two skills. A panel thinks differently. A
council does differently. A panel's product is a synthesis of ideas made by
the orchestrator; a council's product is a stack of working changes,
measured. A council can start from anything. A panel is one good
place to start from, and a panel may feed a council only through its
synthesis. One lens's report carries its bend with it.

## Why the result is attacked

Builders test what they meant to build, so their tests pass. The first
adversarial round found thirty problems behind a green suite. So the work
is not done until someone who built none of it has tried to break it and
to make its numbers untrue.

But the attack serves the work, not the reverse. Security, lost data, and
false numbers are always fixed. A harmless once-in-a-decade edge case is
written down and left. Choosing to run a council is the owner's spending
decision; adding cost inside it to stop a stray pixel is not.

## The balance to hold: tight here, loose there

This skill is easy to ruin from either side.

**Keep tight** (loosen these and you get cheating or waste):

- the measure: fixed first, the same for all, not editable by members;
- the guard clause on the goal;
- every claim carries a before and after;
- a stop needs evidence of the last attempts and what blocks more;
- routes do not duplicate;
- the stress round always runs;
- only the owner starts a council; policy choices go to the owner.

**Keep loose** (tighten these and you kill the leap):

- how a member works inside its road;
- whether a member leaves the expected method for a better one;
- what is fenced off as a sibling's (one lever, never an area);
- limits: a loop detector in whatever unit fits the project, never a cap on
  honest hard work;
- what the orchestrator keeps: a whole road, none of it, or one piece.

Rules here are backed by a check where one exists. The script refuses a
member that changed the measure, stops cleanly on a conflict, and reports
a measure file that changed anywhere, a loaded machine, and a combined
copy with no measurement of its last commit. `test_council.py` in this
folder exercises them. Where a rule is only
judgement, the reason is given so the judgement can be made well. Projects
differ too much for one set of numbers.

## Analogies to keep

**Race teams.** Three crews, three identical copies of the car, one lap
time nobody has driven. One crew takes the engine, one the air, one the
tyres. Nobody argues; the stopwatch decides. The best parts go on one car
and it is timed again, because a faster engine can be undone by the new
wing. Then people who built none of it try to crash it. The crews are never
told the lap time was picked to be out of reach.

**The mine.** The panel was a miner, a chemist and an engineer talking, and
a failed compound that turned out to crack bedrock. The council is what
comes next: several competent crews, each with its own test shaft, each
trying a different way to turn that into metres a day, then an inspector
trying to bring the roof down before anyone is sent in.

**The four-minute mile.** Runners treated it as a wall until one man ran
through it; then many did. The wall was partly in the belief. A council
member is put on the track as someone who has been told the time is hard
and can be run.

## How this skill can go wrong

- **Members become task-holders.** Different chores, no shared number. This
  happened once and the owner called the result unrepresentative.
- **Members are given lenses.** Then they are panelists with write access.
- **The brief leaks the design.** Any sentence that tells a member the goal
  is unlikely, deliberate or optional. A member that loads this skill reads
  the design too; the brief's marker and `Skills:` line exist to prevent
  that.
- **The baseline breakdown is used to lower the goal.** It is for drawing
  roads where the number is, nothing more.
- **Reports are blended.** Results are stacked and measured, not averaged
  from prose.
- **The stress round grows.** More attackers on shared ground find the same
  defect twice.
- **The measure moves under the numbers.** Not by a member: by the
  orchestrator, or by other work on the project. The script
  now reports it.
- **The measure counts a state the owner chose.** Work toward the number
  then undoes a decision.
- **A plan made before the baseline is treated as authority.** Routes, a
  member count and an attack list arrived in a ticket and were kept
  though two routes overlapped. Tickets will go on naming
  routes; the skill tests them, and does not ask tickets to change.
- **The pick is made before the attack and not opened again.** The gap
  between routes was the part of the number that was not true.
- **A council is put on work that is undone, not hard.** The number was
  far only because nothing had been tried. No rule: it is
  the owner's spending decision. The proposal now says what was tried.
- **A rule document is read as intent.** The project councils came from
  wrote rules for its own tools and costs. When a record and this file
  disagree about purpose, this file is the purpose.

## Tests for a proposed change

1. Could a member learn from it that the goal is not meant to be reached?
   Then it is wrong.
2. Does it let anything but a measurement count as a result? Wrong.
3. Does it make two members more likely to do the same work? Wrong.
4. Does it narrow what a member may try inside its road? Probably wrong.
5. Does it let a member touch the measure, or weaken the guard? Wrong.
6. Does it tell a member what to ignore? That is a panel lens.
7. Does it let the council start, grow or merge its result without the
   owner? Wrong.
8. Does it add cost to prevent something rare and harmless? Leave it out.
9. Does it add a rule with no incident behind it and no check? Leave it
   out, or give the reason so judgement can apply.
