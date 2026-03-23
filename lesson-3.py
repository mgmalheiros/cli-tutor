#!/usr/bin/env python3
"""Lesson 3: $PATH, which, system folders, and ls flags."""

import os

import base

# ── Lesson content ──────────────────────────────────────────────────────────

LESSON_NUMBER = 3

LESSON_TEXT = (
    "This lesson explores the `$PATH` variable, the "
    "`which` command, and the main system folders. It also "
    "introduces the `ls -a` and `ls -la` flags "
    "for listing hidden files and detailed information."
)

TASKS = [
    "Run `echo $PATH` to see the list of directories where "
    "the shell looks for commands. Notice that directories are separated "
    "by `:`.",

    "Use `which date` to find out where the `date` "
    "command is located. Then try `which echo` and "
    "`which man`.",

    "Use `ls /bin` to list the contents of the `/bin` "
    "folder. Then try `ls /usr/bin`. These are the main system "
    "folders where commands live.",

    "Pick one command from the `/bin` listing and use "
    "`man` to read its manual page (use the **Q** key "
    "to quit). For example, `man cat` or `man cp`.",

    "Inside the lesson folder, use `echo $PATH > my_path` to "
    "save your current `$PATH` into a file called "
    "`my_path`.",

    "Run `ls -a` inside the lesson folder. Notice that it shows "
    "entries starting with `.`, which are normally hidden. The "
    "`.` entry is the current folder and `..` is "
    "the parent folder.",

    "Run `ls -la` inside the lesson folder. Compare the output "
    "with plain `ls`. The `-l` flag shows "
    "permissions, owner, size and date for each entry.",

    "Use `which` to find where `ls` is located. "
    "Then run `ls -la` on that exact path to see its permissions "
    "and size. For example, if `which ls` shows "
    "`/usr/bin/ls`, run `ls -la /usr/bin/ls`.",

    "Inside the lesson folder, create a file called `visible` "
    "using `echo public > visible`. Then create a hidden file "
    "called `.hidden` using `echo secret > .hidden`. "
    "Run `ls` and then `ls -a` to see the difference.",

    "Again in the lesson folder, run the command "
    "`ls -la / > listing` and then inspect (by using a text "
    "editor) the contents of the `listing` file.",
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
