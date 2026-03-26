#!/usr/bin/env python3
"""Lição 2: navegação de pastas com ls, cd, pwd, mkdir e rmdir."""

import os

import base

# ── Conteúdo da lição ───────────────────────────────────────────────────────

LESSON_NUMBER = 2

LESSON_TEXT = (
    "Esta lição aborda a navegação de pastas usando os comandos "
    "`ls`, `cd`, `pwd`, "
    "`mkdir` e `rmdir`. Também apresenta "
    "os símbolos especiais de pasta `/`, "
    "`.`, `..` e `~`."
)

TASKS = [
    "Execute `pwd` para ver seu diretório atual. Depois "
    "execute `ls` para listar o conteúdo.",

    "Use `cd` para entrar na pasta da lição. Confirme que "
    "está dentro dela com `pwd`.",

    "Dentro da pasta da lição, crie uma subpasta chamada "
    "`alpha` usando `mkdir alpha`. Verifique "
    "que ela existe com `ls`.",

    "Entre em `alpha` usando `cd alpha`. Depois "
    "volte para a pasta da lição usando `cd ..`, e confirme "
    "com `pwd`.",

    "Use `mkdir -p beta/gamma` para criar uma estrutura de "
    "pastas aninhadas. Depois use `ls beta` para verificar "
    "que `gamma` foi criada dentro de `beta`.",

    "Entre em `beta/gamma`. Dica: digite `cd ` "
    "e depois **TAB**, adicionando novas letras e pressionando "
    "**TAB** novamente. Quando estiver dentro de "
    "`gamma`, use `cd ../..` para voltar à "
    "pasta da lição. Confirme com `pwd`.",

    "A partir da pasta da lição, use `cd ~` para ir ao seu "
    "diretório pessoal. Confirme com `pwd`. Depois retorne "
    "manualmente à pasta da lição.",

    "Dentro da pasta da lição, crie uma pasta chamada "
    "`delta` e use "
    "`echo hello > delta/greeting` para criar um arquivo "
    "dentro dela. Verifique que o arquivo existe com "
    "`ls delta`.",

    "Na pasta da lição, crie uma pasta chamada `empty` "
    "usando `mkdir empty`. Depois remova-a usando "
    "`rmdir empty`. Verifique que ela foi removida com "
    "`ls`.",

    "Novamente na pasta da lição, crie a seguinte estrutura: uma pasta "
    "`docs` contendo uma subpasta `drafts`, "
    "e um arquivo `docs/readme` com o conteúdo "
    "`project notes`. Use `mkdir -p` e "
    "`echo` com redirecionamento (`>`).",
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
