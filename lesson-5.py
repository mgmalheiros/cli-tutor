#!/usr/bin/env python3
"""Lesson 5: basic text manipulation with cat, head, tail and >>."""

import os

import base

# ── Lesson content ──────────────────────────────────────────────────────────

LESSON_NUMBER = 5

LESSON_TEXT = (
    "This lesson covers basic text manipulation using the commands "
    "{code}`cat`{/code}, {code}`head`{/code} and {code}`tail`{/code}, and "
    "the append redirection {code}`>>`{/code}. The {code}`cat`{/code} "
    "command displays or concatenates files, {code}`head`{/code} shows the "
    "first lines and {code}`tail`{/code} shows the last lines. The "
    "{code}`>>`{/code} operator appends to a file instead of overwriting it."
)

TASKS = [
    "Enter the lesson folder. Use {code}`cat sample/colors.txt`{/code} to "
    "display the colors file. Notice that the contents are shown in the "
    "terminal.",

    "Use {code}`head sample/numbers.txt`{/code} to see the first 10 lines "
    "(the default). Since the file has exactly 10 lines, you see all of "
    "them. Now try {code}`head -3 sample/numbers.txt`{/code} to see only "
    "the first 3 lines.",

    "Use {code}`tail sample/numbers.txt`{/code} to see the last 10 lines. "
    "Now try {code}`tail -4 sample/numbers.txt`{/code} to see only the "
    "last 4 lines.",

    "Use {code}`head -3 sample/colors.txt > warm`{/code} to save the first "
    "3 colors (the warm ones) into a new file called {code}`warm`{/code}.",

    "Use {code}`tail -3 sample/colors.txt > cool`{/code} to save the last "
    "3 colors (the cool ones) into a new file called {code}`cool`{/code}.",

    "In the lesson folder, use {code}`echo`{/code}, {code}`>`{/code} and "
    "{code}`>>`{/code} to build a file line by line. Run "
    "{code}`echo first > lines`{/code}, then "
    "{code}`echo second >> lines`{/code}, then "
    "{code}`echo third >> lines`{/code}. Use {code}`cat lines`{/code} to "
    "verify. Notice that {code}`>`{/code} creates (or overwrites) while "
    "{code}`>>`{/code} appends.",

    "Inside the {code}`sample`{/code} folder, use {code}`cat`{/code} to "
    "concatenate two files into one: "
    "{code}`cat greeting.txt farewell.txt > ../combined`{/code}. Then use "
    "{code}`cat ../combined`{/code} to verify it contains both lines.",

    "Use {code}`head -1 sample/numbers.txt > first_last`{/code} and then "
    "{code}`tail -1 sample/numbers.txt >> first_last`{/code} to create a "
    "file with only the first and last lines of the numbers file.",

    "Use {code}`head -5 sample/numbers.txt > top5`{/code} and then "
    "{code}`tail -3 top5 > middle`{/code} to extract lines 3, 4 and 5 "
    "from the numbers file into a file called {code}`middle`{/code}.",

    "Create a file called {code}`summary`{/code} that contains the first "
    "2 colors, then a separator line {code}`- - -`{/code}, then the last "
    "2 colors. Use {code}`head`{/code}, {code}`tail`{/code}, "
    "{code}`echo`{/code} and the {code}`>`{/code} and {code}`>>`{/code} "
    "operators.",
]


# ── Setup ───────────────────────────────────────────────────────────────────

SAMPLE_FILES = {
    "colors.txt": "red\norange\nyellow\ngreen\nblue\nindigo\nviolet\n",
    "numbers.txt": "one\ntwo\nthree\nfour\nfive\nsix\nseven\neight\nnine\nten\n",
    "greeting.txt": "hello world\n",
    "farewell.txt": "goodbye world\n",
}


def setup(folder):
    """Create the sample/ subfolder with pre-populated files."""
    sample = os.path.join(folder, "sample")
    os.makedirs(sample)
    for name, content in SAMPLE_FILES.items():
        with open(os.path.join(sample, name), "w") as f:
            f.write(content)


# ── Checks ──────────────────────────────────────────────────────────────────

def get_checks(folder):
    return [
        ("Task 4: file 'warm' contains red, orange, yellow",
         lambda: base.check_file_contents(
             os.path.join(folder, "warm"), "red\norange\nyellow")),

        ("Task 5: file 'cool' contains blue, indigo, violet",
         lambda: base.check_file_contents(
             os.path.join(folder, "cool"), "blue\nindigo\nviolet")),

        ("Task 6: file 'lines' contains first, second, third",
         lambda: base.check_file_contents(
             os.path.join(folder, "lines"), "first\nsecond\nthird")),

        ("Task 7: file 'combined' contains hello world, goodbye world",
         lambda: base.check_file_contents(
             os.path.join(folder, "combined"), "hello world\ngoodbye world")),

        ("Task 8: file 'first_last' contains one, ten",
         lambda: base.check_file_contents(
             os.path.join(folder, "first_last"), "one\nten")),

        ("Task 9: file 'middle' contains three, four, five",
         lambda: base.check_file_contents(
             os.path.join(folder, "middle"), "three\nfour\nfive")),

        ("Task 10: file 'summary' contains red, orange, - - -, indigo, violet",
         lambda: base.check_file_contents(
             os.path.join(folder, "summary"), "red\norange\n- - -\nindigo\nviolet")),
    ]


# ── Main ────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    base.lesson_main(LESSON_NUMBER, LESSON_TEXT, TASKS, get_checks, setup)
