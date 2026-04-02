#!/usr/bin/env python3
"""Lesson 8: pattern matching and substitution with rg (ripgrep)."""

import os

import base

# ── Lesson content ──────────────────────────────────────────────────────────

LESSON_NUMBER = 8

LESSON_TEXT = (
    "This lesson practices **pattern matching and substitution** "
    "with `rg` (ripgrep) using extended regular expressions. The "
    "`rg` command works like `grep` but uses extended syntax by "
    "default: `+` means one or more, `?` means zero or one, and "
    "`*` means zero or more of the previous item. Character sets "
    "`[abc]` match one character from a group. The shorthand classes "
    "`\\d` (any digit), `\\w` (any word character: letter, digit or "
    "underscore) and `\\s` (any whitespace) match common categories. "
    "A capture group `(...)` saves part of a match, which can be "
    "referenced as `$1` in a replacement with the `-r` flag. Use "
    "`-o` to output only the matched portion."
)

TASKS = [
    "Enter the lesson folder. Run `echo 'error 404' | rg '\\d+'` "
    "and notice that `rg` finds the digit sequence `404`. Now use "
    "`rg 'ERROR' sample/log.txt` to find all error lines directly "
    "from a file — `rg` works like `grep` but uses extended regular "
    "expressions by default.",

    "Use `rg -o '\\d+' sample/data.txt > all_numbers` to extract "
    "every sequence of digits from the data file. The `\\d` matches "
    "any digit and `+` means one or more. The `-o` flag outputs "
    "only the matched parts, one per line.",

    "Use `rg '\\w+@\\w+\\.\\w+' sample/emails.txt > valid_emails` "
    "to find all lines matching a simple email pattern: one or more "
    "word characters, an `@`, one or more word characters, a literal "
    "dot, and one or more word characters. The `\\w` class matches "
    "letters, digits and underscores.",

    "Use `rg 'colou?r' sample/words.txt > col_words` to find both "
    "`color` and `colour`. The `?` makes the preceding `u` optional, "
    "matching zero or one occurrence.",

    "Use `rg 'gr[ae]y' sample/words.txt > grays` to find both "
    "`gray` and `grey`. The character set `[ae]` matches either "
    "`a` or `e`.",

    "Use `rg -o '\\w+\\s\\w+$' sample/log.txt > messages` to "
    "extract the two-word message at the end of each log line. Here "
    "`\\w+` matches a word, `\\s` matches the whitespace between "
    "them, and `$` anchors the match at the end of the line.",

    "Use `rg -o '(\\w+)@\\w+\\.\\w+' -r '$1' sample/emails.txt > "
    "usernames` to extract just the username from each email address. "
    "The parentheses `(...)` create a capture group around the first "
    "`\\w+`, and `-r '$1'` replaces the entire match with only the "
    "captured part.",

    "Use `rg` with the `-o` flag and `\\d` to extract only the dates "
    "(in `YYYY-MM-DD` format) from `sample/log.txt`. Save them to a "
    "file called `dates`.",

    "Use `rg` with `-o` to extract only the times (in `HH:MM` "
    "format) from `sample/log.txt`. Save them to a file called `times`.",

    "Use `rg` with a capture group and `-r '$1'` to extract only the "
    "domain names (like `example.com`) from each email address in "
    "`sample/emails.txt`. Save the result to `domains`.",
]


# ── Setup ───────────────────────────────────────────────────────────────────

SAMPLE_FILES = {
    "emails.txt": (
        "alice@example.com\n"
        "bob@mail.org\n"
        "carol@server.net\n"
        "dan99@example.com\n"
        "not-an-email\n"
        "frank@mail.org\n"
        "grace@example.com\n"
    ),
    "log.txt": (
        "2024-01-15 10:30 INFO server started\n"
        "2024-01-15 10:31 ERROR disk full\n"
        "2024-02-20 14:00 WARNING low memory\n"
        "2024-02-20 14:05 INFO user login\n"
        "2024-03-01 09:00 ERROR connection timeout\n"
        "2024-03-01 09:15 INFO backup done\n"
    ),
    "words.txt": (
        "color\ncolour\nfavor\nfavour\n"
        "gray\ngrey\ncenter\ncentre\n"
    ),
    "data.txt": (
        "item:1001 price:25\n"
        "item:1002 price:130\n"
        "item:1003 price:8\n"
        "item:2001 price:55\n"
        "item:2002 price:200\n"
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
        ("Task 2: file 'all_numbers' contains extracted digits",
         lambda: base.check_file_contents(
             os.path.join(folder, "all_numbers"),
             "1001\n25\n1002\n130\n1003\n8\n2001\n55\n2002\n200")),

        ("Task 3: file 'valid_emails' contains matching email lines",
         lambda: base.check_file_contents(
             os.path.join(folder, "valid_emails"),
             "alice@example.com\nbob@mail.org\ncarol@server.net\n"
             "dan99@example.com\nfrank@mail.org\ngrace@example.com")),

        ("Task 4: file 'col_words' contains color and colour",
         lambda: base.check_file_contents(
             os.path.join(folder, "col_words"),
             "color\ncolour")),

        ("Task 5: file 'grays' contains gray and grey",
         lambda: base.check_file_contents(
             os.path.join(folder, "grays"),
             "gray\ngrey")),

        ("Task 6: file 'messages' contains two-word log messages",
         lambda: base.check_file_contents(
             os.path.join(folder, "messages"),
             "server started\ndisk full\nlow memory\n"
             "user login\nconnection timeout\nbackup done")),

        ("Task 7: file 'usernames' contains email usernames",
         lambda: base.check_file_contents(
             os.path.join(folder, "usernames"),
             "alice\nbob\ncarol\ndan99\nfrank\ngrace")),

        ("Task 8: file 'dates' contains extracted ISO dates",
         lambda: base.check_file_contents(
             os.path.join(folder, "dates"),
             "2024-01-15\n2024-01-15\n2024-02-20\n"
             "2024-02-20\n2024-03-01\n2024-03-01")),

        ("Task 9: file 'times' contains extracted times",
         lambda: base.check_file_contents(
             os.path.join(folder, "times"),
             "10:30\n10:31\n14:00\n14:05\n09:00\n09:15")),

        ("Task 10: file 'domains' contains extracted domain names",
         lambda: base.check_file_contents(
             os.path.join(folder, "domains"),
             "example.com\nmail.org\nserver.net\n"
             "example.com\nmail.org\nexample.com")),
    ]


# ── Main ────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    base.lesson_main(LESSON_NUMBER, LESSON_TEXT, TASKS, get_checks, setup)
