"""Czysta logika odmiany i budowania pytań, niezależna od Tkintera."""
from dataclasses import dataclass
from latin_data import WORD_GROUPS, SENTENCE_EXERCISES

CASES = {"nom": "Nominativus", "gen": "Genetivus", "dat": "Dativus",
         "acc": "Accusativus", "abl": "Ablativus", "voc": "Vocativus"}
NUMBERS = {"sg": "liczba pojedyncza", "pl": "liczba mnoga"}

# Formy bez znaków długości samogłosek (łatwiejsze wpisywanie).
ENDINGS = {
    "I": {
        "sg": {"nom":"a", "gen":"ae", "dat":"ae", "acc":"am", "abl":"a", "voc":"a"},
        "pl": {"nom":"ae", "gen":"arum", "dat":"is", "acc":"as", "abl":"is", "voc":"ae"}},
    "II_m": {
        "sg": {"nom":None, "gen":"i", "dat":"o", "acc":"um", "abl":"o", "voc":None},
        "pl": {"nom":"i", "gen":"orum", "dat":"is", "acc":"os", "abl":"is", "voc":"i"}},
    "II_n": {
        "sg": {"nom":"um", "gen":"i", "dat":"o", "acc":"um", "abl":"o", "voc":"um"},
        "pl": {"nom":"a", "gen":"orum", "dat":"is", "acc":"a", "abl":"is", "voc":"a"}},
}

# Druga forma słownikowa pomaga wyznaczyć prawidłowy temat (ager -> agr-, liber -> libr-).
GENITIVE = {
    "puer":"pueri", "ager":"agri", "magister":"magistri", "liber":"libri",
    "filius":"filii",
}

@dataclass(frozen=True)
class Noun:
    latin: str
    polish: str
    group: str
    gender: str
    stem: str


def load_nouns():
    nouns = {}
    neuters = {"bellum", "templum", "donum", "verbum", "oppidum", "periculum"}
    for group, words in WORD_GROUPS.items():
        for latin, polish in words:
            if group == "I deklinacja":
                gender = "m" if latin in {"nauta", "poeta"} else "f"
                stem = latin[:-1]
            elif group == "II deklinacja":
                gender = "n" if latin in neuters else "m"
                stem = GENITIVE.get(latin, (latin[:-2] + "i" if latin.endswith("us") else latin[:-2] + "i") if latin.endswith("um") else latin + "i")[:-1]
            else:
                # Dodanie nowej deklinacji do WORD_GROUPS zachowuje tryb słówek;
                # odmiana zdań wymaga osobnego rozszerzenia silnika.
                continue
            nouns[latin] = Noun(latin, polish, group, gender, stem)
    return nouns

NOUNS = load_nouns()


def decline(noun, case, number):
    """Zwraca formę rzeczownika I lub II deklinacji dla wskazanego przypadku i liczby."""
    key = "I" if noun.group == "I deklinacja" else ("II_n" if noun.gender == "n" else "II_m")
    if noun.group not in ("I deklinacja", "II deklinacja"):
        raise ValueError(f"Brak odmiany dla grupy: {noun.group}")
    if noun.latin == "filius" and case == "voc" and number == "sg":
        return "fili"
    if noun.latin == "deus" and case == "voc" and number == "sg":
        return "deus"
    if noun.latin == "filia" and case == "gen" and number == "pl":
        return "filiarum"  # wariant filiārum; spotykane również filiābus w Dat./Abl. pl.
    if noun.latin == "deus" and number == "pl":
        raise ValueError("Odmiana liczby mnogiej deus ma formy oboczne – wymagane osobne opracowanie")
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


def make_questions(groups):
    """Tworzy pytania tylko dla zaznaczonych grup; waliduje dane na starcie."""
    results = []
    for latin, case, number, sentence, polish, hint in SENTENCE_EXERCISES:
        if latin not in NOUNS:
            raise ValueError(f"Nieznane hasło w zdaniach: {latin}")
        noun = NOUNS[latin]
        if noun.group in groups:
            if sentence.count("____") != 1:
                raise ValueError(f"Zdanie musi zawierać jedną lukę: {sentence}")
            results.append(SentenceQuestion(latin, case, number, sentence, polish, hint,
                                            decline(noun, case, number), noun.group))
    return results
