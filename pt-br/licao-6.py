#!/usr/bin/env python3
"""Lição 6: manipulação de texto com wc, sort, uniq, grep, diff e pipes."""

import os

import base

# ── Conteúdo da lição ───────────────────────────────────────────────────────

LESSON_NUMBER = 6

LESSON_TEXT = (
    "Esta lição aborda ferramentas de manipulação de texto: "
    "`wc` conta linhas, palavras e caracteres; "
    "`sort` ordena linhas alfabeticamente; "
    "`uniq` remove linhas duplicadas adjacentes; "
    "`grep` encontra linhas que contêm uma determinada string; "
    "e `diff` mostra as diferenças entre dois arquivos. O "
    "operador pipe `|` conecta a saída de um comando à entrada "
    "do próximo, permitindo combinar ferramentas. O editor de texto "
    "`nano` permite editar arquivos interativamente."
)

TASKS = [
    "Entre na pasta da lição. Use `wc sample/fruits.txt` para "
    "ver três números: contagem de linhas, palavras e caracteres. Depois "
    "tente `wc -l sample/fruits.txt` para apenas a contagem de "
    "linhas, `wc -w` para palavras e `wc -c` para "
    "caracteres.",

    "Use `sort sample/fruits.txt > sorted_fruits` para ordenar "
    "as frutas alfabeticamente e salvar o resultado. Use "
    "`cat sorted_fruits` para verificar. Note que as entradas "
    "duplicadas agora aparecem juntas.",

    "Use `grep \"cherry\" sample/fruits.txt > found_cherry` "
    "para encontrar todas as linhas contendo a string \"cherry\" e salvá-las "
    "em um arquivo.",

    "Use `diff sample/original.txt sample/revised.txt` para "
    "comparar os dois arquivos. Note como o `diff` marca as "
    "linhas que diferem: `<` para linhas apenas no primeiro "
    "arquivo e `>` para linhas apenas no segundo.",

    "Use `grep -v \"INFO\" sample/log.txt > no_info` para "
    "encontrar todas as linhas que *não* contêm \"INFO\" e "
    "salvá-las. A flag `-v` inverte a condição de busca, "
    "mostrando apenas as linhas que não correspondem.",

    "Use `diff sample/original.txt sample/revised.txt > changes` "
    "para salvar a saída do diff em um arquivo para referência futura.",

    "Use `sort sample/fruits.txt | uniq > unique_fruits` para "
    "ordenar as frutas e depois remover linhas duplicadas. O `|` "
    "(pipe) envia a saída do `sort` como entrada para o "
    "`uniq`. Note que o `uniq` só remove "
    "duplicatas *adjacentes*, por isso o `sort` "
    "deve vir antes.",

    "Use `grep \"ERROR\" sample/log.txt | sort -r > sorted_errors` "
    "para extrair todas as linhas de erro e depois ordená-las em "
    "ordem alfabética reversa (usando a flag `-r`).",

    "Use `tail -5 sample/log.txt | grep \"INFO\" > recent_info` "
    "para primeiro obter as últimas cinco entradas do log e depois filtrar "
    "apenas as que contêm \"INFO\".",

    "Use `grep \"mammal\" sample/animals.txt | sort | uniq > mammals` "
    "para encontrar todas as entradas de mamíferos, ordená-las e "
    "remover duplicatas. Isso encadeia três comandos usando dois pipes.",

    "Copie o arquivo original com "
    "`cat sample/original.txt > fixed`. Depois abra com "
    "`nano fixed` e edite manualmente para que o conteúdo "
    "corresponda a `sample/revised.txt`: mude "
    "`banana` para `blueberry` e "
    "`melon` para `dragonfruit`. Salve com "
    "**Ctrl+O**, confirme o nome do arquivo com **Enter** "
    "e saia com **Ctrl+X**.",

    "Construa um arquivo acrescentando resultados de pipes. Primeiro execute "
    "`grep \"bird\" sample/animals.txt | sort | uniq > wildlife`. "
    "Depois execute "
    "`grep \"fish\" sample/animals.txt | sort | uniq >> wildlife`. "
    "Use `cat wildlife` para verificar que contém as entradas "
    "de aves seguidas pelas de peixes.",
]


