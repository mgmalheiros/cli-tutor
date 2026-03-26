# Lesson

This lesson covers shell **globs** and **wildcards**: `*` matches any number of characters, `?` matches exactly one character, `[...]` matches a set or range of characters and `{a,b,c}` expands into multiple alternatives. These patterns let you work with many files at once.

# Setup

Create a folder called `sample` inside the lesson folder with the following files:

- `note1.txt`, `note2.txt`, `note3.txt` (contents: `note one`, `note two`, `note three`)
- `note10.txt` (contents: `note ten`)
- `report.txt` (contents: `final report`)
- `report.csv` (contents: `a,b,c`)
- `data.csv` (contents: `1,2,3`)
- `README` (contents: `read me`)
- `image.png` (contents from `files/image.png`, bundled with lesson program using base64)
- `logo.svg` (contents from `files/logo.svg`, bundled with lesson program)

# Tasks

1. Use `cd` to enter the lesson folder. Then run `ls sample/*.txt` to list all `.txt` files inside `sample`. The `*` matches any number of characters.

2. Run `ls sample/*.csv` to list all `.csv` files. Then try `ls sample/*.*` to list all files that have an extension. Notice that `README` is not listed because it has no dot.

3. Run `ls sample/note?.txt` to list files matching `note` followed by exactly one character and `.txt`. Notice that `note10.txt` is not listed because `?` matches only a single character.

4. Run `ls sample/note[13].txt` to list only `note1.txt` and `note3.txt`. The `[...]` pattern matches any single character from the given set.

5. Go to the `sample` folder and then run `ls note[1-3].txt` to list `note1.txt`, `note2.txt` and `note3.txt`. Inside `[...]`, a hyphen defines a range of characters.

6. Inside the `sample` folder run `ls {report,data}.csv` to list `report.csv` and `data.csv`. The `{a,b}` syntax expands into separate words.

7. In the lesson folder, use `ls sample/*.txt > txt_list` to save the list of all `.txt` files from `sample` into a file called `txt_list`.

8. Go to the `sample` folder and use `ls ?????.*` to list all files whose name (before the extension) is exactly five characters long. Save the result into a file called `../five_chars` using redirection.

# Check

7. Verify that the file `txt_list` exists and contains 'sample/note10.txt', 'sample/note1.txt', 'sample/note2.txt', 'sample/note3.txt' and 'sample/report.txt'.

8. Verify that the file `five_chars` exists and contains 'image.png', 'note1.txt', 'note2.txt' and 'note3.txt'.
