# Lesson

This lesson practices **pattern matching and substitution** with `rg` (ripgrep) using extended regular expressions. The `rg` command works like `grep` but uses extended syntax by default: `+` means one or more, `?` means zero or one, and `*` means zero or more of the previous item. Character sets `[abc]` match one character from a group. The shorthand classes `\d` (any digit), `\w` (any word character: letter, digit or underscore) and `\s` (any whitespace) match common categories. A capture group `(...)` saves part of a match, which can be referenced as `$1` in a replacement with the `-r` flag. Use `-o` to output only the matched portion.

# Setup

Create a folder called `sample` inside the lesson folder with the following files:

- `emails.txt` (one per line: `alice@example.com`, `bob@mail.org`, `carol@server.net`, `dan99@example.com`, `not-an-email`, `frank@mail.org`, `grace@example.com`)
- `log.txt` (one per line: `2024-01-15 10:30 INFO server started`, `2024-01-15 10:31 ERROR disk full`, `2024-02-20 14:00 WARNING low memory`, `2024-02-20 14:05 INFO user login`, `2024-03-01 09:00 ERROR connection timeout`, `2024-03-01 09:15 INFO backup done`)
- `words.txt` (one per line: `color`, `colour`, `favor`, `favour`, `gray`, `grey`, `center`, `centre`)
- `data.txt` (one per line: `item:1001 price:25`, `item:1002 price:130`, `item:1003 price:8`, `item:2001 price:55`, `item:2002 price:200`)

# Tasks

1. Enter the lesson folder. Run `echo 'error 404' | rg '\d+'` and notice that `rg` finds the digit sequence `404`. Now use `rg 'ERROR' sample/log.txt` to find all error lines directly from a file — `rg` works like `grep` but uses extended regular expressions by default.

2. Use `rg -o '\d+' sample/data.txt > all_numbers` to extract every sequence of digits from the data file. The `\d` matches any digit and `+` means one or more. The `-o` flag outputs only the matched parts, one per line.

3. Use `rg '\w+@\w+\.\w+' sample/emails.txt > valid_emails` to find all lines matching a simple email pattern: one or more word characters, an `@`, one or more word characters, a literal dot, and one or more word characters. The `\w` class matches letters, digits and underscores.

4. Use `rg 'colou?r' sample/words.txt > col_words` to find both `color` and `colour`. The `?` makes the preceding `u` optional, matching zero or one occurrence.

5. Use `rg 'gr[ae]y' sample/words.txt > grays` to find both `gray` and `grey`. The character set `[ae]` matches either `a` or `e`.

6. Use `rg -o '\w+\s\w+$' sample/log.txt > messages` to extract the two-word message at the end of each log line. Here `\w+` matches a word, `\s` matches the whitespace between them, and `$` anchors the match at the end of the line.

7. Use `rg -o '(\w+)@\w+\.\w+' -r '$1' sample/emails.txt > usernames` to extract just the username from each email address. The parentheses `(...)` create a capture group around the first `\w+`, and `-r '$1'` replaces the entire match with only the captured part.

8. Use `rg` with the `-o` flag and `\d` to extract only the dates (in `YYYY-MM-DD` format) from `sample/log.txt`. Save them to a file called `dates`.

9. Use `rg` with `-o` to extract only the times (in `HH:MM` format) from `sample/log.txt`. Save them to a file called `times`.

10. Use `rg` with a capture group and `-r '$1'` to extract only the domain names (like `example.com`) from each email address in `sample/emails.txt`. Save the result to `domains`.

# Check

2. Verify that the file `all_numbers` exists and contains `1001`, `25`, `1002`, `130`, `1003`, `8`, `2001`, `55`, `2002` and `200` (one per line, in this order).

3. Verify that the file `valid_emails` exists and contains `alice@example.com`, `bob@mail.org`, `carol@server.net`, `dan99@example.com`, `frank@mail.org` and `grace@example.com` (one per line, in this order).

4. Verify that the file `col_words` exists and contains `color` and `colour` (one per line, in this order).

5. Verify that the file `grays` exists and contains `gray` and `grey` (one per line, in this order).

6. Verify that the file `messages` exists and contains `server started`, `disk full`, `low memory`, `user login`, `connection timeout` and `backup done` (one per line, in this order).

7. Verify that the file `usernames` exists and contains `alice`, `bob`, `carol`, `dan99`, `frank` and `grace` (one per line, in this order).

8. Verify that the file `dates` exists and contains `2024-01-15`, `2024-01-15`, `2024-02-20`, `2024-02-20`, `2024-03-01` and `2024-03-01` (one per line, in this order).

9. Verify that the file `times` exists and contains `10:30`, `10:31`, `14:00`, `14:05`, `09:00` and `09:15` (one per line, in this order).

10. Verify that the file `domains` exists and contains `example.com`, `mail.org`, `server.net`, `example.com`, `mail.org` and `example.com` (one per line, in this order).
