#!/usr/bin/env python3
"""Lição 3: $PATH, which, pastas do sistema e flags do ls."""

import os

import base

# ── Conteúdo da lição ───────────────────────────────────────────────────────

LESSON_NUMBER = 3

LESSON_TEXT = (
    "Esta lição explora a variável {code}`$PATH`{/code}, o comando "
    "{code}`which`{/code} e as principais pastas do sistema. Também "
    "apresenta as flags {code}`ls -a`{/code} e {code}`ls -la`{/code} "
    "para listar arquivos ocultos e informações detalhadas."
)

TASKS = [
    "Execute {code}`echo $PATH`{/code} para ver a lista de diretórios "
    "onde o shell procura comandos. Note que os diretórios são separados "
    "por {code}`:`{/code}.",

    "Use {code}`which date`{/code} para descobrir onde o comando "
    "{code}`date`{/code} está localizado. Depois tente "
    "{code}`which echo`{/code} e {code}`which man`{/code}.",

    "Use {code}`ls /bin`{/code} para listar o conteúdo da pasta "
    "{code}`/bin`{/code}. Depois tente {code}`ls /usr/bin`{/code}. Estas "
    "são as principais pastas do sistema onde os comandos ficam.",

    "Escolha um comando da listagem de {code}`/bin`{/code} e use "
    "{code}`man`{/code} para ler sua página de manual (use a tecla "
    "{bold}Q{/bold} para sair). Por exemplo, {code}`man cat`{/code} ou "
    "{code}`man cp`{/code}.",

    "Dentro da pasta da lição, use {code}`echo $PATH > my_path`{/code} "
    "para salvar seu {code}`$PATH`{/code} atual em um arquivo chamado "
    "{code}`my_path`{/code}.",

    "Execute {code}`ls -a`{/code} dentro da pasta da lição. Note que são "
    "mostradas entradas começando com {code}`.`{/code}, que normalmente "
    "ficam ocultas. A entrada {code}`.`{/code} é a pasta atual e "
    "{code}`..`{/code} é a pasta pai.",

    "Execute {code}`ls -la`{/code} dentro da pasta da lição. Compare a "
    "saída com {code}`ls`{/code} simples. A flag {code}`-l`{/code} mostra "
    "permissões, dono, tamanho e data de cada entrada.",

    "Use {code}`which`{/code} para descobrir onde {code}`ls`{/code} está "
    "localizado. Depois execute {code}`ls -la`{/code} nesse caminho exato "
    "para ver suas permissões e tamanho. Por exemplo, se "
    "{code}`which ls`{/code} mostrar {code}`/usr/bin/ls`{/code}, execute "
    "{code}`ls -la /usr/bin/ls`{/code}.",

    "Dentro da pasta da lição, crie um arquivo chamado "
    "{code}`visible`{/code} usando {code}`echo public > visible`{/code}. "
    "Depois crie um arquivo oculto chamado {code}`.hidden`{/code} usando "
    "{code}`echo secret > .hidden`{/code}. Execute {code}`ls`{/code} e "
    "depois {code}`ls -a`{/code} para ver a diferença.",

    "Novamente na pasta da lição, execute o comando "
    "{code}`ls -la / > listing`{/code} e depois inspecione (usando um "
    "editor de texto) o conteúdo do arquivo {code}`listing`{/code}.",
]


# ── Verificações ────────────────────────────────────────────────────────────

def get_checks(folder):
    return [
        ("Tarefa 5: arquivo 'my_path' existe e não está vazio",
         lambda: base.check_nonempty_file_exists(os.path.join(folder, "my_path"),
                                                 lang='pt')),

        ("Tarefa 9: arquivo 'visible' existe com conteúdo 'public'",
         lambda: base.check_file_contents(os.path.join(folder, "visible"), "public",
                                          lang='pt')),

        ("Tarefa 9: arquivo '.hidden' existe com conteúdo 'secret'",
         lambda: base.check_file_contents(os.path.join(folder, ".hidden"), "secret",
                                          lang='pt')),

        ("Tarefa 10: arquivo 'listing' existe e não está vazio",
         lambda: base.check_nonempty_file_exists(os.path.join(folder, "listing"),
                                                 lang='pt')),
    ]


# ── Main ────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    base.lesson_main(LESSON_NUMBER, LESSON_TEXT, TASKS, get_checks, lang='pt')
