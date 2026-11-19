"""Mechanical steps of a council: private copies, status, measure, integrate.

Standard library and git only. Run from inside the project.

  council.py new NAME --members a,b,c --measure "CMD" [--protect GLOB]... [--base REF]
  council.py add NAME MEMBER [--from combined|base]
  council.py status NAME
  council.py measure NAME [--in base|combined|MEMBER|all] [--label TEXT] [--with "CMD"]
  council.py integrate NAME --order a,b,c [--each]
  council.py close NAME

A council lives beside the project in <project>-council-NAME/. Each member
has its own worktree there on branch council/NAME/<member>. The measure
command prints the goal number on its last line. Give --protect once for
each glob of files that define the measure. A project that is not a
git repository is copied into <...>/base-repo and committed there first.
"""
from __future__ import annotations

import argparse
import fnmatch
import json
import os
import shutil
import subprocess
import sys
import time
from pathlib import Path


def run(cmd, cwd, check=True, stdin=None):
    p = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True, input=stdin)
    if check and p.returncode:
        sys.exit(f"FAILED ({p.returncode}): {' '.join(cmd)}\n{p.stdout}{p.stderr}")
    return p


def git(args, cwd, check=True, stdin=None):
    return run(["git", *args], cwd, check, stdin)


def repo_root(start: Path) -> Path | None:
    p = git(["rev-parse", "--show-toplevel"], start, check=False)
    return Path(p.stdout.strip()) if p.returncode == 0 else None


def home(name: str) -> tuple[Path, dict]:
    here = Path.cwd()
    root = repo_root(here) or here
    d = root.parent / f"{root.name}-council-{name}"
    f = d / "council.json"
    if not f.is_file():
        sys.exit(f"no council {name!r}: {f} not found")
    return d, json.loads(f.read_text(encoding="utf-8"))


def save(d: Path, cfg: dict) -> None:
    (d / "council.json").write_text(json.dumps(cfg, indent=2), encoding="utf-8")


def worktree(cfg: dict, d: Path, member: str, start: str) -> None:
    git(["worktree", "add", "-b", f"council/{cfg['name']}/{member}",
         str(d / member), start], Path(cfg["repo"]))


def cmd_new(a) -> None:
    here = Path.cwd()
    root = repo_root(here)
    src = root or here
    d = src.parent / f"{src.name}-council-{a.name}"
    if d.exists():
        sys.exit(f"exists: {d}")
    d.mkdir()
    if root is None:  # not a git repository: copy it and commit the copy
        repo = d / "base-repo"
        shutil.copytree(src, repo)
        git(["init", "-q"], repo)
        git(["add", "-A"], repo)
        git(["-c", "user.name=council", "-c", "user.email=council@local",
             "commit", "-q", "-m", "council base"], repo)
        base = "HEAD"
    else:
        repo, base = root, a.base
    sha = git(["rev-parse", base], repo).stdout.strip()
    members = [m.strip() for m in a.members.split(",") if m.strip()]
    cfg = {"name": a.name, "repo": str(repo), "base": sha, "members": members,
           "measure": a.measure, "protect": a.protect or []}
    cfg["protect_base"] = protected_at_base(cfg)
    for m in members:
        worktree(cfg, d, m, sha)
    worktree(cfg, d, "combined", sha)
    save(d, cfg)
    print(f"council {a.name}: {d}\nbase {sha[:10]}")
    for m in members:
        print(f"  {m}: {d / m}")
    if cfg["protect_base"]:
        print(f"measure files recorded: {len(cfg['protect_base'])}")
    else:
        print("NO MEASURE FILES RECORDED: no file at the base matches --protect. "
              "A change to the measure will not be reported.")


def cmd_add(a) -> None:
    d, cfg = home(a.name)
    start = cfg["base"] if a.source == "base" else f"council/{cfg['name']}/combined"
    worktree(cfg, d, a.member, start)
    cfg.setdefault("added", []).append(a.member)
    save(d, cfg)
    print(f"  {a.member}: {d / a.member} (from {a.source})")


def changed(cfg: dict, member: str) -> list[str]:
    out = git(["diff", "--name-only", f"{cfg['base']}..council/{cfg['name']}/{member}"],
              Path(cfg["repo"])).stdout
    return [x for x in out.splitlines() if x]


def protected_hits(cfg: dict, files: list[str]) -> list[str]:
    return [f for f in files if any(fnmatch.fnmatch(f, g) for g in cfg["protect"])]


