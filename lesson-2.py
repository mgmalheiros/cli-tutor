#!/usr/bin/env python3
"""Lesson 2: folder navigation with ls, cd, pwd, mkdir and rmdir."""

import glob
import os
import re
import string
import sys

import base

# ── Lesson content ──────────────────────────────────────────────────────────

LESSON_TEXT = (
    "This lesson covers folder navigation using the commands "
    "{code}`ls`{/code}, {code}`cd`{/code}, {code}`pwd`{/code}, "
    "{code}`mkdir`{/code} and {code}`rmdir`{/code}. It also introduces "
    "the special folder symbols {code}`/`{/code}, "
    "{code}`.`{/code}, {code}`..`{/code} and {code}`~`{/code}."
)

TASKS = [
    "Run {code}`pwd`{/code} to see your current directory. Then run "
    "{code}`ls`{/code} to list its contents.",

    "Use {code}`cd`{/code} to enter the lesson folder. Confirm you are "
    "inside it with {code}`pwd`{/code}.",

    "Inside the lesson folder, create a subfolder called {code}`alpha`{/code} "
    "using {code}`mkdir alpha`{/code}. Verify it exists with {code}`ls`{/code}.",

    "Navigate into {code}`alpha`{/code} using {code}`cd alpha`{/code}. Then "
    "go back to the lesson folder using {code}`cd ..`{/code}, and confirm with "
    "{code}`pwd`{/code}.",

    "Use {code}`mkdir -p beta/gamma`{/code} to create a nested folder "
    "structure. Then use {code}`ls beta`{/code} to verify that "
    "{code}`gamma`{/code} was created inside {code}`beta`{/code}.",

    "Navigate into {code}`beta/gamma`{/code}. Hint: type {code}`cd `{/code} "
    "and then {bold}TAB{/bold}, adding new letters and pressing "
    "{bold}TAB{/bold} again. When inside {code}`gamma`{/code}, use "
    "{code}`cd ../..`{/code} to return to the lesson folder. Confirm with "
    "{code}`pwd`{/code}.",

    "From the lesson folder, use {code}`cd ~`{/code} to go to your home "
    "directory. Confirm with {code}`pwd`{/code}. Then manually return to "
    "the lesson folder.",

    "Inside the lesson folder, create a folder called {code}`delta`{/code} "
    "and use {code}`echo hello > delta/greeting`{/code} to create a file "
    "inside it. Verify the file exists with {code}`ls -la delta`{/code} "
    "(the flags {code}`-la`{/code} show extra information).",

    "At the lesson folder, create a folder called {code}`empty`{/code} "
    "using {code}`mkdir empty`{/code}. Then remove it using "
    "{code}`rmdir empty`{/code}. Verify it is gone with {code}`ls`{/code}.",

    "Again from lesson folder, create the following structure: a folder {code}`docs`{/code} containing "
    "a subfolder {code}`drafts`{/code}, and a file {code}`docs/readme`{/code} "
    "with the content {code}`project notes`{/code}. Use "
    "{code}`mkdir -p`{/code} and {code}`echo`{/code} with redirection "
    "({code}`>`{/code}).",
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

LESSON_NUMBER = 2
FOLDER_CHARS = string.ascii_lowercase


def find_folders():
    """Return sorted list of existing folder-2-? directories."""
    return sorted(glob.glob(f"folder-{LESSON_NUMBER}-[a-z]"))


def next_folder_name():
    """Return the next available folder-2-? name, or None if exhausted."""
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
        ("Task 3: folder 'alpha' exists and is empty",
         lambda: base.check_empty_folder_exists(os.path.join(folder, "alpha"))),

        ("Task 5: folder 'beta/gamma' exists and is empty",
         lambda: base.check_empty_folder_exists(os.path.join(folder, "beta", "gamma"))),

        ("Task 8: file 'delta/greeting' exists with content 'hello'",
         lambda: base.check_file_contents(os.path.join(folder, "delta", "greeting"), "hello")),

        ("Task 9: folder 'empty' does not exist",
         lambda: base.check_folder_not_exists(os.path.join(folder, "empty"))),

        ("Task 10: folder 'docs/drafts' exists and is empty",
         lambda: base.check_empty_folder_exists(os.path.join(folder, "docs", "drafts"))),

        ("Task 10: file 'docs/readme' exists with content 'project notes'",
         lambda: base.check_file_contents(os.path.join(folder, "docs", "readme"), "project notes")),
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
            print("Usage: lesson-2.py task N")
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
