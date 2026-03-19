# Lesson

This lesson covers folder navigation using the commands `ls`, `cd`, `pwd`, `mkdir` and `rmdir`. It also introduces the special folder names `/`, `~`, `.` and `..`.

# Setup

# Tasks

1. Run `pwd` to see your current directory. Then run `ls` to list its contents.

2. Use `cd` to enter the lesson folder. Confirm you are inside it with `pwd`.

3. Inside the lesson folder, create a subfolder called `alpha` using `mkdir alpha`. Verify it exists with `ls`.

4. Navigate into `alpha` using `cd alpha`. Then go back to the lesson folder using `cd ..`. Confirm with `pwd`.

5. Use `mkdir -p beta/gamma` to create a nested folder structure. Then use `ls beta` to verify that `gamma` was created inside `beta`.

6. Navigate into `beta/gamma`. From there, use `cd ../..` to return to the lesson folder. Confirm with `pwd`.

7. From the lesson folder, use `cd ~` to go to your home directory. Then use `cd -` to return to the lesson folder. Confirm with `pwd`.

8. Inside the lesson folder, create a folder called `delta` and use `echo hello > delta/greeting` to create a file inside it. Verify the file exists with `ls delta`.

9. Create a folder called `empty` using `mkdir empty`. Then remove it using `rmdir empty`. Verify it is gone with `ls`.

10. Create the following structure: a folder `docs` containing a subfolder `drafts`, and a file `docs/readme` with the content `project notes`. Use `mkdir -p` and `echo` with redirection.

# Check

3. Verify that the folder `alpha` exists and is empty.

5. Verify that the folder `beta/gamma` exists and is empty.

8. Verify that the file `delta/greeting` exists and contains `hello`.

9. Verify that the folder `empty` does not exist.

10. Verify that the folder `docs/drafts` exists and is empty. Verify that the file `docs/readme` exists and contains `project notes`.
