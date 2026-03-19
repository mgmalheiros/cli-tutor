"""Shared testing functions and lesson engine for CLI tutor lessons."""

import glob
import os
import re
import string
import subprocess
import sys


# ── ANSI helpers ────────────────────────────────────────────────────────────

BOLD = "\033[1m"
ITALIC = "\033[3m"
CODE = "\033[36m"  # cyan for inline code
GREEN = "\033[32m"
RED = "\033[31m"
RESET = "\033[0m"


def render(text):
    """Convert markup to ANSI sequences.

    Supported markers:
      {bold}...{/bold}     → bold
      {italic}...{/italic} → italic
      {code}...{/code}     → cyan
      `...`                → cyan (backticks)
    """
    text = text.replace("{bold}", BOLD).replace("{/bold}", RESET)
    text = text.replace("{italic}", ITALIC).replace("{/italic}", RESET)
    text = text.replace("{code}", CODE).replace("{/code}", RESET)
    text = re.sub(r'`([^`]+)`', CODE + r'\1' + RESET, text)
    return text


# ── Folder naming helpers ───────────────────────────────────────────────────

def find_folders(lesson_number):
    """Return sorted list of existing folder-N-? directories."""
    return sorted(glob.glob(f"folder-{lesson_number}-[a-z]"))


def next_folder_name(lesson_number):
    """Return the next available folder-N-? name, or None if exhausted."""
    existing = {os.path.basename(f) for f in find_folders(lesson_number)}
    for ch in string.ascii_lowercase:
        name = f"folder-{lesson_number}-{ch}"
        if name not in existing:
            return name
    return None


# ── Lesson engine ───────────────────────────────────────────────────────────

def run_checks(folder, checks):
    """Run a list of (description, check_fn) tuples and print results."""
    passed = 0
    failed = 0
    for desc, fn in checks:
        ok, msg = fn()
        if ok:
            passed += 1
            print(f"  {BOLD}{GREEN}✓{RESET} {desc}")
        else:
            failed += 1
            print(f"  {BOLD}{RED}✗{RESET} {desc}")
            print(f"    {msg}")

    total = passed + failed
    if failed == 0:
        print(f"\nAll checks passed ({total}/{total}).")
    else:
        print(f"\n{passed}/{total} checks passed, {failed} failed.")
        sys.exit(1)


def lesson_main(lesson_number, lesson_text, tasks, get_checks):
    """Generic CLI entry point for a lesson.

    get_checks is a callable that receives the folder path and returns
    a list of (description, check_fn) tuples.
    """
    args = sys.argv[1:]
    script = os.path.basename(sys.argv[0])

    if not args:
        print(render(lesson_text))
        print()
        print("Commands:")
        print("  setup    Create a new practice folder")
        print("  tasks    Show all tasks")
        print("  task N   Show task N")
        print("  check    Check your work")
    elif args[0] == "setup":
        name = next_folder_name(lesson_number)
        if name is None:
            print("All folder slots (a-z) are taken.")
            sys.exit(1)
        os.makedirs(name)
        print(f"Created {name}")
    elif args[0] == "tasks":
        for i, task in enumerate(tasks, 1):
            print(render(f"{BOLD}{i}.{RESET} {task}"))
            if i < len(tasks):
                print()
    elif args[0] == "task":
        if len(args) < 2:
            print(f"Usage: {script} task N")
            sys.exit(1)
        try:
            n = int(args[1])
        except ValueError:
            print(f"Error: '{args[1]}' is not a valid task number.")
            sys.exit(1)
        if n < 1 or n > len(tasks):
            print(f"Error: task {n} does not exist. Valid range: 1-{len(tasks)}.")
            sys.exit(1)
        print(render(f"{BOLD}{n}.{RESET} {tasks[n - 1]}"))
    elif args[0] == "check":
        folders = find_folders(lesson_number)
        if not folders:
            print("No folder found. Run 'setup' first.")
            sys.exit(1)
        folder = folders[-1]
        print(f"Checking folder {folder}...")
        run_checks(folder, get_checks(folder))
    else:
        print(f"Unknown command: {args[0]}")
        print("Available commands: setup, tasks, task N, check")
        sys.exit(1)


def check_empty_folder_exists(folder, lang='en'):
    """Check that a given empty folder exists."""
    if not os.path.isdir(folder):
        if lang == 'pt':
            return False, f"A pasta '{folder}' não existe."
        return False, f"Folder '{folder}' does not exist."
    contents = os.listdir(folder)
    if contents:
        if lang == 'pt':
            return False, f"A pasta '{folder}' existe mas não está vazia (contém {len(contents)} item(s))."
        return False, f"Folder '{folder}' exists but is not empty (contains {len(contents)} item(s))."
    if lang == 'pt':
        return True, f"A pasta '{folder}' existe e está vazia."
    return True, f"Folder '{folder}' exists and is empty."


