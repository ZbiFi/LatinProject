"""Podstawowe 40 rzeczowników. Dodatkowe zestawy są w latin_extra.py."""

WORD_GROUPS = {
    "I deklinacja": [
        ("puella", "dziewczyna"),
        ("rosa", "róża"),
        ("aqua", "woda"),
        ("terra", "ziemia"),
        ("via", "droga"),
        ("silva", "las"),
        ("femina", "kobieta"),
        ("vita", "życie"),
        ("insula", "wyspa"),
        ("patria", "ojczyzna"),
        ("familia", "rodzina"),
        ("amica", "przyjaciółka"),
        ("filia", "córka"),
        ("villa", "dom wiejski; willa"),
        ("porta", "brama"),
        ("stella", "gwiazda"),
        ("luna", "księżyc"),
        ("cura", "troska; opieka"),
        ("nauta", "żeglarz"),
        ("poeta", "poeta"),
    ],
    "II deklinacja": [
        ("servus", "niewolnik"),
        ("dominus", "pan; właściciel"),
        ("amicus", "przyjaciel"),
        ("puer", "chłopiec"),
        ("ager", "pole"),
        ("filius", "syn"),
        ("equus", "koń"),
        ("magister", "nauczyciel"),
        ("populus", "lud; naród"),
        ("hortus", "ogród"),
        ("deus", "bóg"),
        ("locus", "miejsce"),
        ("animus", "duch; umysł"),
        ("liber", "książka"),
        ("bellum", "wojna"),
        ("templum", "świątynia"),
        ("donum", "dar; prezent"),
        ("verbum", "słowo"),
        ("oppidum", "miasto; miasteczko"),
        ("periculum", "niebezpieczeństwo"),
    ],
}

# Zestawy dodatkowe łączymy automatycznie; GUI tworzy checkbox dla każdego.
from latin_extra import EXTRA_GROUPS
WORD_GROUPS.update({name: [(latin, polish) for latin, polish, *_ in entries] for name, entries in EXTRA_GROUPS.items()})
