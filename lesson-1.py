#!/usr/bin/env python3
"""Lesson 1: basic commands date, echo, man and clear."""

import glob
import os
import re
import string
import sys

import base

# ── Lesson content ──────────────────────────────────────────────────────────

LESSON_TEXT = (
    "This lesson covers the basic commands {code}`date`{/code}, "
    "{code}`echo`{/code}, {code}`man`{/code} and {code}`clear`{/code}. "
    "It also presents the main editing shortcuts, the shell history and "
    "{bold}tab{/bold} completion."
)

TASKS = [
    "Use the command {code}`date`{/code}. Then use the command "
    "{code}`date +%Y-%m-%d`{/code}. Finally, take a look at the options "
    "with {code}`date --help`{/code}.",

    "Use the command {code}`echo`{/code}. Then use the command "
    "{code}`echo test`{/code}. Finally, try the command "
    "{code}`echo test > file`{/code}. What happened?",

    "Use the command {code}`man`{/code}. Then use the command "
    "{code}`man echo`{/code} (use the {bold}q{/bold} key to quit). "
    "Finally, try {code}`man date`{/code}.",

    "Use the {bold}up{/bold} key to go back in history and the "
    "{bold}enter{/bold} key to execute the current command. Test also "
    "the {bold}down{/bold} key.",

    "Test other keys like {bold}left{/bold}, {bold}right{/bold}, "
    "{bold}backspace{/bold}.",

    "Use the command {code}`clear`{/code}. Then repeat a previous command. "
    "Now try the {code}`control+l`{/code} shortcut.",

    "Now just type {code}`man`{/code} but do not press {bold}enter{/bold}. "
    "Instead hit the {bold}tab{/bold} key twice. What happened?",
]

# ── ANSI helpers ────────────────────────────────────────────────────────────

BOLD = "\033[1m"
ITALIC = "\033[3m"
CODE = "\033[36m"  # cyan for inline code
GREEN = "\033[32m"
RED = "\033[31m"
RESET = "\033[0m"


def render(text):
    """Convert markup to ANSI sequences.

    Supported markers:
      {bold}...{/bold}     → bold
      {italic}...{/italic} → italic
      {code}...{/code}     → cyan
      `...`                → cyan (backticks)
    """
    text = text.replace("{bold}", BOLD).replace("{/bold}", RESET)
    text = text.replace("{italic}", ITALIC).replace("{/italic}", RESET)
    text = text.replace("{code}", CODE).replace("{/code}", RESET)
    text = re.sub(r'`([^`]+)`', CODE + r'\1' + RESET, text)
    return text


# ── Folder naming helpers ───────────────────────────────────────────────────

LESSON_NUMBER = 1
FOLDER_CHARS = string.ascii_lowercase


def find_folders():
    """Return sorted list of existing folder-1-? directories."""
    return sorted(glob.glob(f"folder-{LESSON_NUMBER}-[a-z]"))


def next_folder_name():
    """Return the next available folder-1-? name, or None if exhausted."""
    existing = {os.path.basename(f) for f in find_folders()}
    for ch in FOLDER_CHARS:
        name = f"folder-{LESSON_NUMBER}-{ch}"
        if name not in existing:
            return name
    return None


# ── Commands ────────────────────────────────────────────────────────────────

def cmd_lesson():
    print(render(LESSON_TEXT))
    print()
    print("Commands:")
    print("  setup    Create a new practice folder")
    print("  tasks    Show all tasks")
    print("  task N   Show task N")
    print("  check    Check your work")


def cmd_setup():
    name = next_folder_name()
    if name is None:
        print("All folder slots (a-z) are taken.")
        sys.exit(1)
    os.makedirs(name)
    print(f"Created {name}")


def cmd_tasks():
    for i, task in enumerate(TASKS, 1):
        print(render(f"{BOLD}{i}.{RESET} {task}"))
        if i < len(TASKS):
            print()


def cmd_task(n):
    if n < 1 or n > len(TASKS):
        print(f"Error: task {n} does not exist. Valid range: 1-{len(TASKS)}.")
        sys.exit(1)
    print(render(f"{BOLD}{n}.{RESET} {TASKS[n - 1]}"))


def cmd_check():
    folders = find_folders()
    if not folders:
        print("No folder found. Run 'setup' first.")
        sys.exit(1)
    folder = folders[-1]
    print(f"Checking folder {folder}...")

    checks = [
        ("Task 2: file 'file' exists with content 'test'",
         lambda: base.check_file_contents(os.path.join(folder, "file"), "test")),
    ]

    passed = 0
    failed = 0
    for desc, fn in checks:
        ok, msg = fn()
        if ok:
            passed += 1
            print(f"  {BOLD}{GREEN}✓{RESET} {desc}")
        else:
            failed += 1
            print(f"  {BOLD}{RED}✗{RESET} {desc}")
            print(f"    {msg}")

    total = passed + failed
    if failed == 0:
        print(f"\nAll checks passed ({total}/{total}).")
    else:
        print(f"\n{passed}/{total} checks passed, {failed} failed.")
        sys.exit(1)


# ── Main ────────────────────────────────────────────────────────────────────

def main():
    args = sys.argv[1:]

    if not args:
        cmd_lesson()
    elif args[0] == "setup":
        cmd_setup()
    elif args[0] == "tasks":
        cmd_tasks()
    elif args[0] == "task":
        if len(args) < 2:
            print("Usage: lesson-1.py task N")
            sys.exit(1)
        try:
            n = int(args[1])
        except ValueError:
            print(f"Error: '{args[1]}' is not a valid task number.")
            sys.exit(1)
        cmd_task(n)
    elif args[0] == "check":
        cmd_check()
    else:
        print(f"Unknown command: {args[0]}")
        print("Available commands: setup, tasks, task N, check")
        sys.exit(1)


if __name__ == "__main__":
    main()