def protected_at_base(cfg: dict) -> dict[str, str]:
    """Blob hash of each file at the base commit that matches a --protect glob."""
    out = git(["ls-tree", "-r", "-z", cfg["base"]], Path(cfg["repo"])).stdout
    found = {}
    for entry in out.split("\0"):
        meta, _, path = entry.partition("\t")
        if path and meta.split()[1] == "blob":
            found[path] = meta.split()[2]
    return {f: found[f] for f in protected_hits(cfg, sorted(found))}


def protected_now(cfg: dict, cwd: Path) -> dict[str, str]:
    """Blob hash of each file in a working tree that matches a --protect glob."""
    out = git(["ls-files", "-z", "-c", "-o", "--exclude-standard"], cwd).stdout
    files = [f for f in protected_hits(cfg, sorted(set(out.split("\0")) - {""}))
             if (cwd / f).is_file()]
    if not files:
        return {}
    hashes = git(["hash-object", "--stdin-paths"], cwd, stdin="\n".join(files) + "\n")
    return dict(zip(files, hashes.stdout.split()))


def measure_changed(cfg: dict, cwd: Path) -> list[str]:
    """Measure files that differ from the base: changed, added or removed."""
    base, now = cfg["protect_base"], protected_now(cfg, cwd)
    return sorted(f for f in set(base) | set(now) if base.get(f) != now.get(f))


def cmd_status(a) -> None:
    d, cfg = home(a.name)
    seen: dict[str, list[str]] = {}
    for m in cfg["members"] + cfg.get("added", []):
        files = changed(cfg, m)
        n = git(["rev-list", "--count", f"{cfg['base']}..council/{cfg['name']}/{m}"],
                Path(cfg["repo"])).stdout.strip()
        dirty = git(["status", "--porcelain"], d / m).stdout.strip()
        print(f"{m}: {n} commit(s), {len(files)} file(s)"
              + (", UNCOMMITTED changes" if dirty else ""))
        for f in protected_hits(cfg, files):
            print(f"  PROTECTED file changed: {f}")
        for f in files:
            seen.setdefault(f, []).append(m)
    both = {f: ms for f, ms in seen.items() if len(ms) > 1}
    print(f"files changed by more than one member: {len(both)}")
    for f, ms in sorted(both.items()):
        print(f"  {f}: {', '.join(ms)}")
    no_final_number(d, cfg)


def load_now() -> float | None:
    """One-minute load average. Windows does not give one."""
    try:
        return round(os.getloadavg()[0], 1)
    except (AttributeError, OSError):
        return None


def measure(d: Path, cfg: dict, where: str, label: str, command: str = "") -> dict:
    cwd = Path(cfg["repo"]) if where == "base" else d / where
    if where == "base":  # measure the base commit in a detached worktree
        cwd = d / "_base"
        if not cwd.exists():
            git(["worktree", "add", "--detach", str(cwd), cfg["base"]], Path(cfg["repo"]))
    drift = {}
    if cfg.get("protect_base"):  # a council made before this check has no record
        drift = {"copy": measure_changed(cfg, cwd),
                 "project": measure_changed(cfg, Path(cfg["repo"]))}
    load, cores = load_now(), os.cpu_count()
    commit = git(["rev-parse", "HEAD"], cwd).stdout.strip()
    dirty = bool(git(["status", "--porcelain", "--untracked-files=no"], cwd).stdout.strip())
    t = time.time()
    p = subprocess.run(command or cfg["measure"], cwd=cwd, shell=True, capture_output=True, text=True)
    lines = [x for x in p.stdout.strip().splitlines() if x.strip()]
    last = lines[-1].strip() if lines else ""
    try:
        value = float(last.split()[-1])
    except (ValueError, IndexError):
        value = None
    row = {"where": where, "label": label, "exit": p.returncode, "value": value,
           "last_line": last, "wall_s": round(time.time() - t, 1),
           "at": time.strftime("%Y-%m-%dT%H:%M:%S"), "load": load, "cores": cores,
           "commit": commit, "dirty": dirty}
    if any(drift.values()):
        row["measure_changed"] = drift
    if command:  # not the council's measure: the row says which command it was
        row["command"] = command
    with (d / "measurements.jsonl").open("a", encoding="utf-8") as f:
        f.write(json.dumps(row) + "\n")
    print(json.dumps(row))
    if load and cores and load > cores:
        print(f"MACHINE LOADED: load {load} on {cores} cores when this measurement "
              "started.\n  A time, or a count that depends on a timeout, is not "
              "reliable.")
    if drift.get("copy"):
        print(f"MEASURE CHANGED in {where}: {', '.join(drift['copy'])}\n"
              "  This number is not from the measure the council started with.")
    if drift.get("project"):
        print("MEASURE CHANGED in the project checkout since the council base: "
              f"{', '.join(drift['project'])}\n"
              "  The copies hold the old measure. A number from the project and a "
              "number from a copy are not the same measure.")
    return row


