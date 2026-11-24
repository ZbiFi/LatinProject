TRENER ŁACINY – STATYSTYKI I NOWE ZESTAWY

Uruchomienie: python latin_vocab_trainer.py
Wymagania: Python 3 z Tkinter (bez bibliotek zewnętrznych).

Nowe zestawy:
- I deklinacja – zestaw 3: 20 nowych rzeczowników
- II deklinacja – zestaw 3: 20 nowych rzeczowników
Łącznie: 120 rzeczowników, 6 zestawów po 20 słów.

Limit: do 50 początkowych pytań w każdym trybie (wybór losowy,
bez powtarzania tego samego pytania w puli startowej).
Powtórki błędów są dodatkowe i mogą zwiększyć liczbę prób.

Przycisk "Pokaż statystyki" znajduje się po lewej stronie przycisku
"Rozpocznij / zresetuj" w tym samym wierszu.
W oknie statystyk:
- "Usuń zaznaczony rekord" usuwa jeden wybrany wynik,
- "Resetuj historię tej lekcji" usuwa wyniki całej wybranej konfiguracji.
Obie operacje wymagają potwierdzenia i są nieodwracalne.

Plik latin_statistics.json tworzy się automatycznie obok programu
po ukończeniu lekcji. Historia jest podzielona według trybów, grup
i ustawień. Lekcje przerwane lub zresetowane nie są zapisywane.

WAŻNE PRZY AKTUALIZACJI: Zachowaj dotychczasowy latin_statistics.json
i przenieś go do folderu z nową wersją programu. NIE zastępuj go
pustym plikiem. Format historii jest zgodny z poprzednią wersją.
