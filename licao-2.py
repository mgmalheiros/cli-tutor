#!/usr/bin/env python3
"""Lição 2: navegação de pastas com ls, cd, pwd, mkdir e rmdir."""

import os

import base

# ── Conteúdo da lição ───────────────────────────────────────────────────────

LESSON_NUMBER = 2

LESSON_TEXT = (
    "Esta lição aborda a navegação de pastas usando os comandos "
    "{code}`ls`{/code}, {code}`cd`{/code}, {code}`pwd`{/code}, "
    "{code}`mkdir`{/code} e {code}`rmdir`{/code}. Também apresenta "
    "os símbolos especiais de pasta {code}`/`{/code}, "
    "{code}`.`{/code}, {code}`..`{/code} e {code}`~`{/code}."
)

TASKS = [
    "Execute {code}`pwd`{/code} para ver seu diretório atual. Depois "
    "execute {code}`ls`{/code} para listar o conteúdo.",

    "Use {code}`cd`{/code} para entrar na pasta da lição. Confirme que "
    "está dentro dela com {code}`pwd`{/code}.",

    "Dentro da pasta da lição, crie uma subpasta chamada "
    "{code}`alpha`{/code} usando {code}`mkdir alpha`{/code}. Verifique "
    "que ela existe com {code}`ls`{/code}.",

    "Entre em {code}`alpha`{/code} usando {code}`cd alpha`{/code}. Depois "
    "volte para a pasta da lição usando {code}`cd ..`{/code}, e confirme "
    "com {code}`pwd`{/code}.",

    "Use {code}`mkdir -p beta/gamma`{/code} para criar uma estrutura de "
    "pastas aninhadas. Depois use {code}`ls beta`{/code} para verificar "
    "que {code}`gamma`{/code} foi criada dentro de {code}`beta`{/code}.",

    "Entre em {code}`beta/gamma`{/code}. Dica: digite {code}`cd `{/code} "
    "e depois {bold}TAB{/bold}, adicionando novas letras e pressionando "
    "{bold}TAB{/bold} novamente. Quando estiver dentro de "
    "{code}`gamma`{/code}, use {code}`cd ../..`{/code} para voltar à "
    "pasta da lição. Confirme com {code}`pwd`{/code}.",

    "A partir da pasta da lição, use {code}`cd ~`{/code} para ir ao seu "
    "diretório pessoal. Confirme com {code}`pwd`{/code}. Depois retorne "
    "manualmente à pasta da lição.",

    "Dentro da pasta da lição, crie uma pasta chamada "
    "{code}`delta`{/code} e use "
    "{code}`echo hello > delta/greeting`{/code} para criar um arquivo "
    "dentro dela. Verifique que o arquivo existe com "
    "{code}`ls delta`{/code}.",

    "Na pasta da lição, crie uma pasta chamada {code}`empty`{/code} "
    "usando {code}`mkdir empty`{/code}. Depois remova-a usando "
    "{code}`rmdir empty`{/code}. Verifique que ela foi removida com "
    "{code}`ls`{/code}.",

    "Novamente na pasta da lição, crie a seguinte estrutura: uma pasta "
    "{code}`docs`{/code} contendo uma subpasta {code}`drafts`{/code}, "
    "e um arquivo {code}`docs/readme`{/code} com o conteúdo "
    "{code}`project notes`{/code}. Use {code}`mkdir -p`{/code} e "
    "{code}`echo`{/code} com redirecionamento ({code}`>`{/code}).",
]


# ── Verificações ────────────────────────────────────────────────────────────

def get_checks(folder):
    return [
        ("Tarefa 3: pasta 'alpha' existe e está vazia",
         lambda: base.check_empty_folder_exists(os.path.join(folder, "alpha"),
                                                lang='pt')),

        ("Tarefa 5: pasta 'beta/gamma' existe e está vazia",
         lambda: base.check_empty_folder_exists(os.path.join(folder, "beta", "gamma"),
                                                lang='pt')),

        ("Tarefa 8: arquivo 'delta/greeting' existe com conteúdo 'hello'",
         lambda: base.check_file_contents(os.path.join(folder, "delta", "greeting"),
                                          "hello", lang='pt')),

        ("Tarefa 9: pasta 'empty' não existe",
         lambda: base.check_folder_not_exists(os.path.join(folder, "empty"),
                                              lang='pt')),

        ("Tarefa 10: pasta 'docs/drafts' existe e está vazia",
         lambda: base.check_empty_folder_exists(os.path.join(folder, "docs", "drafts"),
                                                lang='pt')),

        ("Tarefa 10: arquivo 'docs/readme' existe com conteúdo 'project notes'",
         lambda: base.check_file_contents(os.path.join(folder, "docs", "readme"),
                                          "project notes", lang='pt')),
    ]


# ── Main ────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    base.lesson_main(LESSON_NUMBER, LESSON_TEXT, TASKS, get_checks, lang='pt')
