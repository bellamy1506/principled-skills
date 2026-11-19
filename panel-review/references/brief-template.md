# Panel brief template

Fill the angle brackets. Keep the body identical across the three briefs;
change only the first line and the lens paragraph. Aim for 400 to 700 words.
Put long evidence in a file and name the file.

A brief never says that a lens may be the weak one, that a report will be
cut down or combined, or how the panel is designed. It never names the
panel skill.

```
PANEL-BRIEF: <lens name>

You are one reviewer on a panel. Each reviewer has a different lens. You
will not see the other reports.

READ-ONLY. Do not change, create or delete a file. Do not commit. You can
run commands that read or check. Return a report only.

Subject: <what is under review, in one or two sentences, no verdict>

Goal: <the outcome the owner wants, and what must not be given up. No
method, no mechanism, no candidate answer.> Every recommendation must serve
this goal.

Your lens: <LENS>. <Two or three sentences: the premise this specialist
holds above everything else, and what it treats as secondary. Name no
candidate cause and no expected answer.>
Push this premise as far as the evidence allows. Do not balance it against
other concerns; other reviewers carry those. State your bias in the first
line of your report.

Start with these. Go wider inside the project when your lens needs it, and
say where you went:
- <path or evidence pack>
- <path>

Skills: use only <named skills, or none>.

Questions:
1. <question>
2. <question>
3. <question>

Rules:
- A fact about the project carries its evidence: the command and its
  output, or the file and line. Give each fact a confidence from 0 to 100
  and say what would change your mind.
- An idea can be speculative. Label it as an idea. For each idea say what
  it gives if it works, and separately how likely you think it is. Do not
  drop an idea because it is unlikely.
- Rank your recommendations. Say which ones you would NOT implement.
- Disagreement with this brief is a valid finding.
- If you find no defects, say so. Sections 3 to 5 are still required.

Report shape, about <N> words; use more if the content needs it:
1. Bias
2. Findings (ranked; evidence; confidence)
3. Your approach: what you would do, as this lens sees it
4. The one idea you expect the others to overlook
5. What your approach costs elsewhere
6. Recommendations (at most <M>)
7. Anything else: what fits no heading above
```

## Cross-pollination round

Send this to each continuing reviewer, with the other two reports attached
verbatim and your proof of the discovery (command and output). Do not
attach your synthesis.

For a replacement seat, write a normal round-one brief with a new lens whose
premise starts from the verified discovery, and attach the round-one
reports as evidence. For an adversarial seat, attach the other two reports
and ask one question: where do these crack, on facts and on reasoning, with
evidence for each.

```
PANEL-BRIEF: <lens name>, round 2

The other two reports are below. Keep your lens. Do not look for agreement.

1. What in their reports changes your approach? Name the idea and its source.
2. What can you build from their ideas that they did not? Include an idea of
   theirs that fails at its own purpose but helps yours.
3. Which of their claims are wrong on the facts? Give the command or the
   file and line.
4. Your revised approach, and what you still hold against both of them.

READ-ONLY, as before. About <N> words.
```

## Notes

- The first line is a literal marker. It makes panel dispatches easy to find
  in a transcript, and a project hook can key on it.
- The `Skills:` line and "inside the project" keep a reviewer from loading
  the panel skill or reading its design files, where it would learn how its
  report is used.
- If a skill for controlled technical English is installed (`asd-ste100`),
  name it in the `Skills:` line and in the report-shape line.
- A question names an area ("what should change in the checks"). A list of
  candidate answers inside a question comes back as the first finding of
  all three reviewers.
- Describe work items by role ("the catalogue card"), not by an identifier
  that a project's tooling can read as a real dispatch.
