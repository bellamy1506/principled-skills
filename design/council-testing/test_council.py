"""Checks of council.py in a scratch repository. Standard library and git.

  python design/council-testing/test_council.py

Makes a repository in a temporary folder, runs a small council in it, and
prints one line for each check. Exit 1 if a check fails.
"""
from __future__ import annotations

import json
import subprocess
import sys
import tempfile
from pathlib import Path

SCRIPT = Path(__file__).resolve().parents[2] / "council-testing" / "scripts" / "council.py"
FAILED = []


def sh(args, cwd):
    return subprocess.run(args, cwd=cwd, capture_output=True, text=True)


def git(args, cwd):
    p = sh(["git", "-c", "user.name=t", "-c", "user.email=t@local", *args], cwd)
    assert p.returncode == 0, p.stderr
    return p.stdout


def council(args, cwd):
    p = sh([sys.executable, str(SCRIPT), *args], cwd)
    return p.stdout + p.stderr


def check(name, ok, detail=""):
    print(("ok    " if ok else "FAIL  ") + name + (f"\n      {detail}" if not ok else ""))
    if not ok:
        FAILED.append(name)


def rows(home):
    text = (home / "measurements.jsonl").read_text(encoding="utf-8")
    return [json.loads(x) for x in text.splitlines()]


def main():
    tmp = Path(tempfile.mkdtemp(prefix="council-test-"))
    repo = tmp / "proj"
    repo.mkdir()
    git(["init", "-q"], repo)
    (repo / ".gitattributes").write_text("* text=auto eol=lf\n")
    (repo / "data.txt").write_text("a\nb\nc\n")
    (repo / "measure.py").write_text(
        "print(len(open('data.txt').read().split()))\n")
    (repo / "extra.cfg").write_text("x\n")
    git(["add", "-A"], repo)
    git(["commit", "-q", "-m", "base"], repo)
    home = tmp / "proj-council-t"

    out = council(["new", "t", "--members", "a,b", "--measure",
                   f'"{sys.executable}" measure.py',
                   "--protect", "measure.py", "--protect", "*.cfg"], repo)
    check("new records the files of two --protect flags",
          "measure files recorded: 2" in out, out)

    # 1. measure drift
    out = council(["measure", "t", "--in", "base", "--label", "baseline"], repo)
    check("a clean measurement prints no MEASURE CHANGED",
          "MEASURE CHANGED" not in out and rows(home)[-1]["value"] == 3.0, out)
    (home / "a" / "data.txt").write_text("a\n")
    git(["commit", "-qam", "less"], home / "a")
    (home / "b" / "extra.cfg").write_text("y\n")
    out = council(["measure", "t", "--in", "b"], repo)
    check("a changed measure file in a copy is reported and marked",
          "MEASURE CHANGED in b: extra.cfg" in out
          and rows(home)[-1]["measure_changed"]["copy"] == ["extra.cfg"], out)
    git(["checkout", "-q", "extra.cfg"], home / "b")
    (repo / "measure.py").write_text("print(0)\n")
    git(["commit", "-qam", "orchestrator changes the measure"], repo)
    out = council(["measure", "t", "--in", "a"], repo)
    check("a changed measure file in the project is reported and marked",
          "MEASURE CHANGED in the project checkout" in out
          and rows(home)[-1]["measure_changed"] == {"copy": [], "project": ["measure.py"]},
          out)
    git(["reset", "-q", "--hard", "HEAD~1"], repo)

    # 2. load stamp (no load figure on Windows; the keys are always there)
    r = rows(home)[-1]
    check("a row records load and cores",
          "load" in r and isinstance(r["cores"], int), str(r))

    # 3. final number
    check("a row records the commit measured",
          r["commit"] == git(["rev-parse", "HEAD"], home / "a").strip(), str(r))
    out = council(["integrate", "t", "--order", "a"], repo)
    check("integrate measures combined", '"value": 1.0' in out, out)
    out = council(["status", "t"], repo)
    check("status is quiet when combined is measured", "NO FINAL NUMBER" not in out, out)
    (home / "combined" / "data.txt").write_text("a\nb\n")
    git(["commit", "-qam", "a fix after the stress round"], home / "combined")
    out = council(["status", "t"], repo)
    check("status says when combined has no measurement of its last commit",
          "NO FINAL NUMBER" in out, out)

    # 5. measure --in all, --with
    before = len(rows(home))
    out = council(["measure", "t", "--in", "all", "--label", "corrected",
                   "--with", f'"{sys.executable}" -c "print(7)"'], repo)
    new = rows(home)[before:]
    check("measure --in all measures the base, each member and combined",
          [x["where"] for x in new] == ["base", "a", "b", "combined"], out)
    check("--with runs the other command and the row records it",
          all(x["value"] == 7.0 and "print(7)" in x["command"] for x in new), out)
    out = council(["status", "t"], repo)
    check("a --with row is not a final number", "NO FINAL NUMBER" in out, out)
    council(["measure", "t"], repo)
    out = council(["status", "t"], repo)
    check("a measurement of the last commit ends the message",
          "NO FINAL NUMBER" not in out and rows(home)[-1]["value"] == 2.0, out)
    (home / "combined" / "data.txt").write_text("a\n")
    git(["commit", "-qam", "one more"], home / "combined")
    out = council(["close", "t"], repo)
    check("close says when there is no final number", "NO FINAL NUMBER" in out, out)

    print("FAILED: " + ", ".join(FAILED) if FAILED else "all checks passed")
    print(f"scratch: {tmp}")
    sys.exit(1 if FAILED else 0)


if __name__ == "__main__":
    main()
