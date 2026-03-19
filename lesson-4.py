#!/usr/bin/env python3
"""Lesson 4: shell globs and wildcards."""

import base64
import os

import base

# ── Lesson content ──────────────────────────────────────────────────────────

LESSON_NUMBER = 4

LESSON_TEXT = (
    "This lesson covers shell {bold}globs{/bold} and {bold}wildcards{/bold}: "
    "{code}`*`{/code} matches any number of characters, {code}`?`{/code} "
    "matches exactly one character, {code}`[...]`{/code} matches a set or "
    "range of characters and {code}`{a,b,c}`{/code} expands into multiple "
    "alternatives. These patterns let you work with many files at once."
)

TASKS = [
    "Use {code}`cd`{/code} to enter the lesson folder. Then run "
    "{code}`ls sample/*.txt`{/code} to list all {code}`.txt`{/code} files "
    "inside {code}`sample`{/code}. The {code}`*`{/code} matches any number "
    "of characters.",

    "Run {code}`ls sample/*.csv`{/code} to list all {code}`.csv`{/code} "
    "files. Then try {code}`ls sample/*.*`{/code} to list all files that "
    "have an extension. Notice that {code}`README`{/code} is not listed "
    "because it has no dot.",

    "Run {code}`ls sample/note?.txt`{/code} to list files matching "
    "{code}`note`{/code} followed by exactly one character and "
    "{code}`.txt`{/code}. Notice that {code}`note10.txt`{/code} is not "
    "listed because {code}`?`{/code} matches only a single character.",

    "Run {code}`ls sample/note[13].txt`{/code} to list only "
    "{code}`note1.txt`{/code} and {code}`note3.txt`{/code}. The "
    "{code}`[...]`{/code} pattern matches any single character from the "
    "given set.",

    "Go to the {code}`sample`{/code} folder and then run "
    "{code}`ls note[1-3].txt`{/code} to list {code}`note1.txt`{/code}, "
    "{code}`note2.txt`{/code} and {code}`note3.txt`{/code}. Inside "
    "{code}`[...]`{/code}, a hyphen defines a range of characters.",

    "Inside the {code}`sample`{/code} folder run "
    "{code}`ls {report,data}.csv`{/code} to list {code}`report.csv`{/code} "
    "and {code}`data.csv`{/code}. The {code}`{a,b}`{/code} syntax expands "
    "into separate words — it is not a true wildcard but a shell expansion.",

    "In the lesson folder, use "
    "{code}`ls sample/*.txt > txt_list`{/code} to save the list of all "
    "{code}`.txt`{/code} files from {code}`sample`{/code} into a file "
    "called {code}`txt_list`{/code}.",

    "Go to the {code}`sample`{/code} folder and use {code}`ls ?????.*`{/code} "
    "to list all files whose name (before the extension) is exactly five "
    "characters long. Save the result into a file called {code}`../five_chars`{/code} "
    "using redirection.",
]


# ── Setup ───────────────────────────────────────────────────────────────────

# image.png bundled as base64
IMAGE_PNG_B64 = (
    "iVBORw0KGgoAAAANSUhEUgAAAIAAAACACAMAAAD04JH5AAAAFVBMVEUfIis7NjNbdyp7mTmTvDjY"
    "0bXR24LQt5i4AAAAqElEQVR42u3YMQoDIBBEUVXj/Y+cfppFUmjg/VrhlcO2HY1oRjv6RKtoRAAA"
    "AAAAAAD3ASNa0Sw6/Z9gAAAAgPsAAACAGfWiasD0IgAAAAAAAID/A7SoGhwt6tGKAAAA3gMAAAAA"
    "rGhHp4NjRAAAAAAAAADvAU4PDq2oGiAJBAAAAAAAAHgf0H4sATMCAAAAAAAAuA4oH/RoF/VoRCsC"
    "AAAAAAAAuA74AooztQEgXSCJAAAAAElFTkSuQmCC"
)

LOGO_SVG = (
    '<svg xmlns="http://www.w3.org/2000/svg" width="340" height="370">'
    '<defs><path id="a" fill="#231f20" d="M-62.99 36.37H62.99l62.99 109.1'
    "-17.5 30.31-62.99-109.1H-80.49zM41.16 74.18h-20l-24.5 42.44 30.31 "
    '17.5 24.5-42.44z"/></defs><g transform="translate(210 190)">'
    '<path fill="#ed1c24" d="m0-57.74-50 86.61H50z"/><use href="#a"/>'
    '<use href="#a" transform="rotate(120)"/>'
    '<use href="#a" transform="rotate(240)"/></g></svg>\n'
)

SAMPLE_FILES = {
    "note1.txt": "note one\n",
    "note2.txt": "note two\n",
    "note3.txt": "note three\n",
    "note10.txt": "note ten\n",
    "report.txt": "final report\n",
    "report.csv": "a,b,c\n",
    "data.csv": "1,2,3\n",
    "README": "read me\n",
    "logo.svg": LOGO_SVG,
}


def setup(folder):
    """Create the sample/ subfolder with pre-populated files."""
    sample = os.path.join(folder, "sample")
    os.makedirs(sample)
    for name, content in SAMPLE_FILES.items():
        with open(os.path.join(sample, name), "w") as f:
            f.write(content)
    # binary file
    with open(os.path.join(sample, "image.png"), "wb") as f:
        f.write(base64.b64decode(IMAGE_PNG_B64))


# ── Checks ──────────────────────────────────────────────────────────────────

TXT_LIST_EXPECTED = "\n".join([
    "sample/note10.txt",
    "sample/note1.txt",
    "sample/note2.txt",
    "sample/note3.txt",
    "sample/report.txt",
])

FIVE_CHARS_EXPECTED = "\n".join([
    "image.png",
    "note1.txt",
    "note2.txt",
    "note3.txt",
])


def get_checks(folder):
    return [
        ("Task 7: file 'txt_list' has the expected listing",
         lambda: base.check_file_contents(os.path.join(folder, "txt_list"), TXT_LIST_EXPECTED)),

        ("Task 8: file 'five_chars' has the expected listing",
         lambda: base.check_file_contents(os.path.join(folder, "five_chars"), FIVE_CHARS_EXPECTED)),
    ]


# ── Main ────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    base.lesson_main(LESSON_NUMBER, LESSON_TEXT, TASKS, get_checks, setup)
