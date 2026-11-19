---
name: panel-review
description: "Run a panel: three read-only reviewers dispatched at the same time, each given a different lens on the same subject; the orchestrator checks their facts and gives the owner one combined report. Use when the owner says \"run the panel\", \"panel this\", \"panel review\", \"confer with the panel\", \"have the panel look at this\", or asks for independent, adversarial or multi-lens review of a plan, design, prompt, document, problem or finished work, or wants new ways to think about a problem where step-by-step improvement has stopped paying. Also use when you are about to grade or review your own work on something expensive to get wrong: propose a panel. Not for a question one command answers, not for a single-reviewer check, and not for a council (agents that build, experiment or patch): a panelist only reads, thinks and reports."
---

# Panel review

A panel is three read-only reviewers, dispatched together, each committed to
a different lens. They look at the same subject and think about it
differently. You, the orchestrator, do not review. You commission, verify,
and **synthesise**.

Before you edit this skill, read `design/panel-review/PHILOSOPHY.md` in the
repository this skill came from. You do not need it to run
a panel.

## Why it exists

Two problems, one instrument. A panel reviews work, and it is also where a
new way of doing something is first imagined. When "do this, a little
better" has stopped paying, a panel is the place to look for a different
base to improve from.

**Models converge.** Ask three capable generalists the same question and you
get one answer three times, because they share the same training and the
same ruts. A rut limits which solutions are even considered. A lens is a
forced premise, strong enough to overcome that pull, so that each reviewer
enters the problem from a different side. A miner improves a mine by wanting
a better pickaxe. A chemist beside him thinks of explosives; an engineer
thinks of a drill. None of them alone would plan the mine well. Together
they put ideas on the table that no single one would reach.

**An author cannot see its own work.** An agent that reviews what it built
has no external anchor, so plausibility replaces verification. The first
panel was called because the owner wanted a grade that did not
come from the agent that did the work.

Hold these while you run one:

- **The product is a synthesis, not a consensus.** You are not looking for
  what the three agree on. You are looking for the best of each: the strong
  idea a lens found by pushing its premise hard, the practical or elegant
  detail it revealed, and sometimes a by-product that fails at its own
  purpose but solves another lens's problem. Agreement is only one input.
  A result that all three could sign is usually the average, and the average
  is what you would have had without a panel.
- **Diversity is the fuel.** If the three reports are similar, the synthesis
  cannot be better than its parts. Lens choice decides the value of the
  round before any reviewer starts.
- **A panelist is deliberately lopsided.** It gives up general balance to
  gain a specialist's reach. That makes it a source of ideas and findings,
  never an implementer and never a judge of the whole. Its recommendation
  can be wrong for the whole and still contain the most useful thing in the
  round.
- **Your reasoning must not leak in.** Anything that carries your hypothesis
  into a brief pulls all three back into your rut.
- **A panel is a front-loaded cost against future autonomy.** It belongs to
  design, setup, hard problems and trust decisions, not to a routine loop.
  When a panel keeps finding the same shape, build a check for that shape.

## When to run one, and when not

Run a panel when the owner asks. Without a request, you can propose one in a
single line, with the reason, and then you wait. Do not start one on your
own. Good reasons to propose:

- a change about to be built is expensive if it is wrong;
- a problem is stuck, or every solution on the table looks like the last one;
- a failure's class is not yet understood;
- finished work needs adversarial checking before it is trusted.

First ask whether one cheap command, or evidence already on disk, answers
the question. If it does, use that.

| The need | The instrument |
|---|---|
| A fact about the project | A command |
| One specific check ("is the capitalisation consistent") | One reviewer. The brief rules below help, but it is a review, not a panel |
| Different ways of thinking about one subject, then one synthesis | **A panel** |
| Building, experimenting, testing, patching toward a goal | A council. Not this skill |

**Panels think, councils do.** A council member is a capable generalist that
takes a direction or a component and works on it: it experiments, tests and
improves a real artefact. A panelist takes a premise and thinks. It never
edits, never works in a clone, never produces a patch. If the work needs any
of those, it is not a panel; say so and stop. A panel's synthesis can be the
input that tells a council what to build.

## Procedure

### 1. Choose three lenses, and make them far apart

A lens is a specialist with a premise it holds above everything else. All
three get the same subject and the same questions. They differ in what they
believe matters most, and so in how they attack the problem.

