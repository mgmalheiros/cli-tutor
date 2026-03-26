#!/usr/bin/env python3
"""Lição 1: comandos básicos date, echo, man e clear."""

import os

import base

# ── Conteúdo da lição ───────────────────────────────────────────────────────

LESSON_NUMBER = 1

LESSON_TEXT = (
    "Esta lição aborda os comandos básicos `date`, "
    "`echo`, `man` e `clear`. "
    "Também apresenta os principais atalhos de edição, o histórico do "
    "shell e a completação com **TAB**."
)

TASKS = [
    "Use o comando `date`. Depois use o comando "
    "`date +%Y-%m-%d`. Por fim, veja as opções "
    "com `date --help`.",

    "Use o comando `echo`. Depois use o comando "
    "`echo test`. Por fim, experimente o comando "
    "`echo test > file`. O que aconteceu?",

    "Use o comando `man`. Depois use o comando "
    "`man echo` (use a tecla **Q** para sair). "
    "Por fim, experimente `man date`.",

    "Use a tecla **UP** para voltar no histórico e a tecla "
    "**ENTER** para executar o comando atual. Teste também "
    "a tecla **DOWN**.",

    "Teste outras teclas como **LEFT**, **RIGHT**, "
    "**BACKSPACE**.",

    "Use o comando `clear`. Depois repita um comando anterior. "
    "Agora experimente o atalho **CONTROL+L**.",

    "Agora apenas digite `man` mas não pressione "
    "**ENTER**. Em vez disso, pressione a tecla **TAB** "
    "duas vezes. O que aconteceu?",
]


# ── Verificações ────────────────────────────────────────────────────────────

def get_checks(folder):
    return [
        ("Tarefa 2: arquivo 'file' existe com conteúdo 'test'",
         lambda: base.check_file_contents(os.path.join(folder, "file"), "test",
                                          lang='pt')),
    ]


# ── Main ────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    base.lesson_main(LESSON_NUMBER, LESSON_TEXT, TASKS, get_checks, lang='pt')
