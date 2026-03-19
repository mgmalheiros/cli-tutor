#!/usr/bin/env python3
"""Lição 5: manipulação básica de texto com cat, head, tail e >>."""

import os

import base

# ── Conteúdo da lição ───────────────────────────────────────────────────────

LESSON_NUMBER = 5

LESSON_TEXT = (
    "Esta lição aborda a manipulação básica de texto usando os comandos "
    "{code}`cat`{/code}, {code}`head`{/code} e {code}`tail`{/code}, e o "
    "redirecionamento de acréscimo {code}`>>`{/code}. O comando "
    "{code}`cat`{/code} exibe ou concatena arquivos, {code}`head`{/code} "
    "mostra as primeiras linhas e {code}`tail`{/code} mostra as últimas "
    "linhas. O operador {code}`>>`{/code} acrescenta ao arquivo em vez "
    "de sobrescrevê-lo."
)

TASKS = [
    "Entre na pasta da lição. Use {code}`cat sample/colors.txt`{/code} "
    "para exibir o arquivo de cores. Note que o conteúdo é mostrado no "
    "terminal.",

    "Use {code}`head sample/numbers.txt`{/code} para ver as primeiras 10 "
    "linhas (o padrão). Como o arquivo tem exatamente 10 linhas, você vê "
    "todas. Agora tente {code}`head -3 sample/numbers.txt`{/code} para "
    "ver apenas as 3 primeiras linhas.",

    "Use {code}`tail sample/numbers.txt`{/code} para ver as últimas 10 "
    "linhas. Agora tente {code}`tail -4 sample/numbers.txt`{/code} para "
    "ver apenas as 4 últimas linhas.",

    "Use {code}`head -3 sample/colors.txt > warm`{/code} para salvar as "
    "3 primeiras cores (as quentes) em um novo arquivo chamado "
    "{code}`warm`{/code}.",

    "Use {code}`tail -3 sample/colors.txt > cool`{/code} para salvar as "
    "3 últimas cores (as frias) em um novo arquivo chamado "
    "{code}`cool`{/code}.",

    "Na pasta da lição, use {code}`echo`{/code}, {code}`>`{/code} e "
    "{code}`>>`{/code} para construir um arquivo linha por linha. Execute "
    "{code}`echo first > lines`{/code}, depois "
    "{code}`echo second >> lines`{/code}, depois "
    "{code}`echo third >> lines`{/code}. Use {code}`cat lines`{/code} "
    "para verificar. Note que {code}`>`{/code} cria (ou sobrescreve) "
    "enquanto {code}`>>`{/code} acrescenta.",

    "Dentro da pasta {code}`sample`{/code}, use {code}`cat`{/code} para "
    "concatenar dois arquivos em um: "
    "{code}`cat greeting.txt farewell.txt > ../combined`{/code}. Depois "
    "use {code}`cat ../combined`{/code} para verificar que contém as "
    "duas linhas.",

    "Use {code}`head -1 sample/numbers.txt > first_last`{/code} e depois "
    "{code}`tail -1 sample/numbers.txt >> first_last`{/code} para criar "
    "um arquivo com apenas a primeira e a última linha do arquivo de "
    "números.",

    "Use {code}`head -5 sample/numbers.txt > top5`{/code} e depois "
    "{code}`tail -3 top5 > middle`{/code} para extrair as linhas 3, 4 "
    "e 5 do arquivo de números em um arquivo chamado "
    "{code}`middle`{/code}.",

    "Crie um arquivo chamado {code}`summary`{/code} que contenha as 2 "
    "primeiras cores, depois uma linha separadora {code}`- - -`{/code}, "
    "depois as 2 últimas cores. Use {code}`head`{/code}, "
    "{code}`tail`{/code}, {code}`echo`{/code} e os operadores "
    "{code}`>`{/code} e {code}`>>`{/code}.",
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