**Where the lenses come from.** The owner can name them, in a few words or
in detail, or can leave them to you and give only the goal or the hoped-for
result. If the owner's direction is very short ("cost, speed, robustness"),
expand each into a premise with enough room to think from, and tell the
owner how you expanded it. If the choice is yours, derive the lenses from
the goal.

**Every lens serves the panel's goal.** A premise is an extreme way to reach
the goal, never a replacement for it. A cost lens on a software project
that concludes "stop developing" has met its premise and failed the panel.
State the goal and what is not negotiable in the shared part of the brief,
so that each lens pushes hard inside those bounds.

The goal line is where your own framing most easily leaks in. Write it as
an outcome and its limits: what the owner wants to be true, and what must
not be given up. Put no method, no mechanism and no candidate answer in
it. If the owner's request contains a proposed solution, that solution is a
claim for the panel to test, not part of the goal. The owner does not have
to word the goal; you word it, briefly, from what they asked. Apply the same test to
your own plan for the panel: a lens set that is extreme but cannot produce
anything usable toward the goal is badly chosen.

Choose for distance, not coverage:

- For each pair, ask: would these two propose different solutions, or only
  rank the same solution differently? If only the ranking differs, replace
  one. Remove any lens that overlaps another.
- Check it on paper. Write one line per lens: the kind of answer this lens
  will most likely push for. Every reviewer starts by exploring, so do not
  predict its first step; predict its headline. If two headlines match,
  redraw a lens.
- Include a lens you expect to be "wrong" for the final answer if it attacks
  the problem from a side the others will not. Do not tell it so.
- Fit the lenses to the subject. Do not reuse a set by habit.

