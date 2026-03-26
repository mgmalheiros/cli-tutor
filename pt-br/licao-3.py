#!/usr/bin/env python3
"""Lição 3: $PATH, which, pastas do sistema e flags do ls."""

import os

import base

# ── Conteúdo da lição ───────────────────────────────────────────────────────

LESSON_NUMBER = 3

LESSON_TEXT = (
    "Esta lição explora a variável `$PATH`, o comando "
    "`which` e as principais pastas do sistema. Também "
    "apresenta as flags `ls -a` e `ls -la` "
    "para listar arquivos ocultos e informações detalhadas."
)

TASKS = [
    "Execute `echo $PATH` para ver a lista de diretórios "
    "onde o shell procura comandos. Note que os diretórios são separados "
    "por `:`.",

    "Use `which date` para descobrir onde o comando "
    "`date` está localizado. Depois tente "
    "`which echo` e `which man`.",

    "Use `ls /bin` para listar o conteúdo da pasta "
    "`/bin`. Depois tente `ls /usr/bin`. Estas "
    "são as principais pastas do sistema onde os comandos ficam.",

    "Escolha um comando da listagem de `/bin` e use "
    "`man` para ler sua página de manual (use a tecla "
    "**Q** para sair). Por exemplo, `man cat` ou "
    "`man cp`.",

    "Dentro da pasta da lição, use `echo $PATH > my_path` "
    "para salvar seu `$PATH` atual em um arquivo chamado "
    "`my_path`.",

    "Execute `ls -a` dentro da pasta da lição. Note que são "
    "mostradas entradas começando com `.`, que normalmente "
    "ficam ocultas. A entrada `.` é a pasta atual e "
    "`..` é a pasta pai.",

    "Execute `ls -la` dentro da pasta da lição. Compare a "
    "saída com `ls` simples. A flag `-l` mostra "
    "permissões, dono, tamanho e data de cada entrada.",

    "Use `which` para descobrir onde `ls` está "
    "localizado. Depois execute `ls -la` nesse caminho exato "
    "para ver suas permissões e tamanho. Por exemplo, se "
    "`which ls` mostrar `/usr/bin/ls`, execute "
    "`ls -la /usr/bin/ls`.",

    "Dentro da pasta da lição, crie um arquivo chamado "
    "`visible` usando `echo public > visible`. "
    "Depois crie um arquivo oculto chamado `.hidden` usando "
    "`echo secret > .hidden`. Execute `ls` e "
    "depois `ls -a` para ver a diferença.",

    "Novamente na pasta da lição, execute o comando "
    "`ls -la / > listing` e depois inspecione (usando um "
    "editor de texto) o conteúdo do arquivo `listing`.",
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
