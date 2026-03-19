"""Shared testing functions for CLI tutor lessons."""

import os
import subprocess


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