def check_folder_has_files(folder, file_list, lang='en'):
    """Check that a given folder exists and has the specified list of files."""
    if not os.path.isdir(folder):
        if lang == 'pt':
            return False, f"A pasta '{folder}' não existe."
        return False, f"Folder '{folder}' does not exist."
    for fname in file_list:
        fpath = os.path.join(folder, fname)
        if not os.path.isfile(fpath):
            if lang == 'pt':
                return False, f"O arquivo '{fname}' não foi encontrado na pasta '{folder}'."
            return False, f"File '{fname}' not found in folder '{folder}'."
    if lang == 'pt':
        return True, f"A pasta '{folder}' contém todos os arquivos esperados."
    return True, f"Folder '{folder}' contains all expected files."


def check_folder_not_exists(folder, lang='en'):
    """Check that a given folder does not exist."""
    if os.path.isdir(folder):
        if lang == 'pt':
            return False, f"A pasta '{folder}' ainda existe."
        return False, f"Folder '{folder}' still exists."
    if lang == 'pt':
        return True, f"A pasta '{folder}' não existe."
    return True, f"Folder '{folder}' does not exist."


def check_file_not_exists(filepath, lang='en'):
    """Check that a given file does not exist."""
    if os.path.isfile(filepath):
        if lang == 'pt':
            return False, f"O arquivo '{filepath}' ainda existe."
        return False, f"File '{filepath}' still exists."
    if lang == 'pt':
        return True, f"O arquivo '{filepath}' não existe."
    return True, f"File '{filepath}' does not exist."


def check_empty_file_exists(filepath, lang='en'):
    """Check that a given empty file exists."""
    if not os.path.isfile(filepath):
        if lang == 'pt':
            return False, f"O arquivo '{filepath}' não existe."
        return False, f"File '{filepath}' does not exist."
    if os.path.getsize(filepath) != 0:
        if lang == 'pt':
            return False, f"O arquivo '{filepath}' existe mas não está vazio."
        return False, f"File '{filepath}' exists but is not empty."
    if lang == 'pt':
        return True, f"O arquivo '{filepath}' existe e está vazio."
    return True, f"File '{filepath}' exists and is empty."


def _normalize(text):
    """Strip trailing whitespace from each line and trailing newline at EOF."""
    lines = text.split('\n')
    lines = [line.rstrip() for line in lines]
    # Remove trailing empty lines
    while lines and lines[-1] == '':
        lines.pop()
    return '\n'.join(lines)


def check_file_contents(filepath, expected, lang='en'):
    """Check that a given file exists and has the specified contents."""
    if not os.path.isfile(filepath):
        if lang == 'pt':
            return False, f"O arquivo '{filepath}' não existe."
        return False, f"File '{filepath}' does not exist."
    with open(filepath, 'r') as f:
        actual = f.read()
    if _normalize(actual) != _normalize(expected):
        if lang == 'pt':
            return False, f"O conteúdo do arquivo '{filepath}' não corresponde ao valor esperado."
        return False, f"File '{filepath}' contents do not match expected value."
    if lang == 'pt':
        return True, f"O arquivo '{filepath}' tem o conteúdo esperado."
    return True, f"File '{filepath}' has the expected contents."


def check_executable_output(filepath, arguments, expected_output, lang='en'):
    """Check that a file exists, is executable, and produces the expected stdout."""
    if not os.path.isfile(filepath):
        if lang == 'pt':
            return False, f"O arquivo '{filepath}' não existe."
        return False, f"File '{filepath}' does not exist."
    if not os.access(filepath, os.X_OK):
        if lang == 'pt':
            return False, f"O arquivo '{filepath}' não é executável."
        return False, f"File '{filepath}' is not executable."
    try:
        result = subprocess.run(
            [filepath] + arguments,
            capture_output=True, text=True, timeout=10
        )
    except subprocess.TimeoutExpired:
        if lang == 'pt':
            return False, f"A execução de '{filepath}' expirou."
        return False, f"Running '{filepath}' timed out."
    except Exception as e:
        if lang == 'pt':
            return False, f"Erro ao executar '{filepath}': {e}"
        return False, f"Error running '{filepath}': {e}"
    if _normalize(result.stdout) != _normalize(expected_output):
        if lang == 'pt':
            return False, f"A saída de '{filepath}' não corresponde ao valor esperado."
        return False, f"Output of '{filepath}' does not match expected value."
    if lang == 'pt':
        return True, f"O arquivo '{filepath}' produziu a saída esperada."
    return True, f"File '{filepath}' produced the expected output."
