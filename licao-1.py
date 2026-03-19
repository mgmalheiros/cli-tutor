#!/usr/bin/env python3
"""Lição 1: comandos básicos date, echo, man e clear."""

import os

import base

# ── Conteúdo da lição ───────────────────────────────────────────────────────

LESSON_NUMBER = 1

LESSON_TEXT = (
    "Esta lição aborda os comandos básicos {code}`date`{/code}, "
    "{code}`echo`{/code}, {code}`man`{/code} e {code}`clear`{/code}. "
    "Também apresenta os principais atalhos de edição, o histórico do "
    "shell e a completação com {bold}TAB{/bold}."
)

TASKS = [
    "Use o comando {code}`date`{/code}. Depois use o comando "
    "{code}`date +%Y-%m-%d`{/code}. Por fim, veja as opções "
    "com {code}`date --help`{/code}.",

    "Use o comando {code}`echo`{/code}. Depois use o comando "
    "{code}`echo test`{/code}. Por fim, experimente o comando "
    "{code}`echo test > file`{/code}. O que aconteceu?",

    "Use o comando {code}`man`{/code}. Depois use o comando "
    "{code}`man echo`{/code} (use a tecla {bold}Q{/bold} para sair). "
    "Por fim, experimente {code}`man date`{/code}.",

    "Use a tecla {bold}UP{/bold} para voltar no histórico e a tecla "
    "{bold}ENTER{/bold} para executar o comando atual. Teste também "
    "a tecla {bold}DOWN{/bold}.",

    "Teste outras teclas como {bold}LEFT{/bold}, {bold}RIGHT{/bold}, "
    "{bold}BACKSPACE{/bold}.",

    "Use o comando {code}`clear`{/code}. Depois repita um comando anterior. "
    "Agora experimente o atalho {bold}CONTROL+L{/bold}.",

    "Agora apenas digite {code}`man`{/code} mas não pressione "
    "{bold}ENTER{/bold}. Em vez disso, pressione a tecla {bold}TAB{/bold} "
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
