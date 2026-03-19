# Lesson

This lesson explores the `$PATH` variable, the `which` command, and the main system folders. It also introduces the `ls -a` and `ls -la` flags for listing hidden files and detailed information.

# Setup

# Tasks

1. Run `echo $PATH` to see the list of directories where the shell looks for commands. Notice that directories are separated by `:`.

2. Use `which date` to find out where the `date` command is located. Then try `which echo` and `which man`.

3. Use `ls /bin` to list the contents of the `/bin` folder. Then try `ls /usr/bin`. These are the main system folders where commands live.

4. Pick one command from the `/bin` listing and use `man` to read its manual page (use the **Q** key to quit). For example, `man cat` or `man cp`.

5. Inside the lesson folder, use `echo $PATH > my_path` to save your current `$PATH` into a file called `my_path`.

6. Run `ls -a` inside the lesson folder. Notice that it shows entries starting with `.`, which are normally hidden. The `.` entry is the current folder and `..` is the parent folder.

7. Run `ls -la` inside the lesson folder. Compare the output with plain `ls`. The `-l` flag shows permissions, owner, size and date for each entry.

8. Use `which` to find where `ls` is located. Then run `ls -la` on that exact path to see its permissions and size. For example, if `which ls` shows `/usr/bin/ls`, run `ls -la /usr/bin/ls`.

9. Inside the lesson folder, create a file called `visible` using `echo public > visible`. Then create a hidden file called `.hidden` using `echo secret > .hidden`. Run `ls` and then `ls -a` to see the difference.

10. Again in the lesson folder, run the command `ls -la / > listing` and then inspect (by using a text editor) the contents of the `listing` file.

# Check

5. Verify that the file `my_path` exists and is not empty.

9. Verify that the file `visible` exists and contains `public`. Verify that the file `.hidden` exists and contains `secret`.

10. Verify that the file `listing` exists and is not empty.
