# Lesson

This lesson covers basic text manipulation using the commands `cat`, `head` and `tail`, and the append redirection `>>`. The `cat` command displays or concatenates files, `head` shows the first lines and `tail` shows the last lines. The `>>` operator appends to a file instead of overwriting it.

# Setup

Create a folder called `sample` inside the lesson folder with the following files:

- `colors.txt` (one color per line: `red`, `orange`, `yellow`, `green`, `blue`, `indigo`, `violet`)
- `numbers.txt` (one number per line: `one`, `two`, `three`, `four`, `five`, `six`, `seven`, `eight`, `nine`, `ten`)
- `greeting.txt` (contents: `hello world`)
- `farewell.txt` (contents: `goodbye world`)

# Tasks

1. Enter the lesson folder. Use `cat sample/colors.txt` to display the colors file. Notice that the contents are shown in the terminal.

2. Use `head sample/numbers.txt` to see the first 10 lines (the default). Since the file has exactly 10 lines, you see all of them. Now try `head -3 sample/numbers.txt` to see only the first 3 lines.

3. Use `tail sample/numbers.txt` to see the last 10 lines. Now try `tail -4 sample/numbers.txt` to see only the last 4 lines.

4. Use `head -3 sample/colors.txt > warm` to save the first 3 colors (the warm ones) into a new file called `warm`.

5. Use `tail -3 sample/colors.txt > cool` to save the last 3 colors (the cool ones) into a new file called `cool`.

6. In the lesson folder, use `echo`, `>` and `>>` to build a file line by line. Run `echo first > lines`, then `echo second >> lines`, then `echo third >> lines`. Use `cat lines` to verify. Notice that `>` creates (or overwrites) while `>>` appends.

7. Inside the `sample` folder, use `cat` to concatenate two files into one: `cat greeting.txt farewell.txt > ../combined`. Then use `cat ../combined` to verify it contains both lines.

8. Use `head -1 sample/numbers.txt > first_last` and then `tail -1 sample/numbers.txt >> first_last` to create a file with only the first and last lines of the numbers file.

9. Use `head -5 sample/numbers.txt > top5` and then `tail -3 top5 > middle` to extract lines 3, 4 and 5 from the numbers file into a file called `middle`.

10. Create a file called `summary` that contains the first 2 colors, then a separator line `- - -`, then the last 2 colors. Use `head`, `tail`, `echo` and the `>` and `>>` operators.

# Check

4. Verify that the file `warm` exists and contains `red`, `orange` and `yellow` (one per line).

5. Verify that the file `cool` exists and contains `blue`, `indigo` and `violet` (one per line).

6. Verify that the file `lines` exists and contains `first`, `second` and `third` (one per line).

7. Verify that the file `combined` exists and contains `hello world` and `goodbye world` (one per line).

8. Verify that the file `first_last` exists and contains `one` and `ten` (one per line).

9. Verify that the file `middle` exists and contains `three`, `four` and `five` (one per line).

10. Verify that the file `summary` exists and contains `red`, `orange`, `- - -`, `indigo` and `violet` (one per line).