# ── Setup ───────────────────────────────────────────────────────────────────

SAMPLE_FILES = {
    "fruits.txt": (
        "banana\napple\ncherry\nbanana\nmelon\n"
        "apple\nkiwi\nlemon\nbanana\ncherry\n"
    ),
    "log.txt": (
        "INFO server started\n"
        "ERROR connection failed\n"
        "INFO user logged in\n"
        "WARNING disk space low\n"
        "ERROR timeout occurred\n"
        "INFO backup complete\n"
        "WARNING high memory usage\n"
        "ERROR file not found\n"
        "INFO server stopped\n"
    ),
    "original.txt": "apple\nbanana\ncherry\nmelon\nkiwi\n",
    "revised.txt": "apple\nblueberry\ncherry\ndragonfruit\nkiwi\n",
    "animals.txt": (
        "dog mammal\ncat mammal\neagle bird\nsalmon fish\nfrog amphibian\n"
        "cat mammal\ndog mammal\nparrot bird\ntrout fish\ndog mammal\n"
    ),
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
        ("Tarefa 2: arquivo 'sorted_fruits' contém lista de frutas ordenada",
         lambda: base.check_file_contents(
             os.path.join(folder, "sorted_fruits"),
             "apple\napple\nbanana\nbanana\nbanana\n"
             "cherry\ncherry\nkiwi\nlemon\nmelon", lang='pt')),

        ("Tarefa 3: arquivo 'found_cherry' contém linhas com cherry",
         lambda: base.check_file_contents(
             os.path.join(folder, "found_cherry"),
             "cherry\ncherry", lang='pt')),

        ("Tarefa 5: arquivo 'no_info' contém linhas sem INFO",
         lambda: base.check_file_contents(
             os.path.join(folder, "no_info"),
             "ERROR connection failed\n"
             "WARNING disk space low\n"
             "ERROR timeout occurred\n"
             "WARNING high memory usage\n"
             "ERROR file not found", lang='pt')),

        ("Tarefa 6: arquivo 'changes' contém saída do diff",
         lambda: base.check_file_contents(
             os.path.join(folder, "changes"),
             "2c2\n< banana\n---\n> blueberry\n"
             "4c4\n< melon\n---\n> dragonfruit", lang='pt')),

        ("Tarefa 7: arquivo 'unique_fruits' contém frutas únicas ordenadas",
         lambda: base.check_file_contents(
             os.path.join(folder, "unique_fruits"),
             "apple\nbanana\ncherry\nkiwi\nlemon\nmelon", lang='pt')),

        ("Tarefa 8: arquivo 'sorted_errors' contém erros em ordem reversa",
         lambda: base.check_file_contents(
             os.path.join(folder, "sorted_errors"),
             "ERROR timeout occurred\n"
             "ERROR file not found\n"
             "ERROR connection failed", lang='pt')),

        ("Tarefa 9: arquivo 'recent_info' contém últimas entradas INFO",
         lambda: base.check_file_contents(
             os.path.join(folder, "recent_info"),
             "INFO backup complete\nINFO server stopped", lang='pt')),

        ("Tarefa 10: arquivo 'mammals' contém mamíferos únicos ordenados",
         lambda: base.check_file_contents(
             os.path.join(folder, "mammals"),
             "cat mammal\ndog mammal", lang='pt')),

        ("Tarefa 11: arquivo 'fixed' corresponde a revised.txt",
         lambda: base.check_file_contents(
             os.path.join(folder, "fixed"),
             "apple\nblueberry\ncherry\ndragonfruit\nkiwi", lang='pt')),

        ("Tarefa 12: arquivo 'wildlife' contém aves e depois peixes",
         lambda: base.check_file_contents(
             os.path.join(folder, "wildlife"),
             "eagle bird\nparrot bird\nsalmon fish\ntrout fish", lang='pt')),
    ]


# ── Main ────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    base.lesson_main(LESSON_NUMBER, LESSON_TEXT, TASKS, get_checks, setup,
                     lang='pt')