def no_final_number(d: Path, cfg: dict) -> None:
    """Say so when combined has changed and its last commit has no measurement."""
    tip = git(["rev-parse", "--verify", "-q", f"council/{cfg['name']}/combined"],
              Path(cfg["repo"]), check=False).stdout.strip()
    if not tip or tip == cfg["base"]:
        return
    f = d / "measurements.jsonl"
    done = [json.loads(x) for x in f.read_text(encoding="utf-8").splitlines()] if f.is_file() else []
    if any(r.get("where") == "combined" and r.get("commit") == tip and not r.get("dirty")
           and not r.get("command") for r in done):
        return
    print(f"NO FINAL NUMBER: combined is at {tip[:10]} and no measurement of that "
          f"commit is recorded.\n  Run: council.py measure {cfg['name']}\n"
          "  If you do not, the report must say that the council has no final number.")


def cmd_measure(a) -> None:
    d, cfg = home(a.name)
    wheres = ["base", *cfg["members"], "combined"] if a.where == "all" else [a.where]
    for w in wheres:
        measure(d, cfg, w, a.label, a.command)


def cmd_integrate(a) -> None:
    d, cfg = home(a.name)
    comb = d / "combined"
    if git(["status", "--porcelain"], comb).stdout.strip():
        sys.exit("combined has uncommitted changes; commit or discard them first")
    for m in [x.strip() for x in a.order.split(",") if x.strip()]:
        bad = protected_hits(cfg, changed(cfg, m))
        if bad:
            sys.exit(f"REFUSED {m}: changes protected file(s): {', '.join(bad)}")
        branch = f"council/{cfg['name']}/{m}"
        todo = git(["rev-list", "--reverse", f"HEAD..{branch}"], comb).stdout.split()
        if not todo:
            print(f"{m}: nothing new")
            continue
        p = git(["cherry-pick", "--allow-empty", "--keep-redundant-commits", *todo],
                comb, check=False)
        if p.returncode:
            files = git(["diff", "--name-only", "--diff-filter=U"], comb).stdout.split()
            git(["cherry-pick", "--abort"], comb, check=False)
            sys.exit(f"CONFLICT at {m}: {', '.join(files) or p.stderr.strip()}\n"
                     "combined is unchanged for this member. Resolve by policy, "
                     "then run integrate again with the remaining order.")
        print(f"{m}: applied {len(todo)} commit(s)")
        if a.each:
            measure(d, cfg, "combined", f"after {m}")
    if not a.each:
        measure(d, cfg, "combined", "after " + a.order)


def cmd_close(a) -> None:
    d, cfg = home(a.name)
    repo = Path(cfg["repo"])
    no_final_number(d, cfg)
    for m in cfg["members"] + cfg.get("added", []) + ["combined", "_base"]:
        if (d / m).exists():
            git(["worktree", "remove", "--force", str(d / m)], repo, check=False)
    print(f"worktrees removed; branches council/{cfg['name']}/* and {d} are kept")


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    sub = ap.add_subparsers(dest="cmd", required=True)
    s = sub.add_parser("new"); s.add_argument("name")
    s.add_argument("--members", required=True); s.add_argument("--measure", required=True)
    s.add_argument("--protect", action="append", metavar="GLOB",
                   help="files that define the measure; give the flag once for each glob")
    s.add_argument("--base", default="HEAD")
    s.set_defaults(fn=cmd_new)
    s = sub.add_parser("add"); s.add_argument("name"); s.add_argument("member")
    s.add_argument("--from", dest="source", choices=["combined", "base"], default="combined")
    s.set_defaults(fn=cmd_add)
    s = sub.add_parser("status"); s.add_argument("name"); s.set_defaults(fn=cmd_status)
    s = sub.add_parser("measure"); s.add_argument("name")
    s.add_argument("--in", dest="where", default="combined",
                   help="base, combined, a member, or all (base, each member, combined)")
    s.add_argument("--label", default="")
    s.add_argument("--with", dest="command", default="", metavar="CMD",
                   help="run this command in place of the council's measure; the row records it")
    s.set_defaults(fn=cmd_measure)
    s = sub.add_parser("integrate"); s.add_argument("name")
    s.add_argument("--order", required=True); s.add_argument("--each", action="store_true")
    s.set_defaults(fn=cmd_integrate)
    s = sub.add_parser("close"); s.add_argument("name"); s.set_defaults(fn=cmd_close)
    a = ap.parse_args()
    a.fn(a)


if __name__ == "__main__":
    main()
