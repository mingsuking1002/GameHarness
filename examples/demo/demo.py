"""Deterministic, standard-library demo of a board movement regression."""
from html import escape
from pathlib import Path
import sys


def route(start, roll, *, before_fix=False):
    steps = roll + int(before_fix and roll == 12)
    movement = [("dice", (start + offset) % 32) for offset in range(1, steps + 1)]
    if movement[-1][1] == 4:
        movement.append(("event", 7))
    return movement


def main(action):
    if action in ("repro-before", "movement"):
        path = route(24, 12, before_fix=action == "repro-before")
        actual = sum(cause == "dice" for cause, _ in path)
        if actual != 12:
            sys.exit(f"start=24, roll=12: expected 12 dice steps, observed {actual}")
        print("start=24, roll=12: exactly 12 dice steps")
    elif action == "replay":
        expected = [("dice", position) for position in [25, 26, 27, 28, 29, 30, 31, 0, 1, 2, 3, 4]]
        expected.append(("event", 7))
        if route(24, 12) != expected:
            sys.exit("Replay diverged: the event must follow the twelfth dice step")
        print("Existing replay keeps event movement separate")
    elif action == "wiki":
        history = Path("history.md").read_text(encoding="utf-8")
        handoff = Path("HANDOFF.md").read_text(encoding="utf-8")
        Path(sys.argv[2]).write_text(
            "<!doctype html><html lang='ko'><meta charset='utf-8'><title>데모 위키</title>"
            "<h1>게임 검증 기록</h1><pre>" + escape(history) + "</pre><h2>인수인계</h2><pre>"
            + escape(handoff) + "</pre></html>", encoding="utf-8"
        )
    else:
        sys.exit("Unknown check")


if __name__ == "__main__":
    main(sys.argv[1])
