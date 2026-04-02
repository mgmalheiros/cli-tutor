#!/usr/bin/env python3
"""Lesson 6: text manipulation with wc, sort, uniq, grep, diff and pipes."""

import os

import base

# ── Lesson content ──────────────────────────────────────────────────────────

LESSON_NUMBER = 6

LESSON_TEXT = (
    "This lesson covers text manipulation tools: `wc` counts "
    "lines, words and characters; `sort` orders lines "
    "alphabetically; `uniq` removes adjacent duplicate lines; "
    "`grep` finds lines that contain a given string; and "
    "`diff` shows the differences between two files. The pipe "
    "operator `|` connects the output of one command to the "
    "input of the next, allowing you to combine tools. The `nano` "
    "text editor lets you edit files interactively."
)

TASKS = [
    "Enter the lesson folder. Use `wc sample/fruits.txt` to see "
    "three numbers: line count, word count and character count. Then try "
    "`wc -l sample/fruits.txt` for only the line count, "
    "`wc -w` for words and `wc -c` for characters.",

    "Use `sort sample/fruits.txt > sorted_fruits` to sort the "
    "fruits alphabetically and save the result. Use "
    "`cat sorted_fruits` to verify. Notice that duplicate "
    "entries now appear next to each other.",

    "Use `grep \"cherry\" sample/fruits.txt > found_cherry` to "
    "find all lines containing the string \"cherry\" and save them to a file.",

    "Use `diff sample/original.txt sample/revised.txt` to "
    "compare the two files. Notice how `diff` marks lines that "
    "differ: `<` for lines only in the first file and "
    "`>` for lines only in the second.",

    "Use `grep -v \"INFO\" sample/log.txt > no_info` to find "
    "all lines that do *not* contain \"INFO\" and save them. "
    "The `-v` flag inverts the match condition, showing only "
    "non-matching lines.",

    "Use `diff sample/original.txt sample/revised.txt > changes` "
    "to save the diff output into a file for later reference.",

    "Use `sort sample/fruits.txt | uniq > unique_fruits` to "
    "sort the fruits and then remove duplicate lines. The `|` "
    "(pipe) sends the output of `sort` as input to "
    "`uniq`. Note that `uniq` only removes "
    "*adjacent* duplicates, which is why `sort` "
    "must come first.",

    "Use `grep \"ERROR\" sample/log.txt | sort -r > sorted_errors` "
    "to extract all error lines and then sort them in reverse "
    "alphabetical order (using the `-r` flag).",

    "Use `tail -5 sample/log.txt | grep \"INFO\" > recent_info` "
    "to first get the last five log entries, then filter only the ones "
    "containing \"INFO\".",

    "Use `grep \"mammal\" sample/animals.txt | sort | uniq > mammals` "
    "to find all mammal entries, sort them and remove duplicates. "
    "This chains three commands together using two pipes.",

    "Copy the original file with "
    "`cat sample/original.txt > fixed`. Then open it with "
    "`nano fixed` and manually edit it so that its contents "
    "match `sample/revised.txt`: change `banana` "
    "to `blueberry` and `melon` to "
    "`dragonfruit`. Save with **Ctrl+O**, confirm the "
    "filename with **Enter**, and exit with **Ctrl+X**.",

    "Build a file by appending pipe results. First run "
    "`grep \"bird\" sample/animals.txt | sort | uniq > wildlife`. "
    "Then run "
    "`grep \"fish\" sample/animals.txt | sort | uniq >> wildlife`. "
    "Use `cat wildlife` to verify it contains the bird entries "
    "followed by the fish entries.",
]


# ── Setup ───────────────────────────────────────────────────────────────────

SAMPLE_FILES = {
    "fruits.txt": (
        "banana\napple\ncherry\nbanana\nmelon\n"
        "apple\nkiwi\nlemon\nbanana\ncherry\n"
    ),
    "log.txt": (
        "INFO server started\n"
        "ERROR connection failed\n"
        "INFO user logged in\n"
        "WARNING disk space low\n"
        "ERROR timeout occurred\n"
        "INFO backup complete\n"
        "WARNING high memory usage\n"
        "ERROR file not found\n"
        "INFO server stopped\n"
    ),
    "original.txt": "apple\nbanana\ncherry\nmelon\nkiwi\n",
    "revised.txt": "apple\nblueberry\ncherry\ndragonfruit\nkiwi\n",
    "animals.txt": (
        "dog mammal\ncat mammal\neagle bird\nsalmon fish\nfrog amphibian\n"
        "cat mammal\ndog mammal\nparrot bird\ntrout fish\ndog mammal\n"
    ),
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
        ("Task 2: file 'sorted_fruits' contains sorted fruit list",
         lambda: base.check_file_contents(
             os.path.join(folder, "sorted_fruits"),
             "apple\napple\nbanana\nbanana\nbanana\n"
             "cherry\ncherry\nkiwi\nlemon\nmelon")),

        ("Task 3: file 'found_cherry' contains cherry lines",
         lambda: base.check_file_contents(
             os.path.join(folder, "found_cherry"),
             "cherry\ncherry")),

        ("Task 5: file 'no_info' contains non-INFO log lines",
         lambda: base.check_file_contents(
             os.path.join(folder, "no_info"),
             "ERROR connection failed\n"
             "WARNING disk space low\n"
             "ERROR timeout occurred\n"
             "WARNING high memory usage\n"
             "ERROR file not found")),

        ("Task 6: file 'changes' contains diff output",
         lambda: base.check_file_contents(
             os.path.join(folder, "changes"),
             "2c2\n< banana\n---\n> blueberry\n"
             "4c4\n< melon\n---\n> dragonfruit")),

        ("Task 7: file 'unique_fruits' contains sorted unique fruits",
         lambda: base.check_file_contents(
             os.path.join(folder, "unique_fruits"),
             "apple\nbanana\ncherry\nkiwi\nlemon\nmelon")),

        ("Task 8: file 'sorted_errors' contains errors in reverse order",
         lambda: base.check_file_contents(
             os.path.join(folder, "sorted_errors"),
             "ERROR timeout occurred\n"
             "ERROR file not found\n"
             "ERROR connection failed")),

        ("Task 9: file 'recent_info' contains last INFO entries",
         lambda: base.check_file_contents(
             os.path.join(folder, "recent_info"),
             "INFO backup complete\nINFO server stopped")),

        ("Task 10: file 'mammals' contains unique sorted mammals",
         lambda: base.check_file_contents(
             os.path.join(folder, "mammals"),
             "cat mammal\ndog mammal")),

        ("Task 11: file 'fixed' matches revised.txt",
         lambda: base.check_file_contents(
             os.path.join(folder, "fixed"),
             "apple\nblueberry\ncherry\ndragonfruit\nkiwi")),

        ("Task 12: file 'wildlife' contains birds then fish",
         lambda: base.check_file_contents(
             os.path.join(folder, "wildlife"),
             "eagle bird\nparrot bird\nsalmon fish\ntrout fish")),
    ]


# ── Main ────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    base.lesson_main(LESSON_NUMBER, LESSON_TEXT, TASKS, get_checks, setup)
