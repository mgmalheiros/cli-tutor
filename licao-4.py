#!/usr/bin/env python3
"""Lição 4: globs e wildcards do shell."""

import base64
import os

import base

# ── Conteúdo da lição ───────────────────────────────────────────────────────

LESSON_NUMBER = 4

LESSON_TEXT = (
    "Esta lição aborda os **globs** e **wildcards** do "
    "shell: `*` corresponde a qualquer número de caracteres, "
    "`?` corresponde a exatamente um caractere, "
    "`[...]` corresponde a um conjunto ou faixa de caracteres "
    "e `{a,b,c}` expande em múltiplas alternativas. Esses "
    "padrões permitem trabalhar com muitos arquivos de uma vez."
)

TASKS = [
    "Use `cd` para entrar na pasta da lição. Depois execute "
    "`ls sample/*.txt` para listar todos os arquivos "
    "`.txt` dentro de `sample`. O `*` "
    "corresponde a qualquer número de caracteres.",

    "Execute `ls sample/*.csv` para listar todos os arquivos "
    "`.csv`. Depois tente `ls sample/*.*` para "
    "listar todos os arquivos que têm extensão. Note que "
    "`README` não aparece porque não tem ponto.",

    "Execute `ls sample/note?.txt` para listar arquivos que "
    "correspondem a `note` seguido de exatamente um caractere "
    "e `.txt`. Note que `note10.txt` não aparece "
    "porque `?` corresponde a apenas um único caractere.",

    "Execute `ls sample/note[13].txt` para listar apenas "
    "`note1.txt` e `note3.txt`. O padrão "
    "`[...]` corresponde a qualquer caractere único do "
    "conjunto dado.",

    "Vá para a pasta `sample` e execute "
    "`ls note[1-3].txt` para listar `note1.txt`, "
    "`note2.txt` e `note3.txt`. Dentro de "
    "`[...]`, um hífen define uma faixa de caracteres.",

    "Dentro da pasta `sample` execute "
    "`ls {report,data}.csv` para listar "
    "`report.csv` e `data.csv`. A sintaxe "
    "`{a,b}` expande em palavras separadas — não é um "
    "verdadeiro wildcard, mas uma expansão do shell.",

    "Na pasta da lição, use "
    "`ls sample/*.txt > txt_list` para salvar a lista de "
    "todos os arquivos `.txt` de `sample` em "
    "um arquivo chamado `txt_list`.",

    "Vá para a pasta `sample` e use "
    "`ls ?????.*` para listar todos os arquivos cujo nome "
    "(antes da extensão) tem exatamente cinco caracteres. Salve o "
    "resultado em um arquivo chamado `../five_chars` usando "
    "redirecionamento.",
]


# ── Setup ───────────────────────────────────────────────────────────────────

# image.png bundled as base64
IMAGE_PNG_B64 = (
    "iVBORw0KGgoAAAANSUhEUgAAAIAAAACACAMAAAD04JH5AAAAFVBMVEUfIis7NjNbdyp7mTmTvDjY"
    "0bXR24LQt5i4AAAAqElEQVR42u3YMQoDIBBEUVXj/Y+cfppFUmjg/VrhlcO2HY1oRjv6RKtoRAAA"
    "AAAAAAD3ASNa0Sw6/Z9gAAAAgPsAAACAGfWiasD0IgAAAAAAAID/A7SoGhwt6tGKAAAA3gMAAAAA"
    "rGhHp4NjRAAAAAAAAADvAU4PDq2oGiAJBAAAAAAAAHgf0H4sATMCAAAAAAAAuA4oH/RoF/VoRCsC"
    "AAAAAAAAuA74AooztQEgXSCJAAAAAElFTkSuQmCC"
)

LOGO_SVG = (
    '<svg xmlns="http://www.w3.org/2000/svg" width="340" height="370">'
    '<defs><path id="a" fill="#231f20" d="M-62.99 36.37H62.99l62.99 109.1'
    "-17.5 30.31-62.99-109.1H-80.49zM41.16 74.18h-20l-24.5 42.44 30.31 "
    '17.5 24.5-42.44z"/></defs><g transform="translate(210 190)">'
    '<path fill="#ed1c24" d="m0-57.74-50 86.61H50z"/><use href="#a"/>'
    '<use href="#a" transform="rotate(120)"/>'
    '<use href="#a" transform="rotate(240)"/></g></svg>\n'
)

SAMPLE_FILES = {
    "note1.txt": "note one\n",
    "note2.txt": "note two\n",
    "note3.txt": "note three\n",
    "note10.txt": "note ten\n",
    "report.txt": "final report\n",
    "report.csv": "a,b,c\n",
    "data.csv": "1,2,3\n",
    "README": "read me\n",
    "logo.svg": LOGO_SVG,
}


def setup(folder):
    """Create the sample/ subfolder with pre-populated files."""
    sample = os.path.join(folder, "sample")
    os.makedirs(sample)
    for name, content in SAMPLE_FILES.items():
        with open(os.path.join(sample, name), "w") as f:
            f.write(content)
    # binary file
    with open(os.path.join(sample, "image.png"), "wb") as f:
        f.write(base64.b64decode(IMAGE_PNG_B64))


# ── Verificações ────────────────────────────────────────────────────────────

TXT_LIST_EXPECTED = "\n".join([
    "sample/note10.txt",
    "sample/note1.txt",
    "sample/note2.txt",
    "sample/note3.txt",
    "sample/report.txt",
])

FIVE_CHARS_EXPECTED = "\n".join([
    "image.png",
    "note1.txt",
    "note2.txt",
    "note3.txt",
])


def get_checks(folder):
    return [
        ("Tarefa 7: arquivo 'txt_list' tem a listagem esperada",
         lambda: base.check_file_contents(os.path.join(folder, "txt_list"),
                                          TXT_LIST_EXPECTED, lang='pt')),

        ("Tarefa 8: arquivo 'five_chars' tem a listagem esperada",
         lambda: base.check_file_contents(os.path.join(folder, "five_chars"),
                                          FIVE_CHARS_EXPECTED, lang='pt')),
    ]


# ── Main ────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    base.lesson_main(LESSON_NUMBER, LESSON_TEXT, TASKS, get_checks, setup,
                     lang='pt')
