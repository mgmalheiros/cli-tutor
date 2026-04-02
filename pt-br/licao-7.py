#!/usr/bin/env python3
"""Lição 7: correspondência de padrões com grep e expressões regulares básicas."""

import os

import base

# ── Conteúdo da lição ───────────────────────────────────────────────────────

LESSON_NUMBER = 7

LESSON_TEXT = (
    "Esta lição pratica **correspondência de padrões** com `grep` usando "
    "expressões regulares básicas. Em uma expressão regular básica, "
    "`.` corresponde a qualquer caractere, `\\.` corresponde a um ponto "
    "literal, `[a-z]` corresponde a um caractere de uma faixa, "
    "`*` significa zero ou mais do caractere anterior, "
    "`^` ancora a correspondência no início da linha e "
    "`$` ancora no final. Use `grep 'padrão' arquivo` para "
    "buscar dentro de um arquivo e `wc -l` para contar linhas. "
    "Salve resultados com redirecionamento `>`."
)


TASKS = [
    "Entre na pasta da lição. Use "
    "`cat sample/emails.txt | grep 'example'` para encontrar todas as "
    "linhas contendo a string `example`. Agora use o comando equivalente "
    "`grep 'example' sample/emails.txt`",

    "Use `grep 'ca.' sample/words.txt > ca_dot` para encontrar todas "
    "as palavras que contêm `ca` seguido de qualquer caractere. O `.` "
    "corresponde a exatamente um caractere, então `cat`, `car` e `card` "
    "são todos encontrados (entre outros).",

    "Use `grep 'ERROR' sample/log.txt | wc -l` para contar todas as "
    "linhas de erro do arquivo de log. Depois use "
    "`grep '2024-03' sample/log.txt` para ver todas as entradas de março "
    "de 2024.",

    "Use o comando `grep` com a faixa `[0-9]` (duas vezes) e o ponto "
    "literal `\\.` para mostrar **apenas os números de ponto flutuante** em "
    "`sample/numbers.txt`.",

    "Use `grep '^2024-02' sample/log.txt > february` para encontrar "
    "todas as linhas de log de fevereiro. O `^` ancora a correspondência "
    "no início da linha.",

    "Use `grep 'org$' sample/emails.txt > at_org` para encontrar "
    "todos os endereços de e-mail terminados em `org`. O `$` ancora "
    "a correspondência no final da linha.",

    "Use o comando `grep` para encontrar palavras em `sample/words.txt` "
    "que começam com `c` e terminam com `t`. Use as âncoras `^` e `$` "
    "para corresponder à linha inteira, e `.*` para corresponder a zero "
    "ou mais de qualquer caractere entre eles.",

    "Use o comando `grep` para encontrar todos os endereços IP listados "
    "em `hosts.txt` que estão na sub-rede `192.168.1`, colocando-os "
    "em um arquivo `local_net`.",
]


# ── Setup ───────────────────────────────────────────────────────────────────

SAMPLE_FILES = {
    "emails.txt": (
        "alice@example.com\n"
        "bob.smith@mail.org\n"
        "carol@server.net\n"
        "dan99@example.com\n"
        "eve@test\n"
        "frank@mail.org\n"
        "grace_h@example.com\n"
    ),
    "numbers.txt": (
        "42\n3.14\n100\n-7.5\n0.001\n99\n2.0\nhello\n12x34\n7\n"
    ),
    "log.txt": (
        "2024-01-15 INFO server started\n"
        "2024-01-15 ERROR disk full\n"
        "2024-02-20 WARNING low memory\n"
        "2024-02-20 INFO user login\n"
        "2024-03-01 ERROR timeout\n"
        "2024-03-01 INFO backup done\n"
        "2024-03-01 WARNING high load\n"
    ),
    "words.txt": (
        "cat\ncar\ncard\ncart\ncare\ncup\ncut\nbat\nbar\nbit\n"
    ),
    "hosts.txt": (
        "192.168.1.1\n"
        "10.0.0.1\n"
        "172.16.0.100\n"
        "192.168.1.20\n"
        "10.0.0.255\n"
        "abc.def.ghi\n"
        "999.999.999.999\n"
        "192.168.1.5\n"
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
        ("Tarefa 2: arquivo 'ca_dot' contém correspondências de ca.",
         lambda: base.check_file_contents(
             os.path.join(folder, "ca_dot"),
             "cat\ncar\ncard\ncart\ncare", lang='pt')),

        ("Tarefa 5: arquivo 'february' contém linhas de log de fevereiro",
         lambda: base.check_file_contents(
             os.path.join(folder, "february"),
             "2024-02-20 WARNING low memory\n"
             "2024-02-20 INFO user login", lang='pt')),

        ("Tarefa 6: arquivo 'at_org' contém endereços de e-mail .org",
         lambda: base.check_file_contents(
             os.path.join(folder, "at_org"),
             "bob.smith@mail.org\nfrank@mail.org", lang='pt')),

        ("Tarefa 8: arquivo 'local_net' contém endereços 192.168.1.x",
         lambda: base.check_file_contents(
             os.path.join(folder, "local_net"),
             "192.168.1.1\n192.168.1.20\n192.168.1.5", lang='pt')),
    ]


# ── Main ────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    base.lesson_main(LESSON_NUMBER, LESSON_TEXT, TASKS, get_checks, setup,
                     lang='pt')