Simple examples: one lens for cost, one for run-time speed, one for
robustness and future change. Sets that have worked for systems and process
reviews: detection and signal fidelity ("this fires too late, or under the
wrong name"), class generalisation ("you fixed one of three; here are the
others"), cost and portability ("this costs more than the defect it
prevents"). Others used: reliability, maintainability, cold-start
comprehension, evidence scepticism, questioning assumptions.

Three is the working number. Keep the count odd, so that a coarse
disagreement on an assumption has a tiebreak. Use more (five) only at the
owner's word, in waves of at most three, and hold every added lens to the
same distance test.

### 2. Prepare evidence, not conclusions

Give reviewers paths, command output and figures. Keep your hypothesis, your
preferred answer and any candidate cause out of the brief and out of the
lens text. A hypothesis written into a brief has been reproduced by all
three reviewers. An "independent" finding was once traced to a cause named
in one reviewer's lens paragraph.

Everything you write for a reviewer carries your view: the goal line, the
lens text, the questions, and which facts the pack counts. Test each one
before dispatch:

- A lens paragraph says what the specialist values. It names nothing the
  specialist will find.
- No two lens paragraphs make the same claim in different words.
- A question names an area. It lists no candidate answers.
- The pack counts what a reviewer of any lens would want counted, and not
  only the facts that point where you expect.

When the subject is your own conclusion, present it as a claim to test with
its evidence, and hide work that would anchor the reviewer. For a large
subject, write one evidence pack (figures and paths only) and point all
three briefs at it.

**Check the instrument before dispatch.** Evidence often reaches a reviewer
through a stand-in for the real thing: a test page for the device, a sandbox
for the live system, a score for a listener. Three reviewers who share a faulty
instrument return its fault as three findings, and their agreement then
looks like proof.

- Name each stand-in in the pack.
- Where one cheap comparison with the real thing exists, run it now: one
  reading on the device, one photograph beside the screenshot, one owner
  judgement beside the score.
- Where none exists, say in the pack what was not measured on the real
  thing. A reviewer that knows the gap can aim at it.

### 3. Write the briefs

One brief per lens, from `references/brief-template.md`. The body is the
same; only the lens paragraph differs. Each brief:

1. States read-only plainly: change nothing, create nothing, commit nothing.
2. Commits the reviewer to its lens. Tell it to push the premise as far as
   the evidence allows and not to balance it against other concerns; other
   reviewers carry those. A lens that moderates itself returns the generic
   answer.
3. Names where to start reading, and lets the reviewer go wider inside the
   project when its lens needs it. It says where it went. A lens often
   finds its best material somewhere you did not think to name.
4. Names the skills the reviewer may load. It must not load this one.
5. Asks numbered questions. Each names an area and lists no candidate
   answers.
6. Separates facts from ideas. A fact carries its evidence and a confidence
   score. An idea can be speculative, if it is labelled as one; for an idea
   the reviewer gives the payoff if it works, and separately the odds. A
   single confidence number on everything rewards the safe answer and
   buries the long shot, and the long shot is what you are paying for.
7. Asks for an approach, not only defects: what this lens would do, and the
   one idea it expects everyone else to overlook. A reviewer can report
   that it found no defects. It cannot skip these sections.
8. Asks what its approach costs elsewhere. You need this to temper it.
9. Says that disagreement with the brief is a valid finding.
10. Gives a report shape with a free last section and a generous length,
    so that an idea that fits no heading still has a place.

Do not tell a reviewer that its lens may be the weak one, and do not ask it
to seek agreement. Write the brief so that a fresh specialist understands it
fully and cannot fall into your earlier reasoning.

### 4. Dispatch all three in one message

As you dispatch, post this block in chat. The round is won or lost at lens
choice, and the owner is the only outside eye on that choice before the
round is spent. The block shows your work to that eye.

```
Goal: <the goal line, word for word as the briefs carry it>
Lenses:
- <lens>: <its premise in one line>. Expected headline: <one line>
- <lens>: <its premise in one line>. Expected headline: <one line>
- <lens>: <its premise in one line>. Expected headline: <one line>
Model and effort: <model>, <effort>
Expected cost: <tokens or money>
```

The expected headlines are the ones from your paper check in step 1.
Reviewers do not see this block. Do not wait for an answer; the owner asked
for the panel and can stop it.

- **Together, in one message.** A reviewer that starts after another has
  reported is anchored to it.
- **Sonnet, named on every dispatch.** An unnamed model inherits yours and
  the round costs several times what it needed. A stronger model is used
  only when the owner asks for it; do not raise the model yourself.
- **Effort high by default.** You can raise effort to max for a round when
  the subject needs argument that must be built, not looked up. Say that you
  did, and why, in your report.
- **A read-only agent type.** Use `panel-reviewer` if it is in your list of
  agent types. If it is not, use a built-in type that has no edit or write
  tool; the brief template carries every instruction the reviewer needs, so
  the round does not depend on the custom type. If no read-only type
  exists, use a general agent and rely on the read-only line. A reviewer
  keeps its shell so that it can run checks.
  `python scripts/install_reviewer.py` (in this skill's directory) copies
  the `panel-reviewer` definition into `~/.claude/agents`. A machine's setup
  script can run it so the type exists before a session starts. If you run
  it during a session, use the fallback for this round; do not assume the
  new type has loaded.

### 5. Verify facts before you use them

Reviewers are confidently wrong in both directions. Recorded cases: a
duplicate line that a grep refuted; two checks called redundant that covered
disjoint cases; a count low by more than half; three reviewers who agreed a
file was absent because all three searched the same two directories.
Agreement on a method is not agreement on a fact.

Run the command for each factual claim you intend to build on. Mark what you
could not check as unverified. Say plainly when a reviewer was right and you
were not. Verification applies to facts. Do not discard an idea because its
lens also made a factual error.

### 6. Synthesise

This is your work, and it needs your general judgement, which the lenses
gave up. Go through the three reports and:

- **Take the strongest element of each lens**, even where its overall
  recommendation is wrong for the whole.
- **Temper the unreasonable.** Use each lens's stated costs, and the other
  lenses' objections, to cut an idea down to the part that survives.
- **Elevate what was revealed.** A practical detail or an elegant mechanism
  that one lens found is often worth more than its headline.
- **Look for transfer.** Ask of each idea, including the failed ones: does
  this solve a problem that a different lens described? This is where a
  panel pays most, and no single reviewer can see it.
- **Combine** into one result that none of the three proposed.

**Guard against your own rut.** The reviewers were pushed out of the common
answer; you were not, and tempering is where an odd, valuable idea is most
easily lost.

- Before you leave an idea out as unreasonable, write what would have to be
  true for it to work. If that is cheap to check, check it.
- Name the strangest idea you kept and the strangest you left out.
- Judge by content. A long report is not a heavy one, and the most useful
  thing in a round can be one sentence in the free section.

Do not average, and do not reduce the result to the overlap. Where two
lenses disagree on a fact, settle it with a command. Where they disagree on
what matters, that tension is material: resolve it in the synthesis if you
can, and if you cannot, give it to the owner as a choice with both positions
and your recommendation.

If the three reports are close to each other, say so. The lenses were too
similar, and the round found less than it should. Do not present overlap as
confirmation.

### 7. A cross-pollination round, when a discovery earns it

A second round exists for one purpose: a strong premise or a proved
discovery can cause new ideas in the lenses once they see it. It is not a
vote and not a push to agree.

**When.** At the owner's word. Or on your own decision, if both are true:
a discovery exists that could change how a lens attacks the problem, and a
cheap check proved it. One extra round. Say that you ran it, and why.

- **The discovery can come from anywhere:** a lens, your own verification
  in step 5, or the owner. A proved fact is evidence, not your opinion. A
  read-only reviewer often cannot prove its own discovery; you can.
- **It must open something.** Evidence that only removes a finding does not
  open a round: correct the finding in step 5 and say so.
- **Let the reports decide whether it could change an approach.** Each
  report says what would change its mind and what it found missing. A
  discovery that meets one of those conditions qualifies. One that meets
  none goes to the owner as a question.
- If the proof is not cheap, describe the discovery to the owner and ask.

**What each seat does.** Decide per seat, and keep the count odd.

- A seat that has a verified discovery from another lens to receive
  continues: same reviewer, same lens.
- A seat with nothing new to receive (often the discoverer itself, when the
  others found nothing comparable) has no reason to repeat its work. Either
  replace it with a fresh reviewer under a new lens whose premise starts
  from the discovery, or keep it and give it an adversarial task: attack the
  other two round-one reports and find where they crack.
- When the discovery came from your verification or from the owner, every
  seat has something new to receive, and all three continue.

**What it carries.**

- Give each continuing reviewer the other two reports verbatim, and the
  proof of the discovery as command and output. Do not send your synthesis,
  your summary or your reading of the proof; that would leak your reasoning.
- Ask each one, still inside its own lens: what does this change in your
  approach; what can you build from their ideas that they did not; which of
  their claims are wrong on the facts, with evidence.
- A reviewer must hold its lens. One that drops its premise to agree has
  stopped being useful.

Then synthesise again from every report of both rounds.

In the one recorded case every position that moved did so
because another reviewer supplied evidence, and the round added about 60% to
the cost. Disputes about what matters did not move, and should not be
expected to.

### 8. Report and save

Report the synthesis to the owner in chat, as a numbered list they can
answer by number:

1. **Synthesis**: the combined result, and which lens each part came from.
2. **Verified**: the facts it stands on, each with its command; anything
   unverified, marked.
3. **Left out**: ideas you did not use, why, and what would have to be true
   for each to work. Mark the strangest one you kept and the strangest you
   left out. A rejected idea with its reason can be the right one later.
4. **Open choices**: tensions you could not resolve; both positions; your
   recommendation on its own line.
5. **Next**: actions, cheapest first.
6. **Cost**: tokens or money, model and effort used.
7. **If it should be built**: only when the synthesis is something that can
   be built and measured. Propose one goal number, the command that would
   measure it, and two or three different routes to it. The routes are
   candidates: no baseline exists yet, and a council draws its own routes
   from one. Write that beside them, and in any ticket made from them. This
   is what a council (`council-testing`) starts from. A council takes the synthesis,
   never one reviewer's report. If the owner said "council after the panel"
   in advance, go on to it.

Save the whole round, so that a later reader can check it without you:

- the evidence pack, with any correction made after dispatch marked at its
  top;
- the three briefs as sent. They are the only proof that your reasoning
  stayed out;
- the three reports verbatim;
- the synthesis with all seven sections above;
- short process notes: what in this skill helped, what was missing or
  wasteful, and what you would change. A later review of this skill reads
  them.

Use the place and form the project already uses for research or review
records. That form can add headings. It cannot drop one of the seven
sections. If the project has no such place, make a panel results directory
with one folder per panel, named for the subject, and title each report by
subject and lens.

## Later rounds

To re-grade work that changed because of a panel, use **fresh reviewers**
with the same brief and rubric; a reviewer that grades its own suggested
edit is not independent, and the same brief makes scores compare. Stop when
a round names only new small items and the scores do not move.

Graded rubrics, research-then-resume, and disjoint panels at once are in
`references/variants.md`. The incident behind each rule is in
`references/origins.md`.
