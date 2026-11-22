TRENER LACINY 4.0 — ROZNORODNE ZDANIA
====================================

Uruchomienie:
    python latin_vocab_trainer.py

Wymaga Pythona 3 i biblioteki Tkinter (standardowo w Windows/macOS).
W niektorych dystrybucjach Linuxa trzeba zainstalowac python3-tk.

TRYBY
1) Slowka: polski -> lacina, lacina -> polski, lub oba kierunki.
2) Zdania: polskie zdanie + lacinskie z luka. Przetlumacz i odmien
   polski rzeczownik, wstawiajac jedna forme lacinska.

GRUPY
4 checkboxy po 20 slow — stare i nowe zestawy I i II deklinacji.

ZDANIA
- 113 historycznych cwiczen z wersji 2 (latin_legacy.py).
- Ponad 120 nowych, rekombinowanych konstrukcji (latin_sentences.py).
- Generator wybiera formy z latin_practice.py, semantycznie pasujace
  rzeczowniki i gotowa polska fleksje z latin_extra.py.
- Z kazdego zaznaczonego slowa wybierane jest do 5 zdan na runde.
- Kolejna runda przynosi zwykle inny zestaw.
- Po bledzie widzisz poprawna odpowiedz i mozesz przejsc dalej (Enter).
- Bledne zadanie wraca pozniej w losowym momencie, jesli zaznaczono powtorki.
- Zwykle powtorka jest oddzielona co najmniej 3 innymi pytaniami.
  Przy koncu bardzo malej puli pytan ten odstep nie zawsze jest mozliwy.
- 'Pokaz odpowiedz' dziala analogicznie i tez dodaje zadanie do powtorek.

EDYCJA
latin_data.py        — pierwsze 40 slow
latin_extra.py       — kolejne 40 slow i polska fleksja wszystkich
latin_legacy.py      — oryginalny bank zdan z wersji 2
latin_sentences.py   — szablony tematyczne i ich warunki
latin_practice.py    — generowanie pytan, koncowki deklinacyjne
latin_vocab_trainer.py — Tkinter GUI i logika treningu

Nie tworzymy dowolnych zdan przez laczenie przypadkowych slow.
Nowe slowo trzeba dodac do bazy form, a potem przypisac do pasujacych
semantycznie szablonow (np. PEOPLE, VISIBLE, THOUGHTS), lub dopisac
konkretne zdania. Dzieki temu zachowujemy gramatyke i sens.

UWAGI
Dlugosc samoglosek w lacinskich odpowiedziach jest pomijana.
Nie wszystkie znaczenia jednego wyrazu sa uwzglednione naraz.
System cwiczy odmiane w zdaniach, ale nie jest pelnym tlumaczem.
