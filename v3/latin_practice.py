"""Niezależny od GUI silnik odmiany i losowego budowania zdań.

Nowe słowa trafiają do ćwiczeń automatycznie po dodaniu ich do bazy,
o ile podano dla nich płeć, dopełniacz i polskie formy.
"""
from dataclasses import dataclass
import random
from latin_data import WORD_GROUPS
from latin_extra import EXTRA_GROUPS, BASE_POLISH_FORMS
from latin_sentences import PATTERNS
from latin_legacy import SENTENCE_EXERCISES

CASES = {"nom": "Nominativus", "gen": "Genetivus", "dat": "Dativus",
         "acc": "Accusativus", "abl": "Ablativus", "voc": "Vocativus"}
NUMBERS = {"sg": "liczba pojedyncza", "pl": "liczba mnoga"}

ENDINGS = {
    "I": {"sg": {"nom": "a", "gen": "ae", "dat": "ae", "acc": "am", "abl": "a", "voc": "a"},
          "pl": {"nom": "ae", "gen": "arum", "dat": "is", "acc": "as", "abl": "is", "voc": "ae"}},
    "II_m": {"sg": {"nom": None, "gen": "i", "dat": "o", "acc": "um", "abl": "o", "voc": None},
             "pl": {"nom": "i", "gen": "orum", "dat": "is", "acc": "os", "abl": "is", "voc": "i"}},
    "II_n": {"sg": {"nom": "um", "gen": "i", "dat": "o", "acc": "um", "abl": "o", "voc": "um"},
             "pl": {"nom": "a", "gen": "orum", "dat": "is", "acc": "a", "abl": "is", "voc": "a"}},
}

BASE_GENITIVE = {"puer": "pueri", "ager": "agri", "magister": "magistri", "liber": "libri"}
BASE_NEUTERS = {"bellum", "templum", "donum", "verbum", "oppidum", "periculum"}
BASE_MASC_I = {"nauta", "poeta"}

@dataclass(frozen=True)
class Noun:
    latin: str
    polish: str
    group: str
    declension: str
    gender: str
    genitive: str
    stem: str
    forms: tuple  # nom.sg, acc.sg, gen.sg, loc.sg, nom.pl, acc.pl
    kind: str     # person / thing / abstract


def load_nouns():
    nouns = {}
    for group, words in WORD_GROUPS.items():
        if group in EXTRA_GROUPS:
            continue
        declension = group.split()[0]
        for latin, polish in words:
            gender = ("m" if latin in BASE_MASC_I else "f") if declension == "I" else ("n" if latin in BASE_NEUTERS else "m")
            genitive = (latin[:-1] + "ae") if declension == "I" else BASE_GENITIVE.get(latin, latin[:-2] + "i" if latin.endswith(("us", "um")) else latin + "i")
            if latin not in BASE_POLISH_FORMS:
                raise ValueError("Brak polskich form dla " + latin)
            *forms, kind = BASE_POLISH_FORMS[latin]
            nouns[latin] = Noun(latin, polish, group, declension, gender, genitive,
                                genitive[:-2] if declension == "I" else genitive[:-1], tuple(forms), kind)
    for group, words in EXTRA_GROUPS.items():
        declension = group.split()[0]
        for latin, polish, gender, genitive, forms, kind in words:
            if latin in nouns:
                raise ValueError("Powtórzone słowo: " + latin)
            nouns[latin] = Noun(latin, polish, group, declension, gender, genitive,
                                genitive[:-2] if declension == "I" else genitive[:-1], forms, kind)
    return nouns

NOUNS = load_nouns()


def decline(noun, case, number):
    """Formy w pisowni szkolnej, bez znaków długości samogłosek."""
    if noun.declension not in {"I", "II"}:
        raise ValueError("Brak obsługi deklinacji: " + noun.declension)
    if noun.latin == "deus" and number == "pl":
        raise ValueError("deus ma oboczne formy liczby mnogiej")
    if noun.latin == "filius" and case == "voc" and number == "sg":
        return "fili"
    if noun.latin == "deus" and case == "voc" and number == "sg":
        return "deus"
    if noun.latin in {"filius", "nuntius", "socius", "gladius"} and case == "voc" and number == "sg":
        return noun.stem + "i" if noun.latin.endswith("ius") else noun.latin
    key = "I" if noun.declension == "I" else ("II_n" if noun.gender == "n" else "II_m")
    ending = ENDINGS[key][number][case]
    if key == "II_m" and number == "sg":
        if case == "nom":
            return noun.latin
        if case == "voc":
            return noun.latin[:-2] + "e" if noun.latin.endswith("us") else noun.latin
    return noun.stem + ending


@dataclass(frozen=True)
class SentenceQuestion:
    latin: str
    case: str
    number: str
    sentence: str
    polish_sentence: str
    polish_hint: str
    expected: str
    group: str


# Formy polskie zapisane jawnie w latin_extra.py, bez automatycznego
# zgadywania odmiany. Mamy tu tylko przypadki, dla których te formy są znane.
POLISH_SLOT = {
    ("nom", "sg"): 0,
    ("acc", "sg"): 1,
    ("gen", "sg"): 2,
    ("abl", "sg"): 3,  # przyimkowe „o...” lub miejscownik po „w...”
    ("nom", "pl"): 4,
    ("acc", "pl"): 5,
}


def candidate_questions(noun):
    """Dobiera pasujące znaczeniowo zdania z rozbudowanego leksykonu."""
    result = []
    for p in PATTERNS:
        if noun.latin not in p.words:
            continue
        index = POLISH_SLOT.get((p.case, p.number))
        if index is None or noun.forms[index] is None:
            continue
        if noun.latin == "deus" and p.number == "pl":
            continue
        x = noun.forms[index]
        polish = p.polish.replace("{X}", x.capitalize()).replace("{x}", x)
        result.append(SentenceQuestion(noun.latin, p.case, p.number,
                                       p.latin, polish, x,
                                       decline(noun, p.case, p.number), noun.group))
    # Zachowujemy dawne zdania, zamiast rezygnować z nich przy zmianie
    # generatora. Stanowią uzupełnienie nowych, wielokrotnego użytku wzorów.
    for latin, case, number, latin_sentence, polish, hint in SENTENCE_EXERCISES:
        if latin != noun.latin:
            continue
        result.append(SentenceQuestion(noun.latin, case, number,
                                       latin_sentence, polish, hint,
                                       decline(noun, case, number), noun.group))
    # Dedup pełnej treści pytania
    return list({(q.sentence, q.polish_sentence, q.expected): q for q in result}.values())


def make_questions(groups, per_noun=3):
    """Losuje różne konstrukcje bez wymuszania mechanicznej powtarzalności.

    Z każdego wybranego słowa trafia do rundy do per_noun zdań.
    Ponowne rozpoczęcie wybiera zwykle inny zestaw.
    """
    questions = []
    for noun in NOUNS.values():
        if noun.group not in groups:
            continue
        candidates = candidate_questions(noun)
        if not candidates:
            raise ValueError(f"Nie ma zdania dla: {noun.latin}")
        questions.extend(random.sample(candidates, k=min(per_noun, len(candidates))))
    random.shuffle(questions)
    return questions
