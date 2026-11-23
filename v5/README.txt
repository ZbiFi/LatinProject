TRENER LACINY - rozszerzony bank zdan i rownomierniejsze losowanie

URUCHOMIENIE
  python latin_vocab_trainer.py

WYMAGANIA
  Python 3 z Tkinter. Bez bibliotek zewnetrznych.

ZMIANY
  - Bank w latin_sentences.py rozszerzony o zdania z Dat. sg/pl,
    Gen. pl, Abl. pl i Voc. sg/pl, dobierane do kategorii slow.
  - Wszystkie rzeczowniki nadal znajduja sie TYLKO w latin_data.py.
    Opcjonalne dodatkowe formy polskie w tym samym wpisie umozliwiaja
    nowe zdania, bez zgadywania polskiej odmiany.
  - W latin_practice.py make_questions(groups, per_noun=2).
  - Kazdy rzeczownik w jednej rundzie jest cwiczony w 2 ROZNYCH
    przypadkach (np. Nom. i Abl., nie dwa razy Acc.).
  - Losowanie preferuje przypadki niedoreprezentowane W TEJ RUNDZIE;
    pozostaje losowe, nie jest sztywne i nie zapisuje historii.
  - Liczba pojedyncza / mnoga: orientacyjny cel 60/40, jesli dostepna
    pula zdan pozwala; wołacz ma nizsza wage.
  - Poprzednie zdania, trzy tryby i mechanizm powtorek zostaly zachowane.

EDYCJA
  latin_data.py          - centralny leksykon, grupy i formy polskie
  latin_practice.py      - logika odmiany i losowania pytan
  latin_sentences.py     - tematyczne szablony zdan
  latin_legacy.py        - dawny bank 113 zdan
  latin_vocab_trainer.py - interfejs

DODAWANIE NOWEGO RZECZOWNIKA
  Dopisz jeden rekord do wybranej grupy w latin_data.py.
  Format: (lacina, polski, rodzaj, Gen.sg., szesc_form, typ, tagi,
           opcjonalnie: dodatkowe_formy)
  dodatkowe_formy przyjmuja klucze: dat_sg, dat_pl, gen_pl,
  abl_pl, voc_sg, voc_pl. To polskie formy potrzebne do zdan.
  Bez dodatkowych form nowe slowo nadal dziala w trzech podstawowych
  przypadkach, a w razie braku kategorii w zdaniach awaryjnych.

UWAGI
  Nie kazdy przypadek sensownie pasuje do kazdego rzeczownika.
  Np. wołacz jest wykorzystywany przede wszystkim dla osob.
  deus: liczba mnoga jest pomijana z powodu obocznych form.
  Program nie zapisuje statystyk miedzy uruchomieniami/rundami.
