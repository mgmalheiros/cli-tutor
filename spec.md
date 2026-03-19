This is a program for student self-checking. The goal is to learn command-line tools.

Create a `lesson-1.py` with the following features, based on the matching `lesson-1.md` file which describes this lesson.

- The program must be self-contained, that is, it cannot use any features outside the standard Python library.

- When just run it has to present the introductory text found in section **Lesson**, with adequate ANSI markings for the Markdown styles. It also must show the program command-line commands.

- The program has a command `setup` that creates a new folder with name `folder-1-N`, where `1` is the lesson number and `N` goes from `a` to `z`. It should first check whether such folders exists, and then create a new one, showing the according message. If there are any further setup instructions in the **Setup** section, they need to be executed inside the newly created folder. If this section is empty, only the folder should be created.

- The program has a command line command `tasks` that shows all defined tasks, pretty printed.

- The program has a command line command `task N` which shows the specified task, also pretty printed. When there is no such task, it shows an error message. Tasks start at 1, matching the numbers at the lesson.

- The program has a command line command `check` that validates a folder with the same name structure `folder-?`. If no one is found, a message is shown. If more than one folder is found, the latest one is selected. It then shows a message `checking folder <name>...` and proceeds running the verification tests found in the **Check** section. Not all tasks need to have a check. If all checks are passed, it should exhibit a message stating this and how many were checked. For each check that fails, an error message is shown.

- The `check` command should utilize shared and generic testing functions like the ones described below, implemented at `base.py`. More can be added as needed. All should return a tuple of `(passed: bool, message: str)`. All functions need to have a `lang='en'` parameter, printing and returning English messages by default, otherwise providing matching Portuguese messages.

- For the ANSI rendering of Markdown, there is only need to handle italics, bold and code styles.

# Initial testing functions

- a given empty `folder` exists
- a given `folder` does not exist
- a given `folder` exists and has the specified `list of files`

- a given empty `file` exists
- a given `file` does not exist
- a given `file` exists and has the specified `contents` (ignore trailing spaces at the end of each line and a trailing newline at EOF when comparing)
- a given `file` exists, is executable and when run with the given `arguments` produces the specified `output` as the standard output
