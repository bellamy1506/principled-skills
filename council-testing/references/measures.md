# Measures for subjects that are hard to run or measure

A council needs a number that every member can obtain the same way. When no
direct number exists, use one of these. In every case: fix the measure
before any member starts, give every member the same one, and protect its
files from members (`--protect`).

The less direct the measure, the more the owner must know before the
council starts. Tell the owner, in chat: what will actually be measured,
why it stands for the real goal, and the pitfalls listed below.

Keep every measure as fast as it can be and still be true. A measure runs
many times per member. Prefer a small fixed sample that runs in seconds to
a complete one that runs in minutes, and keep the complete one for
integration.

## A. Proxy number

A countable stand-in for a goal that cannot be counted directly.

- Example: the number of questions, from a fixed list, that a help page
  does not answer.
- Tell the owner: the proxy, and one sentence on why it tracks the goal.
- Pitfall: members improve the proxy and not the goal. The guard clause
  must name what the proxy does not see.

## B. Fixed case set

Pass or fail cases written before round one. The goal is "N of M pass".

- Example: forty awkward inputs a parser must handle.
- Tell the owner: who wrote the cases and from what.
- Pitfall: members fit the cases. Hold some cases back; attackers run the
  held-back set in the stress round.

## C. Blind graders

Fresh read-only reviewers score each result against one rubric. They do not
know which member produced which result.

- Use for prompts, documents and designs.
- Use a cheap model, an odd number of graders, the same rubric and brief
  each time, and fresh graders each round.
- Tell the owner: the rubric, the number of graders, and the spread between
  graders on the baseline. A difference smaller than that spread is noise.
- Pitfall: graders reward what reads well. Set the goal as a clear margin
  over the baseline, and have an attacker test the winning result against
  real use.

## D. Replay

Run each result against recorded history.

- Example: would this rule have caught the last fifty real incidents?
- Tell the owner: the period replayed and what was left out.
- Pitfall: a result tuned on the same history it is scored on. Split the
  history; members see one part, the final score uses the other.

## If none fits

There is nothing to build toward. Say so. A panel can still think about
the subject, and may find something that can be measured.
