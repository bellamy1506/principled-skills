# principled-skills

Agent skills built from a stated purpose, with the reasoning kept beside
them. They run in Claude Code and in other agents that load `SKILL.md`
skills.

| Skill | What it does |
|---|---|
| [`panel-review`](panel-review/SKILL.md) | Three read-only reviewers, each made to think from a different premise, and one synthesis that is better than any of them. For review, and for finding a new approach when small steps have stopped paying. |
| [`council-testing`](council-testing/SKILL.md) | Several builders in private copies of a project, each on a different route to one measured goal. The working results are stacked, measured again, and attacked. |

A panel thinks differently. A council does differently. A panel's synthesis
is one good starting point for a council.

## Install

Copy the skill folders you want into your skills directory. Copy only
those folders.

```bash
cp -r panel-review council-testing ~/.claude/skills/
```

Optional, for `panel-review`: install the read-only reviewer agent type, so
that it exists before a session starts.

```bash
python ~/.claude/skills/panel-review/scripts/install_reviewer.py
```

`council-testing` needs git and Python 3. `panel-review` needs nothing.

Then ask in plain words: "panel this design", "run a council on the test
suite, goal under 60 seconds".

## Keep `design/` away from the agents

Both skills depend on what their participants believe. A reviewer that
learns how its report will be used stops pushing its premise. A builder
that learns how its goal was set stops at the first respectable gain.

So this repository has two parts:

- `panel-review/` and `council-testing/` are what an agent loads. They say
  nothing to a participant about the design.
- `design/` is for people and for whoever changes a skill. It says the
  design openly.

Do not copy `design/` into a skills directory. Do not keep a clone of this
repository inside a project that a panel or a council will work on. Do not
name a file from `design/` in a brief. Each skill's brief templates carry a
`Skills:` line for the same reason.

## What is in `design/`

| File | For |
|---|---|
| [`design/PHILOSOPHY.md`](design/PHILOSOPHY.md) | What a skill is underneath: thirteen questions for making one |
| [`design/panel-review/README.md`](design/panel-review/README.md) | The panel, explained for people |
| [`design/panel-review/PHILOSOPHY.md`](design/panel-review/PHILOSOPHY.md) | Why the panel is shaped as it is; tests for a change |
| [`design/council-testing/README.md`](design/council-testing/README.md) | The council, explained for people |
| [`design/council-testing/PHILOSOPHY.md`](design/council-testing/PHILOSOPHY.md) | Why the council is shaped as it is; tests for a change |
| [`design/council-testing/test_council.py`](design/council-testing/test_council.py) | Checks of the council script in a scratch repository |

Each skill's `references/origins.md` gives the reason behind each rule.

## Optional companion

The panel's brief template can name a skill for controlled technical
English, so that reports are hard to misread. One such skill is
[asd-ste100-skill](https://github.com/danyuchn/asd-ste100-skill). It is not
needed.

## Licence

MIT. See [`LICENSE`](LICENSE).
