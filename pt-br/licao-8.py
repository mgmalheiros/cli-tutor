#!/usr/bin/env python3
"""Lição 8: correspondência de padrões e substituição com rg (ripgrep)."""

import os

import base

# ── Conteúdo da lição ───────────────────────────────────────────────────────

LESSON_NUMBER = 8

LESSON_TEXT = (
    "Esta lição pratica **correspondência de padrões e substituição** "
    "com `rg` (ripgrep) usando expressões regulares estendidas. O "
    "comando `rg` funciona como o `grep` mas usa sintaxe estendida "
    "por padrão: `+` significa um ou mais, `?` significa zero ou um, "
    "e `*` significa zero ou mais do item anterior. Conjuntos de "
    "caracteres `[abc]` correspondem a um caractere do grupo. As "
    "classes abreviadas `\\d` (qualquer dígito), `\\w` (qualquer "
    "caractere de palavra: letra, dígito ou sublinhado) e `\\s` "
    "(qualquer espaço em branco) correspondem a categorias comuns. "
    "Um grupo de captura `(...)` salva parte de uma correspondência, "
    "que pode ser referenciada como `$1` em uma substituição com a "
    "flag `-r`. Use `-o` para exibir apenas a parte correspondida."
)

TASKS = [
    "Entre na pasta da lição. Execute `echo 'error 404' | rg '\\d+'` "
    "e observe que o `rg` encontra a sequência de dígitos `404`. "
    "Agora use `rg 'ERROR' sample/log.txt` para encontrar todas as "
    "linhas de erro diretamente de um arquivo — o `rg` funciona como "
    "o `grep` mas usa expressões regulares estendidas por padrão.",

    "Use `rg -o '\\d+' sample/data.txt > all_numbers` para extrair "
    "todas as sequências de dígitos do arquivo de dados. O `\\d` "
    "corresponde a qualquer dígito e `+` significa um ou mais. A "
    "flag `-o` exibe apenas as partes correspondidas, uma por linha.",

    "Use `rg '\\w+@\\w+\\.\\w+' sample/emails.txt > valid_emails` "
    "para encontrar todas as linhas que correspondem a um padrão "
    "simples de e-mail: um ou mais caracteres de palavra, um `@`, "
    "um ou mais caracteres de palavra, um ponto literal e um ou mais "
    "caracteres de palavra. A classe `\\w` corresponde a letras, "
    "dígitos e sublinhados.",

    "Use `rg 'colou?r' sample/words.txt > col_words` para encontrar "
    "tanto `color` quanto `colour`. O `?` torna o `u` anterior "
    "opcional, correspondendo a zero ou uma ocorrência.",

    "Use `rg 'gr[ae]y' sample/words.txt > grays` para encontrar "
    "tanto `gray` quanto `grey`. O conjunto de caracteres `[ae]` "
    "corresponde a `a` ou `e`.",

    "Use `rg -o '\\w+\\s\\w+$' sample/log.txt > messages` para "
    "extrair a mensagem de duas palavras no final de cada linha de "
    "log. Aqui `\\w+` corresponde a uma palavra, `\\s` corresponde "
    "ao espaço entre elas, e `$` ancora a correspondência no final "
    "da linha.",

    "Use `rg -o '(\\w+)@\\w+\\.\\w+' -r '$1' sample/emails.txt > "
    "usernames` para extrair apenas o nome de usuário de cada "
    "endereço de e-mail. Os parênteses `(...)` criam um grupo de "
    "captura ao redor do primeiro `\\w+`, e `-r '$1'` substitui "
    "toda a correspondência apenas pela parte capturada.",

    "Use `rg` com a flag `-o` e `\\d` para extrair apenas as datas "
    "(no formato `YYYY-MM-DD`) de `sample/log.txt`. Salve-as em um "
    "arquivo chamado `dates`.",

    "Use `rg` com `-o` para extrair apenas os horários (no formato "
    "`HH:MM`) de `sample/log.txt`. Salve-os em um arquivo chamado "
    "`times`.",

    "Use `rg` com um grupo de captura e `-r '$1'` para extrair "
    "apenas os nomes de domínio (como `example.com`) de cada "
    "endereço de e-mail em `sample/emails.txt`. Salve o resultado "
    "em `domains`.",
]


