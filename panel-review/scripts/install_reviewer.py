"""Copy the panel-reviewer agent definition into ~/.claude/agents.

Idempotent. Run it from a machine's setup script, so that the agent type
exists before a Claude session starts. Exit 0 when the file is in place.
"""
from pathlib import Path
import sys

src = Path(__file__).resolve().parent.parent / "assets" / "panel-reviewer.md"
dst = Path.home() / ".claude" / "agents" / "panel-reviewer.md"

if not src.is_file():
    sys.exit(f"missing: {src}")
text = src.read_bytes()
if dst.is_file() and dst.read_bytes() == text:
    print(f"current: {dst}")
else:
    dst.parent.mkdir(parents=True, exist_ok=True)
    dst.write_bytes(text)
    print(f"installed: {dst}")
