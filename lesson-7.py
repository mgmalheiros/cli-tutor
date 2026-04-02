#!/usr/bin/env python3
"""Lesson 7: pattern matching with grep and basic regular expressions."""

import os

import base

# ── Lesson content ──────────────────────────────────────────────────────────

LESSON_NUMBER = 7

LESSON_TEXT = (
    "This lesson practices **pattern matching** with `grep` using "
    "basic regular expressions. In a basic regular expression, "
    "`.` matches any single character, `\\.` matches a literal dot, "
    "`[a-z]` matches one character from a range, "
    "`*` means zero or more of the previous character, "
    "`^` anchors the match at the start of a line and "
    "`$` anchors it at the end. Use `grep 'pattern' file` "
    "to search inside a file and `wc -l` to count lines. "
    "Save results with `>` redirection."
)


TASKS = [
    "Enter the lesson folder. Use "
    "`cat sample/emails.txt | grep 'example'` to find all lines "
    "containing the string `example`. Now use the equivalent command "
    "`grep 'example' sample/emails.txt`",

    "Use `grep 'ca.' sample/words.txt > ca_dot` to find all words "
    "that contain `ca` followed by any character. The `.` matches "
    "exactly one character, so `cat`, `car` and `card` all match "
    "(among others).",

    "Use `grep 'ERROR' sample/log.txt | wc -l` to count all error "
    "lines from the log file. Then use "
    "`grep '2024-03' sample/log.txt` to see all entries from March 2024.",

    "Use the `grep` command with the range `[0-9]` (twice) and the "
    "literal dot `\\.` to show **only the floating point numbers** in "
    "`sample/numbers.txt`.",

    "Use `grep '^2024-02' sample/log.txt > february` to find all "
    "log lines from February. The `^` anchors the match at the start "
    "of the line.",

    "Use `grep 'org$' sample/emails.txt > at_org` to find all "
    "email addresses ending in `org`. The `$` anchors the match at "
    "the end of the line.",

    "Use the `grep` command to find words in `sample/words.txt` that "
    "start with `c` and end with `t`. Use the `^` and `$` anchors "
    "to match to the whole line, and `.*` to match zero or more of "
    "any character in between.",

    "Use the `grep` command to find all IP addresses listed in "
    "`hosts.txt` that are on the `192.168.1` subnet, placing them "
    "in a `local_net` file.",
]


# ── Setup ───────────────────────────────────────────────────────────────────

SAMPLE_FILES = {
    "emails.txt": (
        "alice@example.com\n"
        "bob.smith@mail.org\n"
        "carol@server.net\n"
        "dan99@example.com\n"
        "eve@test\n"
        "frank@mail.org\n"
        "grace_h@example.com\n"
    ),
    "numbers.txt": (
        "42\n3.14\n100\n-7.5\n0.001\n99\n2.0\nhello\n12x34\n7\n"
    ),
    "log.txt": (
        "2024-01-15 INFO server started\n"
        "2024-01-15 ERROR disk full\n"
        "2024-02-20 WARNING low memory\n"
        "2024-02-20 INFO user login\n"
        "2024-03-01 ERROR timeout\n"
        "2024-03-01 INFO backup done\n"
        "2024-03-01 WARNING high load\n"
    ),
    "words.txt": (
        "cat\ncar\ncard\ncart\ncare\ncup\ncut\nbat\nbar\nbit\n"
    ),
    "hosts.txt": (
        "192.168.1.1\n"
        "10.0.0.1\n"
        "172.16.0.100\n"
        "192.168.1.20\n"
        "10.0.0.255\n"
        "abc.def.ghi\n"
        "999.999.999.999\n"
        "192.168.1.5\n"
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
        ("Task 2: file 'ca_dot' contains ca. matches",
         lambda: base.check_file_contents(
             os.path.join(folder, "ca_dot"),
             "cat\ncar\ncard\ncart\ncare")),

        ("Task 5: file 'february' contains February log lines",
         lambda: base.check_file_contents(
             os.path.join(folder, "february"),
             "2024-02-20 WARNING low memory\n"
             "2024-02-20 INFO user login")),

        ("Task 6: file 'at_org' contains .org email addresses",
         lambda: base.check_file_contents(
             os.path.join(folder, "at_org"),
             "bob.smith@mail.org\nfrank@mail.org")),

        ("Task 8: file 'local_net' contains 192.168.1.x addresses",
         lambda: base.check_file_contents(
             os.path.join(folder, "local_net"),
             "192.168.1.1\n192.168.1.20\n192.168.1.5")),
    ]


# ── Main ────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    base.lesson_main(LESSON_NUMBER, LESSON_TEXT, TASKS, get_checks, setup)
