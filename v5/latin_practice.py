"""Niezależny od GUI silnik odmiany i losowego budowania zdań.

Nowe słowa trafiają do ćwiczeń automatycznie po dodaniu ich do bazy,
o ile podano dla nich płeć, dopełniacz i polskie formy.
"""
from dataclasses import dataclass
import random
from latin_data import LEXICON, WORD_GROUPS
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

@dataclass(frozen=True)
class Noun:
    latin: str
    polish: str
    group: str
    declension: str
    gender: str
    genitive: str
    stem: str
    forms: tuple
    kind: str
    extra_forms: dict


def load_nouns():
    nouns = {}
    for group, entries in LEXICON.items():
        declension = group.split()[0]
        for record in entries:
            latin, polish, gender, genitive, forms, kind, _tags = record[:7]
            extra_forms = record[7] if len(record) > 7 else {}
            if latin in nouns:
                raise ValueError(f"Powtórzony rzeczownik w leksykonie: {latin}")
            if len(forms) != 6:
                raise ValueError(f"Rzeczownik {latin}: wymagane 6 polskich form")
            if declension == "I" and not genitive.endswith("ae"):
                raise ValueError(f"Niepoprawny Gen. sg. I deklinacji: {latin}")
            if declension == "II" and not genitive.endswith("i"):
                raise ValueError(f"Niepoprawny Gen. sg. II deklinacji: {latin}")
            stem = genitive[:-2] if declension == "I" else genitive[:-1]
            nouns[latin] = Noun(latin, polish, group, declension, gender,
                                genitive, stem, forms, kind, extra_forms)
    return nouns


NOUNS = load_nouns()


def decline(noun, case, number):
    """Formy w pisowni szkolnej, bez znaków długości samogłosek."""
    if noun.declension not in {"I", "II"}:
        raise ValueError("Brak obsługi deklinacji: " + noun.declension)
    if noun.latin == "deus" and number == "pl":
        raise ValueError("deus ma oboczne formy liczby mnogiej")
    if noun.latin == "deus" and case == "voc" and number == "sg":
        return "deus"

    if noun.latin.endswith("ius") and case == "voc" and number == "sg":
        return noun.stem
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


# Formy polskie zapisane jawnie w latin_data.py, bez automatycznego
# zgadywania odmiany. Mamy tu tylko przypadki, dla których te formy są znane.
POLISH_SLOT = {
    ("nom", "sg"): 0,
    ("acc", "sg"): 1,
    ("gen", "sg"): 2,
    ("abl", "sg"): 3,  # przyimkowe „o...” lub miejscownik po „w...”
    ("nom", "pl"): 4,
    ("acc", "pl"): 5,
}

EXTRA_SLOT = {("dat", "sg"): "dat_sg", ("dat", "pl"): "dat_pl",
              ("gen", "pl"): "gen_pl", ("abl", "pl"): "abl_pl",
              ("voc", "sg"): "voc_sg", ("voc", "pl"): "voc_pl"}



def candidate_questions(noun):
    """Dobiera pasujące znaczeniowo zdania z rozbudowanego leksykonu."""
    result = []
    for p in PATTERNS:
        if noun.latin not in p.words:
            continue
        index = POLISH_SLOT.get((p.case, p.number))
        x = (noun.forms[index] if index is not None
             else noun.extra_forms.get(EXTRA_SLOT.get((p.case, p.number))))
        if x is None or (noun.latin == "deus" and p.number == "pl"):
            continue
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


def make_questions(groups, per_noun=2):
    """Losuje per_noun RÓŻNYCH przypadków na rzeczownik w bieżącej rundzie.

    Preferuje przypadki i liczby niedoreprezentowane w aktualnej rundzie.
    Nie zapisuje historii między rundami i nie wymusza sztywnych proporcji.
    """
    from collections import Counter
    if per_noun < 1:
        return []
    selected = [n for n in NOUNS.values()
                if n.group in groups and n.declension in {"I", "II"}]
    random.shuffle(selected)
    # Miękkie udziały przypadków; Vocativus naturalnie występuje rzadziej.
    case_target = {"nom": .20, "gen": .20, "dat": .15,
                   "acc": .20, "abl": .20, "voc": .05}
    number_target = {"sg": .60, "pl": .40}
    case_counts = Counter()
    number_counts = Counter()
    questions = []
    for noun in selected:
        candidates = candidate_questions(noun)
        if not candidates:
            raise ValueError(f"Nie ma zdania dla: {noun.latin}")
        case_types = {q.case for q in candidates}
        # Co najwyżej jeden przykład danego przypadku dla tego rzeczownika.
        wanted = min(per_noun, len(case_types))
        chosen_cases = set()
        for _ in range(wanted):
            available = [q for q in candidates if q.case not in chosen_cases]
            total = len(questions) + 1
            weights = []
            for q in available:
                # Wybór losowy ważony stanem BIEŻĄCEJ rundy.
                case_gap = max(.08, case_target[q.case] * total - case_counts[q.case] + 1)
                number_gap = max(.15, number_target[q.number] * total - number_counts[q.number] + 1)
                # Liczba szablonów nie daje większej szansy przypadkowi.
                group_size = sum(1 for other in available
                                 if (other.case, other.number) == (q.case, q.number))
                weights.append(case_gap ** 2 * number_gap / group_size)
            picked = random.choices(available, weights=weights, k=1)[0]
            questions.append(picked)
            chosen_cases.add(picked.case)
            case_counts[picked.case] += 1
            number_counts[picked.number] += 1
    random.shuffle(questions)
    return questions
