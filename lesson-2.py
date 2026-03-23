#!/usr/bin/env python3
"""Lesson 2: folder navigation with ls, cd, pwd, mkdir and rmdir."""

import os

import base

# ── Lesson content ──────────────────────────────────────────────────────────

LESSON_NUMBER = 2

LESSON_TEXT = (
    "This lesson covers folder navigation using the commands "
    "`ls`, `cd`, `pwd`, "
    "`mkdir` and `rmdir`. It also introduces "
    "the special folder symbols `/`, "
    "`.`, `..` and `~`."
)

TASKS = [
    "Run `pwd` to see your current directory. Then run "
    "`ls` to list its contents.",

    "Use `cd` to enter the lesson folder. Confirm you are "
    "inside it with `pwd`.",

    "Inside the lesson folder, create a subfolder called `alpha` "
    "using `mkdir alpha`. Verify it exists with `ls`.",

    "Navigate into `alpha` using `cd alpha`. Then "
    "go back to the lesson folder using `cd ..`, and confirm with "
    "`pwd`.",

    "Use `mkdir -p beta/gamma` to create a nested folder "
    "structure. Then use `ls beta` to verify that "
    "`gamma` was created inside `beta`.",

    "Navigate into `beta/gamma`. Hint: type `cd ` "
    "and then **TAB**, adding new letters and pressing "
    "**TAB** again. When inside `gamma`, use "
    "`cd ../..` to return to the lesson folder. Confirm with "
    "`pwd`.",

    "From the lesson folder, use `cd ~` to go to your home "
    "directory. Confirm with `pwd`. Then manually return to "
    "the lesson folder.",

    "Inside the lesson folder, create a folder called `delta` "
    "and use `echo hello > delta/greeting` to create a file "
    "inside it. Verify the file exists with `ls delta`.",

    "At the lesson folder, create a folder called `empty` "
    "using `mkdir empty`. Then remove it using "
    "`rmdir empty`. Verify it is gone with `ls`.",

    "Again from lesson folder, create the following structure: a folder `docs` containing "
    "a subfolder `drafts`, and a file `docs/readme` "
    "with the content `project notes`. Use "
    "`mkdir -p` and `echo` with redirection "
    "(`>`).",
]


# ── Checks ──────────────────────────────────────────────────────────────────

def get_checks(folder):
    return [
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


# ── Main ────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    base.lesson_main(LESSON_NUMBER, LESSON_TEXT, TASKS, get_checks)
