TRENER ŁACINY – wersja z ćwiczeniami w zdaniach

URUCHAMIANIE:
  python latin_vocab_trainer.py

Wymagania: Python 3, Tkinter (w Windows zwykle domyślnie z Pythonem;
na niektórych systemach Linux: sudo apt install python3-tk).
Nie potrzeba instalować bibliotek przez pip.

TRYBY:
- Słówka: zachowany dotychczasowy trening w obu kierunkach.
- Zdania: pełne polskie zdanie + łacińskie zdanie z luką.
  Wpisz tylko formę brakującego rzeczownika po łacinie.
  Formy obejmują liczbę pojedynczą i mnogą oraz różne przypadki.

POWTÓRKI: błędy trafiają do dodatkowej rundy (można wyłączyć).

STRUKTURA:
- latin_vocab_trainer.py : interfejs graficzny i przebieg nauki
- latin_data.py          : 40 słówek + pula zdań do rozbudowy
- latin_practice.py      : reguły odmiany i generator pytań

ROZSZERZENIA:
- Nowe słowa dopisz do WORD_GROUPS w latin_data.py.
- Nowe zdania dopisz do SENTENCE_EXERCISES w latin_data.py, według schematu:
  ("rosa", "acc", "sg", "Puella ____ videt.", "Dziewczyna widzi różę.", "różę")
- Dodanie III deklinacji do zdań wymaga rozszerzenia reguł w latin_practice.py.
  Tryb słówek dla nowej grupy działa bez takich zmian.

Zapis łaciński w ćwiczeniach nie wymaga oznaczania długości samogłosek.
