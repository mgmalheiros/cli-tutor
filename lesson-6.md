# Lesson

This lesson covers text manipulation tools: `wc` counts lines, words and characters; `sort` orders lines alphabetically; `uniq` removes adjacent duplicate lines; `grep` finds lines that contain a given string; and `diff` shows the differences between two files. The pipe operator `|` connects the output of one command to the input of the next, allowing you to combine tools. The `nano` text editor lets you edit files interactively.

# Setup

Create a folder called `sample` inside the lesson folder with the following files:

- `fruits.txt` (one item per line: `banana`, `apple`, `cherry`, `banana`, `melon`, `apple`, `kiwi`, `lemon`, `banana`, `cherry`)
- `log.txt` (one entry per line: `INFO server started`, `ERROR connection failed`, `INFO user logged in`, `WARNING disk space low`, `ERROR timeout occurred`, `INFO backup complete`, `WARNING high memory usage`, `ERROR file not found`, `INFO server stopped`)
- `original.txt` (one item per line: `apple`, `banana`, `cherry`, `melon`, `kiwi`)
- `revised.txt` (one item per line: `apple`, `blueberry`, `cherry`, `dragonfruit`, `kiwi`)
- `animals.txt` (one entry per line: `dog mammal`, `cat mammal`, `eagle bird`, `salmon fish`, `frog amphibian`, `cat mammal`, `dog mammal`, `parrot bird`, `trout fish`, `dog mammal`)

# Tasks

1. Enter the lesson folder. Use `wc sample/fruits.txt` to see three numbers: line count, word count and character count. Then try `wc -l sample/fruits.txt` for only the line count, `wc -w` for words and `wc -c` for characters.

2. Use `sort sample/fruits.txt > sorted_fruits` to sort the fruits alphabetically and save the result. Use `cat sorted_fruits` to verify. Notice that duplicate entries now appear next to each other.

3. Use `grep "cherry" sample/fruits.txt > found_cherry` to find all lines containing the string "cherry" and save them to a file.

4. Use `diff sample/original.txt sample/revised.txt` to compare the two files. Notice how `diff` marks lines that differ: `<` for lines only in the first file and `>` for lines only in the second.

5. Use `grep -v "INFO" sample/log.txt > no_info` to find all lines that do *not* contain "INFO" and save them. The `-v` flag inverts the match condition, showing only non-matching lines.

6. Use `diff sample/original.txt sample/revised.txt > changes` to save the diff output into a file for later reference.

7. Use `sort sample/fruits.txt | uniq > unique_fruits` to sort the fruits and then remove duplicate lines. The `|` (pipe) sends the output of `sort` as input to `uniq`. Note that `uniq` only removes *adjacent* duplicates, which is why `sort` must come first.

8. Use `grep "ERROR" sample/log.txt | sort -r > sorted_errors` to extract all error lines and then sort them in reverse alphabetical order (using the `-r` flag).

9. Use `tail -5 sample/log.txt | grep "INFO" > recent_info` to first get the last five log entries, then filter only the ones containing "INFO".

10. Use `grep "mammal" sample/animals.txt | sort | uniq > mammals` to find all mammal entries, sort them and remove duplicates. This chains three commands together using two pipes.

11. Copy the original file with `cat sample/original.txt > fixed`. Then open it with `nano fixed` and manually edit it so that its contents match `sample/revised.txt`: change `banana` to `blueberry` and `melon` to `dragonfruit`. Save with **Ctrl+O**, confirm the filename with **Enter**, and exit with **Ctrl+X**.

12. Build a file by appending pipe results. First run `grep "bird" sample/animals.txt | sort | uniq > wildlife`. Then run `grep "fish" sample/animals.txt | sort | uniq >> wildlife`. Use `cat wildlife` to verify it contains the bird entries followed by the fish entries.


# Check

2. Verify that the file `sorted_fruits` exists and contains `apple`, `apple`, `banana`, `banana`, `banana`, `cherry`, `cherry`, `kiwi`, `lemon` and `melon` (one per line, in this order).

3. Verify that the file `found_cherry` exists and contains `cherry` and `cherry` (two lines).

5. Verify that the file `no_info` exists and contains `ERROR connection failed`, `WARNING disk space low`, `ERROR timeout occurred`, `WARNING high memory usage` and `ERROR file not found` (one per line, in this order).

6. Verify that the file `changes` exists and contains the diff output: `2c2`, `< banana`, `---`, `> blueberry`, `4c4`, `< melon`, `---` and `> dragonfruit` (one per line, in this order).

7. Verify that the file `unique_fruits` exists and contains `apple`, `banana`, `cherry`, `kiwi`, `lemon` and `melon` (one per line, in this order).

8. Verify that the file `sorted_errors` exists and contains `ERROR timeout occurred`, `ERROR file not found` and `ERROR connection failed` (one per line, in this order).

9. Verify that the file `recent_info` exists and contains `INFO backup complete` and `INFO server stopped` (two lines, in this order).

10. Verify that the file `mammals` exists and contains `cat mammal` and `dog mammal` (two lines, in this order).

11. Verify that the file `fixed` exists and contains `apple`, `blueberry`, `cherry`, `dragonfruit` and `kiwi` (one per line, in this order).

12. Verify that the file `wildlife` exists and contains `eagle bird`, `parrot bird`, `salmon fish` and `trout fish` (one per line, in this order).
