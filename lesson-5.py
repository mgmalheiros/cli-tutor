#!/usr/bin/env python3
"""Lesson 5: basic text manipulation with cat, head, tail and >>."""

import os

import base

# ── Lesson content ──────────────────────────────────────────────────────────

LESSON_NUMBER = 5

LESSON_TEXT = (
    "This lesson covers basic text manipulation using the commands "
    "`cat`, `head` and `tail`, and "
    "the append redirection `>>`. The `cat` "
    "command displays or concatenates files, `head` shows the "
    "first lines and `tail` shows the last lines. The "
    "`>>` operator appends to a file instead of overwriting it."
)

TASKS = [
    "Enter the lesson folder. Use `cat sample/colors.txt` to "
    "display the colors file. Notice that the contents are shown in the "
    "terminal.",

    "Use `head sample/numbers.txt` to see the first 10 lines "
    "(the default). Since the file has exactly 10 lines, you see all of "
    "them. Now try `head -3 sample/numbers.txt` to see only "
    "the first 3 lines.",

    "Use `tail sample/numbers.txt` to see the last 10 lines. "
    "Now try `tail -4 sample/numbers.txt` to see only the "
    "last 4 lines.",

    "Use `head -3 sample/colors.txt > warm` to save the first "
    "3 colors (the warm ones) into a new file called `warm`.",

    "Use `tail -3 sample/colors.txt > cool` to save the last "
    "3 colors (the cool ones) into a new file called `cool`.",

    "In the lesson folder, use `echo`, `>` and "
    "`>>` to build a file line by line. Run "
    "`echo first > lines`, then "
    "`echo second >> lines`, then "
    "`echo third >> lines`. Use `cat lines` to "
    "verify. Notice that `>` creates (or overwrites) while "
    "`>>` appends.",

    "Inside the `sample` folder, use `cat` to "
    "concatenate two files into one: "
    "`cat greeting.txt farewell.txt > ../combined`. Then use "
    "`cat ../combined` to verify it contains both lines.",

    "Use `head -1 sample/numbers.txt > first_last` and then "
    "`tail -1 sample/numbers.txt >> first_last` to create a "
    "file with only the first and last lines of the numbers file.",

    "Use `head -5 sample/numbers.txt > top5` and then "
    "`tail -3 top5 > middle` to extract lines 3, 4 and 5 "
    "from the numbers file into a file called `middle`.",

    "Create a file called `summary` that contains the first "
    "2 colors, then a separator line `- - -`, then the last "
    "2 colors. Use `head`, `tail`, "
    "`echo` and the `>` and `>>` "
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