# ── Setup ───────────────────────────────────────────────────────────────────

SAMPLE_FILES = {
    "emails.txt": (
        "alice@example.com\n"
        "bob@mail.org\n"
        "carol@server.net\n"
        "dan99@example.com\n"
        "not-an-email\n"
        "frank@mail.org\n"
        "grace@example.com\n"
    ),
    "log.txt": (
        "2024-01-15 10:30 INFO server started\n"
        "2024-01-15 10:31 ERROR disk full\n"
        "2024-02-20 14:00 WARNING low memory\n"
        "2024-02-20 14:05 INFO user login\n"
        "2024-03-01 09:00 ERROR connection timeout\n"
        "2024-03-01 09:15 INFO backup done\n"
    ),
    "words.txt": (
        "color\ncolour\nfavor\nfavour\n"
        "gray\ngrey\ncenter\ncentre\n"
    ),
    "data.txt": (
        "item:1001 price:25\n"
        "item:1002 price:130\n"
        "item:1003 price:8\n"
        "item:2001 price:55\n"
        "item:2002 price:200\n"
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
        ("Tarefa 2: arquivo 'all_numbers' contém dígitos extraídos",
         lambda: base.check_file_contents(
             os.path.join(folder, "all_numbers"),
             "1001\n25\n1002\n130\n1003\n8\n2001\n55\n2002\n200",
             lang='pt')),

        ("Tarefa 3: arquivo 'valid_emails' contém linhas de e-mail válidas",
         lambda: base.check_file_contents(
             os.path.join(folder, "valid_emails"),
             "alice@example.com\nbob@mail.org\ncarol@server.net\n"
             "dan99@example.com\nfrank@mail.org\ngrace@example.com",
             lang='pt')),

        ("Tarefa 4: arquivo 'col_words' contém color e colour",
         lambda: base.check_file_contents(
             os.path.join(folder, "col_words"),
             "color\ncolour", lang='pt')),

        ("Tarefa 5: arquivo 'grays' contém gray e grey",
         lambda: base.check_file_contents(
             os.path.join(folder, "grays"),
             "gray\ngrey", lang='pt')),

        ("Tarefa 6: arquivo 'messages' contém mensagens de log",
         lambda: base.check_file_contents(
             os.path.join(folder, "messages"),
             "server started\ndisk full\nlow memory\n"
             "user login\nconnection timeout\nbackup done",
             lang='pt')),

        ("Tarefa 7: arquivo 'usernames' contém nomes de usuário",
         lambda: base.check_file_contents(
             os.path.join(folder, "usernames"),
             "alice\nbob\ncarol\ndan99\nfrank\ngrace",
             lang='pt')),

        ("Tarefa 8: arquivo 'dates' contém datas ISO extraídas",
         lambda: base.check_file_contents(
             os.path.join(folder, "dates"),
             "2024-01-15\n2024-01-15\n2024-02-20\n"
             "2024-02-20\n2024-03-01\n2024-03-01",
             lang='pt')),

        ("Tarefa 9: arquivo 'times' contém horários extraídos",
         lambda: base.check_file_contents(
             os.path.join(folder, "times"),
             "10:30\n10:31\n14:00\n14:05\n09:00\n09:15",
             lang='pt')),

        ("Tarefa 10: arquivo 'domains' contém nomes de domínio extraídos",
         lambda: base.check_file_contents(
             os.path.join(folder, "domains"),
             "example.com\nmail.org\nserver.net\n"
             "example.com\nmail.org\nexample.com",
             lang='pt')),
    ]


# ── Main ────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    base.lesson_main(LESSON_NUMBER, LESSON_TEXT, TASKS, get_checks, setup,
                     lang='pt')
