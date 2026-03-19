#!/usr/bin/env python3
"""Lesson 2: folder navigation with ls, cd, pwd, mkdir and rmdir."""

import os

import base

# ── Lesson content ──────────────────────────────────────────────────────────

LESSON_NUMBER = 2

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
    "inside it. Verify the file exists with {code}`ls delta`{/code}.",

    "At the lesson folder, create a folder called {code}`empty`{/code} "
    "using {code}`mkdir empty`{/code}. Then remove it using "
    "{code}`rmdir empty`{/code}. Verify it is gone with {code}`ls`{/code}.",

    "Again from lesson folder, create the following structure: a folder {code}`docs`{/code} containing "
    "a subfolder {code}`drafts`{/code}, and a file {code}`docs/readme`{/code} "
    "with the content {code}`project notes`{/code}. Use "
    "{code}`mkdir -p`{/code} and {code}`echo`{/code} with redirection "
    "({code}`>`{/code}).",
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
