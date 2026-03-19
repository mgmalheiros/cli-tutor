#!/usr/bin/env python3
"""Lesson 3: $PATH, which, system folders, and ls flags."""

import os

import base

# ── Lesson content ──────────────────────────────────────────────────────────

LESSON_NUMBER = 3

LESSON_TEXT = (
    "This lesson explores the {code}`$PATH`{/code} variable, the "
    "{code}`which`{/code} command, and the main system folders. It also "
    "introduces the {code}`ls -a`{/code} and {code}`ls -la`{/code} flags "
    "for listing hidden files and detailed information."
)

TASKS = [
    "Run {code}`echo $PATH`{/code} to see the list of directories where "
    "the shell looks for commands. Notice that directories are separated "
    "by {code}`:`{/code}.",

    "Use {code}`which date`{/code} to find out where the {code}`date`{/code} "
    "command is located. Then try {code}`which echo`{/code} and "
    "{code}`which man`{/code}.",

    "Use {code}`ls /bin`{/code} to list the contents of the {code}`/bin`{/code} "
    "folder. Then try {code}`ls /usr/bin`{/code}. These are the main system "
    "folders where commands live.",

    "Pick one command from the {code}`/bin`{/code} listing and use "
    "{code}`man`{/code} to read its manual page (use the {bold}Q{/bold} key "
    "to quit). For example, {code}`man cat`{/code} or {code}`man cp`{/code}.",

    "Inside the lesson folder, use {code}`echo $PATH > my_path`{/code} to "
    "save your current {code}`$PATH`{/code} into a file called "
    "{code}`my_path`{/code}.",

    "Run {code}`ls -a`{/code} inside the lesson folder. Notice that it shows "
    "entries starting with {code}`.`{/code}, which are normally hidden. The "
    "{code}`.`{/code} entry is the current folder and {code}`..`{/code} is "
    "the parent folder.",

    "Run {code}`ls -la`{/code} inside the lesson folder. Compare the output "
    "with plain {code}`ls`{/code}. The {code}`-l`{/code} flag shows "
    "permissions, owner, size and date for each entry.",

    "Use {code}`which`{/code} to find where {code}`ls`{/code} is located. "
    "Then run {code}`ls -la`{/code} on that exact path to see its permissions "
    "and size. For example, if {code}`which ls`{/code} shows "
    "{code}`/usr/bin/ls`{/code}, run {code}`ls -la /usr/bin/ls`{/code}.",

    "Inside the lesson folder, create a file called {code}`visible`{/code} "
    "using {code}`echo public > visible`{/code}. Then create a hidden file "
    "called {code}`.hidden`{/code} using {code}`echo secret > .hidden`{/code}. "
    "Run {code}`ls`{/code} and then {code}`ls -a`{/code} to see the difference.",

    "Again in the lesson folder, run the command "
    "{code}`ls -la / > listing`{/code} and then inspect (by using a text "
    "editor) the contents of the {code}`listing`{/code} file.",
]


# ── Checks ──────────────────────────────────────────────────────────────────

def get_checks(folder):
    return [
        ("Task 5: file 'my_path' exists and is not empty",
         lambda: base.check_nonempty_file_exists(os.path.join(folder, "my_path"))),

        ("Task 9: file 'visible' exists with content 'public'",
         lambda: base.check_file_contents(os.path.join(folder, "visible"), "public")),

        ("Task 9: file '.hidden' exists with content 'secret'",
         lambda: base.check_file_contents(os.path.join(folder, ".hidden"), "secret")),

        ("Task 10: file 'listing' exists and is not empty",
         lambda: base.check_nonempty_file_exists(os.path.join(folder, "listing"))),
    ]


# ── Main ────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    base.lesson_main(LESSON_NUMBER, LESSON_TEXT, TASKS, get_checks)
