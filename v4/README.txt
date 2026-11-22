TRENER ŁACINY — WERSJA Z UPORZĄDKOWANYM LEKSYKONEM
===================================================

URUCHOMIENIE
  python latin_vocab_trainer.py

Python 3 + Tkinter. Wszystkie pliki .py umieść w jednym katalogu.

GDZIE DODAWAĆ SŁOWA
  Edytuj TYLKO latin_data.py.
  W słowniku LEXICON są 4 grupy po 20 słów (łącznie 80).
  Każda grupa ma własny checkbox utworzony automatycznie w GUI.
  Nie ma już osobnego latin_extra.py ani słowników polskich form
  i odmiany w latin_practice.py.

JAK DODAĆ NOWE SŁOWO
  1. Otwórz latin_data.py.
  2. Wybierz grupę w LEXICON i skopiuj jeden wpis jako wzór.
  3. Zmień siedem pól:
     (forma łacińska, tłumaczenie, rodzaj, Gen.sg.,
      polskie formy, typ, kategorie znaczeniowe)
  4. Zapisz i uruchom program ponownie.

Przykład nowego wpisu I deklinacji:
  ('tabula', 'tablica', 'f', 'tabulae',
   ('tablica', 'tablicę', 'tablicy', 'tablicy', 'tablice', 'tablice'),
   'thing', ('visible', 'carriable')),

Kolejność polskich form:
  mianownik lp, biernik lp, dopełniacz lp,
  forma po "o"/"w" (najczęściej miejscownik) lp, mianownik lm, biernik lm.
  Uwaga: jedna forma po "o"/"w" jest uproszczeniem obecnego generatora.
  Dla braku liczby mnogiej wpisz None w odpowiednich polach.

PRZYKŁADOWE KATEGORIE ZDAŃ (ostatnie pole wpisu)
  individuals, learners, travelers, writers, leaders,
  nature, scenery, visible, carriable, written, places,
  settlements, interiors, structures, thoughts, valuable.
  Lista kategorii jest używana automatycznie w latin_sentences.py.
  Możesz podać kilka kategorii; nie musisz zmieniać list rzeczowników
  w innym pliku. Dla każdego słowa istnieją również 3 ogólne wzory
  zdaniowe wynikające z pola 'kind' (person / thing / abstract).

NOWA GRUPA (NP. I DEKLINACJA — ZESTAW 3)
  W LEXICON dopisz nowy klucz:
    'I deklinacja – zestaw 3': [ ...wpisy... ],
  Nie trzeba modyfikować GUI, funkcji budowania pytań ani indeksów słówek.

WAŻNE — NOWE DEKLINACJE (III, IV, V)
  Nowe grupy z tymi nazwami pojawią się automatycznie w trybie SŁÓWKA.
  Aby odmieniać je W ZDANIACH, trzeba dodatkowo opracować ich reguły
  w latin_practice.py (końcówki, tematy i wyjątki). Program nie będzie
  zgadywać nieistniejących reguł.

POZOSTAŁE PLIKI
  latin_practice.py     — silnik odmiany i wyboru pytań.
  latin_sentences.py    — szablony zdań (bez list wyrazów).
  latin_legacy.py       — zachowane ręczne ćwiczenia oryginalnej wersji.
  latin_vocab_trainer.py — Tkinter GUI, nauka, powtórki i statystyki.

Tryb zdań wybiera domyślnie do 3 zdań na rzeczownik na rundę
(parametr per_noun=3 w latin_practice.py), losowo z przygotowanych
konstrukcji. Po błędzie można przejść dalej, a pytanie wraca później.

NOWY TRYB: ODMIANA — FORMY RZECZOWNIKA
  Zaznacz jedną lub więcej grup i wybierz „Odmiana – formy rzeczownika”.
  Domyślnie program pokazuje polskie znaczenie oraz dwa pola:
    - Nominativus singularis (mianownik lp.)
    - Genetivus singularis (dopełniacz lp.)
  Pole „Zakres odmiany” pozwala wybrać jeden z pięciu wariantów:
    1. Nom. sg. + Gen. sg. (2 formy)
    2. Wszystkie przypadki liczby pojedynczej (6 form)
    3. Nom. sg. + Gen. sg. + liczba mnoga (8 form)
    4. Nom. sg. + Gen. sg. + losowy przypadek lp. lub lm. (3 formy)
    5. Pełna odmiana — wszystkie przypadki lp. i lm. (12 form)

  W wariancie 4 dodatkowy przypadek jest losowany spośród 10 pozostałych
  form (poza Nom. sg. i Gen. sg.) i wyświetlany przy polu odpowiedzi.
  Program losuje tylko obsługiwane formy, a przy powtórce błędu zachowuje
  ten sam przypadek. Nowe losowanie następuje po rozpoczęciu nowej rundy.

  Sprawdzenie wymaga poprawności wszystkich dostępnych pól; błędne formy
  są wskazane z właściwymi odpowiedziami. Jedna plansza to jedna próba.
  Powtarzanie błędnych działa tak jak w pozostałych trybach.
  Dla nieregularnych wyrazów, których pewnych form silnik jeszcze nie
  obsługuje (np. liczba mnoga „deus”), pola te są wyłączone.

  Dodawanie rzeczowników i grup nadal odbywa się wyłącznie w latin_data.py.
  Obsługiwane odmiany w nowym trybie: I i II deklinacja. Nowe deklinacje
  wymagają rozszerzenia reguł w latin_practice.py.

ETYKIETY PRZYPADKÓW W TRYBIE ODMIANY
  Nazwa łacińska jest podana jako pierwsza, a polska w nawiasie:
  Nominativus [mianownik], Genetivus [dopełniacz],
  Dativus [celownik], Accusativus [biernik],
  Ablativus [narzędnik], Vocativus [wołacz].
  Nazwy są używane także przy prezentowaniu błędnych odpowiedzi.
