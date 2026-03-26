#!/usr/bin/env python3
"""Lição 5: manipulação básica de texto com cat, head, tail e >>."""

import os

import base

# ── Conteúdo da lição ───────────────────────────────────────────────────────

LESSON_NUMBER = 5

LESSON_TEXT = (
    "Esta lição aborda a manipulação básica de texto usando os comandos "
    "`cat`, `head` e `tail`, e o "
    "redirecionamento de acréscimo `>>`. O comando "
    "`cat` exibe ou concatena arquivos, `head` "
    "mostra as primeiras linhas e `tail` mostra as últimas "
    "linhas. O operador `>>` acrescenta ao arquivo em vez "
    "de sobrescrevê-lo."
)

TASKS = [
    "Entre na pasta da lição. Use `cat sample/colors.txt` "
    "para exibir o arquivo de cores. Note que o conteúdo é mostrado no "
    "terminal.",

    "Use `head sample/numbers.txt` para ver as primeiras 10 "
    "linhas (o padrão). Como o arquivo tem exatamente 10 linhas, você vê "
    "todas. Agora tente `head -3 sample/numbers.txt` para "
    "ver apenas as 3 primeiras linhas.",

    "Use `tail sample/numbers.txt` para ver as últimas 10 "
    "linhas. Agora tente `tail -4 sample/numbers.txt` para "
    "ver apenas as 4 últimas linhas.",

    "Use `head -3 sample/colors.txt > warm` para salvar as "
    "3 primeiras cores (as quentes) em um novo arquivo chamado "
    "`warm`.",

    "Use `tail -3 sample/colors.txt > cool` para salvar as "
    "3 últimas cores (as frias) em um novo arquivo chamado "
    "`cool`.",

    "Na pasta da lição, use `echo`, `>` e "
    "`>>` para construir um arquivo linha por linha. Execute "
    "`echo first > lines`, depois "
    "`echo second >> lines`, depois "
    "`echo third >> lines`. Use `cat lines` "
    "para verificar. Note que `>` cria (ou sobrescreve) "
    "enquanto `>>` acrescenta.",

    "Dentro da pasta `sample`, use `cat` para "
    "concatenar dois arquivos em um: "
    "`cat greeting.txt farewell.txt > ../combined`. Depois "
    "use `cat ../combined` para verificar que contém as "
    "duas linhas.",

    "Use `head -1 sample/numbers.txt > first_last` e depois "
    "`tail -1 sample/numbers.txt >> first_last` para criar "
    "um arquivo com apenas a primeira e a última linha do arquivo de "
    "números.",

    "Use `head -5 sample/numbers.txt > top5` e depois "
    "`tail -3 top5 > middle` para extrair as linhas 3, 4 "
    "e 5 do arquivo de números em um arquivo chamado "
    "`middle`.",

    "Crie um arquivo chamado `summary` que contenha as 2 "
    "primeiras cores, depois uma linha separadora `- - -`, "
    "depois as 2 últimas cores. Use `head`, "
    "`tail`, `echo` e os operadores "
    "`>` e `>>`.",
]


# ── Setup ───────────────────────────────────────────────────────────────────

SAMPLE_FILES = {
    "colors.txt": "red\norange\nyellow\ngreen\nblue\nindigo\nviolet\n",
    "numbers.txt": "one\ntwo\nthree\nfour\nfive\nsix\nseven\neight\nnine\nten\n",
    "greeting.txt": "hello world\n",
    "farewell.txt": "goodbye world\n",
}


def setup(folder):
    """Create the sample/ subfolder with pre-populated files."""
    sample = os.path.join(folder, "sample")
    os.makedirs(sample)
    for name, content in SAMPLE_FILES.items():
        with open(os.path.join(sample, name), "w") as f:
            f.write(content)


# ── Verificações ────────────────────────────────────────────────────────────

def get_checks(folder):
    return [
        ("Tarefa 4: arquivo 'warm' contém red, orange, yellow",
         lambda: base.check_file_contents(
             os.path.join(folder, "warm"), "red\norange\nyellow", lang='pt')),

        ("Tarefa 5: arquivo 'cool' contém blue, indigo, violet",
         lambda: base.check_file_contents(
             os.path.join(folder, "cool"), "blue\nindigo\nviolet", lang='pt')),

        ("Tarefa 6: arquivo 'lines' contém first, second, third",
         lambda: base.check_file_contents(
             os.path.join(folder, "lines"), "first\nsecond\nthird", lang='pt')),

        ("Tarefa 7: arquivo 'combined' contém hello world, goodbye world",
         lambda: base.check_file_contents(
             os.path.join(folder, "combined"), "hello world\ngoodbye world",
             lang='pt')),

        ("Tarefa 8: arquivo 'first_last' contém one, ten",
         lambda: base.check_file_contents(
             os.path.join(folder, "first_last"), "one\nten", lang='pt')),

        ("Tarefa 9: arquivo 'middle' contém three, four, five",
         lambda: base.check_file_contents(
             os.path.join(folder, "middle"), "three\nfour\nfive", lang='pt')),

        ("Tarefa 10: arquivo 'summary' contém red, orange, - - -, indigo, violet",
         lambda: base.check_file_contents(
             os.path.join(folder, "summary"), "red\norange\n- - -\nindigo\nviolet",
             lang='pt')),
    ]


# ── Main ────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    base.lesson_main(LESSON_NUMBER, LESSON_TEXT, TASKS, get_checks, setup,
                     lang='pt')
