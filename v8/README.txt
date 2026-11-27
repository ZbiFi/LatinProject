TRENER ŁACINY — III DEKLINACJA (7 ZESTAWÓW / 140 RZECZOWNIKÓW)

Uruchomienie: python latin_vocab_trainer.py
Wymagania: Python 3 i Tkinter (bez bibliotek zewnętrznych).

Nowa grupa "III deklinacja – zestaw 1" zawiera 20 rzeczowników.
Jest trzecia na liście grup — po podstawowych I i II deklinacji.
Pozostałe 120 rzeczowników i wszystkie dotychczasowe grupy są zachowane.

Nowe słówka działają w trybach: tłumaczenia, zdania oraz odmiana.
Silnik uwzględnia III deklinację rodzaju męskiego, żeńskiego i nijakiego,
a także Gen. pl. -ium dla civis i urbs. Wszystkie formy są bez makronów.

Wszystkie słowa dodaje się wyłącznie w latin_data.py (LEXICON).
Kolejne grupy III deklinacji można dopisać w tym samym pliku.
Dla trudniejszych wyjątków III deklinacji (np. vis, mare, animal)
trzeba wcześniej rozbudować reguły w latin_practice.py.

STATYSTYKI: zachowano plik latin_statistics.json z przesłanej wersji.
Gdy aktualizujesz program w innym katalogu, przenieś swój najnowszy
latin_statistics.json, aby nie utracić wyników nowszych sesji.

Ograniczenie: maksymalnie 50 nowych pytań na rundę; powtórki dodatkowe.
