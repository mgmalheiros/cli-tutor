#!/usr/bin/env python3
"""Lesson 1: basic commands date, echo, man and clear."""

import os

import base

# ── Lesson content ──────────────────────────────────────────────────────────

LESSON_NUMBER = 1

LESSON_TEXT = (
    "This lesson covers the basic commands `date`, "
    "`echo`, `man` and `clear`. "
    "It also presents the main editing shortcuts, the shell history and "
    "**TAB** completion."
)

TASKS = [
    "Use the command `date`. Then use the command "
    "`date +%Y-%m-%d`. Finally, take a look at the options "
    "with `date --help`.",

    "Use the command `echo`. Then use the command "
    "`echo test`. Finally, try the command "
    "`echo test > file`. What happened?",

    "Use the command `man`. Then use the command "
    "`man echo` (use the **Q** key to quit). "
    "Finally, try `man date`.",

    "Use the **UP** key to go back in history and the "
    "**ENTER** key to execute the current command. Test also "
    "the **DOWN** key.",

    "Test other keys like **LEFT**, **RIGHT**, "
    "**BACKSPACE**.",

    "Use the command `clear`. Then repeat a previous command. "
    "Now try the **CONTROL+L** shortcut.",

    "Now just type `man` but do not press **ENTER**. "
    "Instead hit the **TAB** key twice. What happened?",
]


# ── Checks ──────────────────────────────────────────────────────────────────

def get_checks(folder):
    return [
        ("Task 2: file 'file' exists with content 'test'",
         lambda: base.check_file_contents(os.path.join(folder, "file"), "test")),
    ]


# ── Main ────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    base.lesson_main(LESSON_NUMBER, LESSON_TEXT, TASKS, get_checks)
