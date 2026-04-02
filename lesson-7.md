# Lesson

This lesson practices **pattern matching** with `grep` using basic regular expressions. In a basic regular expression, `.` matches any single character, `\.` matches a literal dot, `[a-z]` matches one character from a range, `*` means zero or more of the previous character, `^` anchors the match at the start of a line and `$` anchors it at the end. Use `grep 'pattern' file` to search inside a file and `wc -l` to count lines. Save results with `>` redirection.

# Setup

Create a folder called `sample` inside the lesson folder with the following files:

- `emails.txt` (one per line: `alice@example.com`, `bob.smith@mail.org`, `carol@server.net`, `dan99@example.com`, `eve@test`, `frank@mail.org`, `grace_h@example.com`)
- `numbers.txt` (one per line: `42`, `3.14`, `100`, `-7.5`, `0.001`, `99`, `2.0`, `hello`, `12x34`, `7`)
- `log.txt` (one per line: `2024-01-15 INFO server started`, `2024-01-15 ERROR disk full`, `2024-02-20 WARNING low memory`, `2024-02-20 INFO user login`, `2024-03-01 ERROR timeout`, `2024-03-01 INFO backup done`, `2024-03-01 WARNING high load`)
- `words.txt` (one per line: `cat`, `car`, `card`, `cart`, `care`, `cup`, `cut`, `bat`, `bar`, `bit`)
- `hosts.txt` (one per line: `192.168.1.1`, `10.0.0.1`, `172.16.0.100`, `192.168.1.20`, `10.0.0.255`, `abc.def.ghi`, `999.999.999.999`, `192.168.1.5`)

# Tasks

1. Enter the lesson folder. Use `cat sample/emails.txt | grep 'example'` to find all lines containing the string `example`. Now use the equivalent command `grep 'example' sample/emails.txt`

2. Use `grep 'ca.' sample/words.txt > ca_dot` to find all words that contain `ca` followed by any character. The `.` matches exactly one character, so `cat`, `car` and `card` all match (among others).

3. Use `grep 'ERROR' sample/log.txt | wc -l` to count all error lines from the log file. Then use `grep '2024-03' sample/log.txt` to see all entries from March 2024.

4. Use the `grep` command with the range `[0-9]` (twice) and the literal dot `\.` to show **only the floating point numbers** in `sample/numbers.txt`.

5. Use `grep '^2024-02' sample/log.txt > february` to find all log lines from February. The `^` anchors the match at the start of the line.

6. Use `grep 'org$' sample/emails.txt > at_org` to find all email addresses ending in `org`. The `$` anchors the match at the end of the line.

7. Use the `grep` command to find words in `sample/words.txt` that start with `c` and end with `t`. Use the `^` and `$` anchors to match to the whole line, and `.*` to match zero or more of any character in between.

8. Use the `grep` command to find all IP addresses listed in `hosts.txt` that are on the `192.168.1` subnet, placing them in a `local_net` file.

# Check

2. Verify that the file `ca_dot` exists and contains `cat`, `car`, `card`, `cart` and `care` (one per line, in this order).

5. Verify that the file `february` exists and contains `2024-02-20 WARNING low memory` and `2024-02-20 INFO user login` (one per line, in this order).

6. Verify that the file `at_org` exists and contains `bob.smith@mail.org` and `frank@mail.org` (one per line, in this order).

8. Verify that the file `local_net` exists and contains `192.168.1.1`, `192.168.1.20` and `192.168.1.5` (one per line, in this order).
