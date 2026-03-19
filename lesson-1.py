#!/usr/bin/env python3
"""Lesson 1: basic commands date, echo, man and clear."""

import os

import base

# ── Lesson content ──────────────────────────────────────────────────────────

LESSON_NUMBER = 1

LESSON_TEXT = (
    "This lesson covers the basic commands {code}`date`{/code}, "
    "{code}`echo`{/code}, {code}`man`{/code} and {code}`clear`{/code}. "
    "It also presents the main editing shortcuts, the shell history and "
    "{bold}TAB{/bold} completion."
)

TASKS = [
    "Use the command {code}`date`{/code}. Then use the command "
    "{code}`date +%Y-%m-%d`{/code}. Finally, take a look at the options "
    "with {code}`date --help`{/code}.",

    "Use the command {code}`echo`{/code}. Then use the command "
    "{code}`echo test`{/code}. Finally, try the command "
    "{code}`echo test > file`{/code}. What happened?",

    "Use the command {code}`man`{/code}. Then use the command "
    "{code}`man echo`{/code} (use the {bold}Q{/bold} key to quit). "
    "Finally, try {code}`man date`{/code}.",

    "Use the {bold}UP{/bold} key to go back in history and the "
    "{bold}ENTER{/bold} key to execute the current command. Test also "
    "the {bold}DOWN{/bold} key.",

    "Test other keys like {bold}LEFT{/bold}, {bold}RIGHT{/bold}, "
    "{bold}BACKSPACE{/bold}.",

    "Use the command {code}`clear`{/code}. Then repeat a previous command. "
    "Now try the {bold}CONTROL+L{/bold} shortcut.",

    "Now just type {code}`man`{/code} but do not press {bold}ENTER{/bold}. "
    "Instead hit the {bold}TAB{/bold} key twice. What happened?",
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
