TRENER LACINY - STATYSTYKI

Uruchom: python latin_vocab_trainer.py
Wymagania: Python 3 z Tkinter. Bez dodatkowych bibliotek.

Nowy modul latin_statistics.py zapisuje tylko ukonczone lekcje.
Plik latin_statistics.json jest tworzony automatycznie w tym katalogu
po pierwszej ukonczonej lekcji. Nie kasuj go, jesli chcesz zachowac historie.

Kazdy tryb, wybor grup, kierunek tlumaczenia oraz zakres odmiany maja
oddzielna historie. Nowe grupy i nowe konfiguracje dostaja historie
bez zmian w module statystyk. Nowy tryb musi przekazac konfiguracje
i wynik do wspolnego mechanizmu.

Reset, zamkniecie okna i przerwanie rundy nie zapisuje wyniku.
Pierwsza proba to odpowiedz przed powtorkami; klikniecie "Pokaz odpowiedz"
liczy sie jako blad. W trybie odmiany jedna proba to caly zestaw pol:
jezeli choc jedno pole jest zle, cala proba jest bledna; bledy
poszczegolnych form sa dodatkowo rejestrowane.

Historie mozna przegladac przyciskiem "Pokaz statystyki" na dole po prawej.
