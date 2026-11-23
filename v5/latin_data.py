"""JEDYNE miejsce edycji słownictwa: wszystkie grupy, formy i kategorie zdań.

Każdy wpis ma postać:
  (łacina, polski, rodzaj m/f/n, Gen. sg., polskie_formy, typ, kategorie[, dodatkowe_formy])

polskie_formy: (mian.sg, bier.sg, dop.sg, forma po 'o/w', mian.pl, bier.pl)
Niedostępne formy można zapisać jako None.
Kategorie (tags) sterują doborem pasujących zdań w latin_sentences.py.
Dodatkowe_formy: opcjonalny słownik dat_sg, dat_pl, gen_pl, abl_pl, voc_sg, voc_pl.
Aby dodać słowo do istniejącej deklinacji, skopiuj jeden wpis, zmień dane i
przypisz kategorie (np. individuals, learners, visible, thoughts, nature).
Aby dodać kolejną grupę 20 słów, dopisz nowy klucz do LEXICON.
W trybie słówek nowa grupa pojawi się automatycznie w GUI.
Tryb zdań wymaga reguł odmiany dla danej deklinacji; obecnie I i II.
"""

LEXICON = {
    'I deklinacja': [
        ('puella', 'dziewczyna', 'f', 'puellae', ('dziewczyna', 'dziewczynę', 'dziewczyny', 'dziewczynie', 'dziewczęta', 'dziewczęta'), 'person', ('people', 'individuals', 'learners', 'writers', 'nom_active'), {'dat_sg': 'dziewczynie', 'dat_pl': 'dziewczętom', 'gen_pl': 'dziewcząt', 'abl_pl': 'dziewczętami', 'voc_sg': 'dziewczyno', 'voc_pl': 'dziewczęta'}),
        ('rosa', 'róża', 'f', 'rosae', ('róża', 'różę', 'róży', 'róży', 'róże', 'róże'), 'thing', ('nature', 'visible', 'carriable', 'everyday'), {'gen_pl': 'róż', 'abl_pl': 'różami'}),
        ('aqua', 'woda', 'f', 'aquae', ('woda', 'wodę', 'wody', 'wodzie', None, None), 'thing', ('nature', 'carriable', 'everyday')),
        ('terra', 'ziemia', 'f', 'terrae', ('ziemia', 'ziemię', 'ziemi', 'ziemi', 'ziemie', 'ziemie'), 'thing', ('nature', 'places'), {'gen_pl': 'ziem', 'abl_pl': 'ziemiami'}),
        ('via', 'droga', 'f', 'viae', ('droga', 'drogę', 'drogi', 'drodze', 'drogi', 'drogi'), 'thing', ('nature', 'scenery', 'visible', 'places'), {'gen_pl': 'dróg', 'abl_pl': 'drogami'}),
        ('silva', 'las', 'f', 'silvae', ('las', 'las', 'lasu', 'lesie', 'lasy', 'lasy'), 'thing', ('nature', 'scenery', 'visible', 'places', 'interiors'), {'gen_pl': 'lasów', 'abl_pl': 'lasami'}),
        ('femina', 'kobieta', 'f', 'feminae', ('kobieta', 'kobietę', 'kobiety', 'kobiecie', 'kobiety', 'kobiety'), 'person', ('people', 'individuals', 'nom_active'), {'dat_sg': 'kobiecie', 'dat_pl': 'kobietom', 'gen_pl': 'kobiet', 'abl_pl': 'kobietami', 'voc_sg': 'kobieto', 'voc_pl': 'kobiety'}),
        ('vita', 'życie', 'f', 'vitae', ('życie', 'życie', 'życia', 'życiu', None, None), 'abstract', ('thoughts',)),
        ('insula', 'wyspa', 'f', 'insulae', ('wyspa', 'wyspę', 'wyspy', 'wyspie', 'wyspy', 'wyspy'), 'thing', ('nature', 'scenery', 'visible', 'places', 'settlements'), {'gen_pl': 'wysp', 'abl_pl': 'wyspami'}),
        ('patria', 'ojczyzna', 'f', 'patriae', ('ojczyzna', 'ojczyznę', 'ojczyzny', 'ojczyźnie', 'ojczyzny', 'ojczyzny'), 'abstract', ('places', 'settlements', 'thoughts'), {'gen_pl': 'ojczyzn', 'abl_pl': 'ojczyznami'}),
        ('familia', 'rodzina', 'f', 'familiae', ('rodzina', 'rodzinę', 'rodziny', 'rodzinie', 'rodziny', 'rodziny'), 'person', ('people',), {'dat_sg': 'rodzinie', 'dat_pl': 'rodzinom', 'gen_pl': 'rodzin', 'abl_pl': 'rodzinami', 'voc_sg': 'rodzino', 'voc_pl': 'rodziny'}),
        ('amica', 'przyjaciółka', 'f', 'amicae', ('przyjaciółka', 'przyjaciółkę', 'przyjaciółki', 'przyjaciółce', 'przyjaciółki', 'przyjaciółki'), 'person', ('people', 'individuals', 'learners'), {'dat_sg': 'przyjaciółce', 'dat_pl': 'przyjaciółkom', 'gen_pl': 'przyjaciółek', 'abl_pl': 'przyjaciółkami', 'voc_sg': 'przyjaciółko', 'voc_pl': 'przyjaciółki'}),
        ('filia', 'córka', 'f', 'filiae', ('córka', 'córkę', 'córki', 'córce', 'córki', 'córki'), 'person', ('people', 'individuals', 'learners', 'nom_active'), {'dat_sg': 'córce', 'dat_pl': 'córkom', 'gen_pl': 'córek', 'abl_pl': 'córkami', 'voc_sg': 'córko', 'voc_pl': 'córki'}),
        ('villa', 'dom wiejski; willa', 'f', 'villae', ('willa', 'willę', 'willi', 'willi', 'wille', 'wille'), 'thing', ('scenery', 'visible', 'places', 'settlements', 'interiors', 'structures'), {'gen_pl': 'willi', 'abl_pl': 'willami'}),
        ('porta', 'brama', 'f', 'portae', ('brama', 'bramę', 'bramy', 'bramie', 'bramy', 'bramy'), 'thing', ('scenery', 'visible', 'places', 'structures'), {'gen_pl': 'bram', 'abl_pl': 'bramami'}),
        ('stella', 'gwiazda', 'f', 'stellae', ('gwiazda', 'gwiazdę', 'gwiazdy', 'gwieździe', 'gwiazdy', 'gwiazdy'), 'thing', ('nature', 'scenery', 'visible'), {'gen_pl': 'gwiazd', 'abl_pl': 'gwiazdami'}),
        ('luna', 'księżyc', 'f', 'lunae', ('księżyc', 'księżyc', 'księżyca', 'księżycu', None, None), 'thing', ('nature', 'scenery', 'visible')),
        ('cura', 'troska; opieka', 'f', 'curae', ('troska', 'troskę', 'troski', 'trosce', 'troski', 'troski'), 'abstract', ('thoughts',), {'gen_pl': 'trosk', 'abl_pl': 'troskami'}),
        ('nauta', 'żeglarz', 'm', 'nautae', ('żeglarz', 'żeglarza', 'żeglarza', 'żeglarzu', 'żeglarze', 'żeglarzy'), 'person', ('people', 'individuals', 'travelers', 'nom_active'), {'dat_sg': 'żeglarzowi', 'dat_pl': 'żeglarzom', 'gen_pl': 'żeglarzy', 'abl_pl': 'żeglarzami', 'voc_sg': 'żeglarzu', 'voc_pl': 'żeglarze'}),
        ('poeta', 'poeta', 'm', 'poetae', ('poeta', 'poetę', 'poety', 'poecie', 'poeci', 'poetów'), 'person', ('people', 'individuals', 'writers', 'nom_active'), {'dat_sg': 'poecie', 'dat_pl': 'poetom', 'gen_pl': 'poetów', 'abl_pl': 'poetami', 'voc_sg': 'poeto', 'voc_pl': 'poeci'}),
    ],
    'II deklinacja': [
        ('servus', 'niewolnik', 'm', 'servi', ('niewolnik', 'niewolnika', 'niewolnika', 'niewolniku', 'niewolnicy', 'niewolników'), 'person', ('people', 'individuals', 'travelers', 'nom_active'), {'dat_sg': 'niewolnikowi', 'dat_pl': 'niewolnikom', 'gen_pl': 'niewolników', 'abl_pl': 'niewolnikami', 'voc_sg': 'niewolniku', 'voc_pl': 'niewolnicy'}),
        ('dominus', 'pan; właściciel', 'm', 'domini', ('pan', 'pana', 'pana', 'panu', 'panowie', 'panów'), 'person', ('people', 'individuals', 'leaders', 'nom_active'), {'dat_sg': 'panu', 'dat_pl': 'panom', 'gen_pl': 'panów', 'abl_pl': 'panami', 'voc_sg': 'panie', 'voc_pl': 'panowie'}),
        ('amicus', 'przyjaciel', 'm', 'amici', ('przyjaciel', 'przyjaciela', 'przyjaciela', 'przyjacielu', 'przyjaciele', 'przyjaciół'), 'person', ('people', 'individuals', 'learners', 'travelers', 'nom_active'), {'dat_sg': 'przyjacielowi', 'dat_pl': 'przyjaciołom', 'gen_pl': 'przyjaciół', 'abl_pl': 'przyjaciółmi', 'voc_sg': 'przyjacielu', 'voc_pl': 'przyjaciele'}),
        ('puer', 'chłopiec', 'm', 'pueri', ('chłopiec', 'chłopca', 'chłopca', 'chłopcu', 'chłopcy', 'chłopców'), 'person', ('people', 'individuals', 'learners', 'travelers', 'writers', 'nom_active'), {'dat_sg': 'chłopcu', 'dat_pl': 'chłopcom', 'gen_pl': 'chłopców', 'abl_pl': 'chłopcami', 'voc_sg': 'chłopcze', 'voc_pl': 'chłopcy'}),
        ('ager', 'pole', 'm', 'agri', ('pole', 'pole', 'pola', 'polu', 'pola', 'pola'), 'thing', ('nature', 'scenery', 'visible', 'places'), {'gen_pl': 'pól', 'abl_pl': 'polami'}),
        ('filius', 'syn', 'm', 'filii', ('syn', 'syna', 'syna', 'synu', 'synowie', 'synów'), 'person', ('people', 'individuals', 'nom_active'), {'dat_sg': 'synowi', 'dat_pl': 'synom', 'gen_pl': 'synów', 'abl_pl': 'synami', 'voc_sg': 'synu', 'voc_pl': 'synowie'}),
        ('equus', 'koń', 'm', 'equi', ('koń', 'konia', 'konia', 'koniu', 'konie', 'konie'), 'thing', ('nature', 'visible'), {'gen_pl': 'koni', 'abl_pl': 'końmi'}),
        ('magister', 'nauczyciel', 'm', 'magistri', ('nauczyciel', 'nauczyciela', 'nauczyciela', 'nauczycielu', 'nauczyciele', 'nauczycieli'), 'person', ('people', 'individuals', 'writers', 'leaders', 'nom_active'), {'dat_sg': 'nauczycielowi', 'dat_pl': 'nauczycielom', 'gen_pl': 'nauczycieli', 'abl_pl': 'nauczycielami', 'voc_sg': 'nauczycielu', 'voc_pl': 'nauczyciele'}),
        ('populus', 'lud; naród', 'm', 'populi', ('lud', 'lud', 'ludu', 'ludzie', 'ludy', 'ludy'), 'person', ()),
        ('hortus', 'ogród', 'm', 'horti', ('ogród', 'ogród', 'ogrodu', 'ogrodzie', 'ogrody', 'ogrody'), 'thing', ('nature', 'scenery', 'visible', 'places', 'interiors'), {'gen_pl': 'ogrodów', 'abl_pl': 'ogrodami'}),
        ('deus', 'bóg', 'm', 'dei', ('bóg', 'boga', 'boga', 'bogu', None, None), 'person', ()),
        ('locus', 'miejsce', 'm', 'loci', ('miejsce', 'miejsce', 'miejsca', 'miejscu', 'miejsca', 'miejsca'), 'thing', ('places',), {'gen_pl': 'miejsc', 'abl_pl': 'miejscami'}),
        ('animus', 'duch; umysł', 'm', 'animi', ('duch', 'ducha', 'ducha', 'duchu', 'duchy', 'duchy'), 'abstract', ('thoughts',)),
        ('liber', 'książka', 'm', 'libri', ('książka', 'książkę', 'książki', 'książce', 'książki', 'książki'), 'thing', ('carriable', 'written', 'valuable', 'everyday'), {'gen_pl': 'książek', 'abl_pl': 'książkami'}),
        ('bellum', 'wojna', 'n', 'belli', ('wojna', 'wojnę', 'wojny', 'wojnie', 'wojny', 'wojny'), 'abstract', ('thoughts',), {'gen_pl': 'wojen', 'abl_pl': 'wojnami'}),
        ('templum', 'świątynia', 'n', 'templi', ('świątynia', 'świątynię', 'świątyni', 'świątyni', 'świątynie', 'świątynie'), 'thing', ('scenery', 'visible', 'places', 'interiors', 'structures'), {'gen_pl': 'świątyń', 'abl_pl': 'świątyniami'}),
        ('donum', 'dar; prezent', 'n', 'doni', ('dar', 'dar', 'daru', 'darze', 'dary', 'dary'), 'thing', ('carriable', 'valuable', 'everyday'), {'gen_pl': 'darów', 'abl_pl': 'darami'}),
        ('verbum', 'słowo', 'n', 'verbi', ('słowo', 'słowo', 'słowa', 'słowie', 'słowa', 'słowa'), 'thing', ('carriable', 'written', 'everyday'), {'gen_pl': 'słów', 'abl_pl': 'słowami'}),
        ('oppidum', 'miasto; miasteczko', 'n', 'oppidi', ('miasteczko', 'miasteczko', 'miasteczka', 'miasteczku', 'miasteczka', 'miasteczka'), 'thing', ('scenery', 'visible', 'places', 'settlements', 'interiors', 'structures'), {'gen_pl': 'miasteczek', 'abl_pl': 'miasteczkami'}),
        ('periculum', 'niebezpieczeństwo', 'n', 'periculi', ('niebezpieczeństwo', 'niebezpieczeństwo', 'niebezpieczeństwa', 'niebezpieczeństwie', 'niebezpieczeństwa', 'niebezpieczeństwa'), 'abstract', ('thoughts',), {'gen_pl': 'niebezpieczeństw', 'abl_pl': 'niebezpieczeństwami'}),
    ],
    'I deklinacja – zestaw 2': [
        ('ancilla', 'służąca', 'f', 'ancillae', ('służąca', 'służącą', 'służącej', 'służącej', 'służące', 'służące'), 'person', ('people', 'individuals', 'nom_active'), {'dat_sg': 'służącej', 'dat_pl': 'służącym', 'gen_pl': 'służących', 'abl_pl': 'służącymi', 'voc_sg': 'służąca', 'voc_pl': 'służące'}),
        ('domina', 'pani', 'f', 'dominae', ('pani', 'panią', 'pani', 'pani', 'panie', 'panie'), 'person', ('people', 'individuals', 'leaders', 'nom_active'), {'dat_sg': 'pani', 'dat_pl': 'paniom', 'gen_pl': 'pań', 'abl_pl': 'paniami', 'voc_sg': 'pani', 'voc_pl': 'panie'}),
        ('regina', 'królowa', 'f', 'reginae', ('królowa', 'królową', 'królowej', 'królowej', 'królowe', 'królowe'), 'person', ('people', 'individuals', 'leaders', 'nom_active'), {'dat_sg': 'królowej', 'dat_pl': 'królowym', 'gen_pl': 'królowych', 'abl_pl': 'królowymi', 'voc_sg': 'królowo', 'voc_pl': 'królowe'}),
        ('discipula', 'uczennica', 'f', 'discipulae', ('uczennica', 'uczennicę', 'uczennicy', 'uczennicy', 'uczennice', 'uczennice'), 'person', ('people', 'individuals', 'learners', 'writers', 'nom_active'), {'dat_sg': 'uczennicy', 'dat_pl': 'uczennicom', 'gen_pl': 'uczennic', 'abl_pl': 'uczennicami', 'voc_sg': 'uczennico', 'voc_pl': 'uczennice'}),
        ('magistra', 'nauczycielka', 'f', 'magistrae', ('nauczycielka', 'nauczycielkę', 'nauczycielki', 'nauczycielce', 'nauczycielki', 'nauczycielki'), 'person', ('people', 'individuals', 'writers', 'leaders', 'nom_active'), {'dat_sg': 'nauczycielce', 'dat_pl': 'nauczycielkom', 'gen_pl': 'nauczycielek', 'abl_pl': 'nauczycielkami', 'voc_sg': 'nauczycielko', 'voc_pl': 'nauczycielki'}),
        ('agricola', 'rolnik', 'm', 'agricolae', ('rolnik', 'rolnika', 'rolnika', 'rolniku', 'rolnicy', 'rolników'), 'person', ('people', 'individuals', 'travelers', 'nom_active'), {'dat_sg': 'rolnikowi', 'dat_pl': 'rolnikom', 'gen_pl': 'rolników', 'abl_pl': 'rolnikami', 'voc_sg': 'rolniku', 'voc_pl': 'rolnicy'}),
        ('incola', 'mieszkaniec', 'm', 'incolae', ('mieszkaniec', 'mieszkańca', 'mieszkańca', 'mieszkańcu', 'mieszkańcy', 'mieszkańców'), 'person', ('people', 'individuals', 'travelers', 'nom_active'), {'dat_sg': 'mieszkańcowi', 'dat_pl': 'mieszkańcom', 'gen_pl': 'mieszkańców', 'abl_pl': 'mieszkańcami', 'voc_sg': 'mieszkańcu', 'voc_pl': 'mieszkańcy'}),
        ('pecunia', 'pieniądze; majątek', 'f', 'pecuniae', ('majątek', 'majątek', 'majątku', 'majątku', None, None), 'abstract', ('carriable', 'valuable')),
        ('cena', 'posiłek; kolacja', 'f', 'cenae', ('kolacja', 'kolację', 'kolacji', 'kolacji', 'kolacje', 'kolacje'), 'thing', ('everyday',)),
        ('mensa', 'stół', 'f', 'mensae', ('stół', 'stół', 'stołu', 'stole', 'stoły', 'stoły'), 'thing', ('visible', 'structures', 'everyday'), {'gen_pl': 'stołów', 'abl_pl': 'stołami'}),
        ('sella', 'krzesło', 'f', 'sellae', ('krzesło', 'krzesło', 'krzesła', 'krześle', 'krzesła', 'krzesła'), 'thing', ('visible', 'structures', 'everyday'), {'gen_pl': 'krzeseł', 'abl_pl': 'krzesłami'}),
        ('fenestra', 'okno', 'f', 'fenestrae', ('okno', 'okno', 'okna', 'oknie', 'okna', 'okna'), 'thing', ('visible', 'structures', 'everyday'), {'gen_pl': 'okien', 'abl_pl': 'oknami'}),
        ('epistula', 'list', 'f', 'epistulae', ('list', 'list', 'listu', 'liście', 'listy', 'listy'), 'thing', ('carriable', 'written', 'valuable', 'everyday'), {'gen_pl': 'listów', 'abl_pl': 'listami'}),
        ('lingua', 'język', 'f', 'linguae', ('język', 'język', 'języka', 'języku', 'języki', 'języki'), 'thing', (), {'gen_pl': 'języków', 'abl_pl': 'językami'}),
        ('historia', 'historia; opowieść', 'f', 'historiae', ('opowieść', 'opowieść', 'opowieści', 'opowieści', 'opowieści', 'opowieści'), 'thing', ('written', 'thoughts'), {'gen_pl': 'opowieści', 'abl_pl': 'opowieściami'}),
        ('fortuna', 'los; szczęście', 'f', 'fortunae', ('los', 'los', 'losu', 'losie', None, None), 'abstract', ('thoughts',)),
        ('victoria', 'zwycięstwo', 'f', 'victoriae', ('zwycięstwo', 'zwycięstwo', 'zwycięstwa', 'zwycięstwie', 'zwycięstwa', 'zwycięstwa'), 'abstract', ('thoughts',), {'gen_pl': 'zwycięstw', 'abl_pl': 'zwycięstwami'}),
        ('sapientia', 'mądrość', 'f', 'sapientiae', ('mądrość', 'mądrość', 'mądrości', 'mądrości', None, None), 'abstract', ('thoughts',)),
        ('memoria', 'pamięć', 'f', 'memoriae', ('pamięć', 'pamięć', 'pamięci', 'pamięci', None, None), 'abstract', ('thoughts',)),
        ('provincia', 'prowincja', 'f', 'provinciae', ('prowincja', 'prowincję', 'prowincji', 'prowincji', 'prowincje', 'prowincje'), 'thing', ('places', 'settlements', 'interiors'), {'gen_pl': 'prowincji', 'abl_pl': 'prowincjami'}),
    ],
    'II deklinacja – zestaw 2': [
        ('medicus', 'lekarz', 'm', 'medici', ('lekarz', 'lekarza', 'lekarza', 'lekarzu', 'lekarze', 'lekarzy'), 'person', ('people', 'individuals', 'leaders', 'nom_active'), {'dat_sg': 'lekarzowi', 'dat_pl': 'lekarzom', 'gen_pl': 'lekarzy', 'abl_pl': 'lekarzami', 'voc_sg': 'lekarzu', 'voc_pl': 'lekarze'}),
        ('discipulus', 'uczeń', 'm', 'discipuli', ('uczeń', 'ucznia', 'ucznia', 'uczniu', 'uczniowie', 'uczniów'), 'person', ('people', 'individuals', 'learners', 'writers', 'nom_active'), {'dat_sg': 'uczniowi', 'dat_pl': 'uczniom', 'gen_pl': 'uczniów', 'abl_pl': 'uczniami', 'voc_sg': 'uczniu', 'voc_pl': 'uczniowie'}),
        ('faber', 'rzemieślnik', 'm', 'fabri', ('rzemieślnik', 'rzemieślnika', 'rzemieślnika', 'rzemieślniku', 'rzemieślnicy', 'rzemieślników'), 'person', ('people', 'individuals', 'nom_active'), {'dat_sg': 'rzemieślnikowi', 'dat_pl': 'rzemieślnikom', 'gen_pl': 'rzemieślników', 'abl_pl': 'rzemieślnikami', 'voc_sg': 'rzemieślniku', 'voc_pl': 'rzemieślnicy'}),
        ('socius', 'towarzysz', 'm', 'socii', ('towarzysz', 'towarzysza', 'towarzysza', 'towarzyszu', 'towarzysze', 'towarzyszy'), 'person', ('people', 'individuals', 'travelers', 'nom_active'), {'dat_sg': 'towarzyszowi', 'dat_pl': 'towarzyszom', 'gen_pl': 'towarzyszy', 'abl_pl': 'towarzyszami', 'voc_sg': 'towarzyszu', 'voc_pl': 'towarzysze'}),
        ('vicinus', 'sąsiad', 'm', 'vicini', ('sąsiad', 'sąsiada', 'sąsiada', 'sąsiedzie', 'sąsiedzi', 'sąsiadów'), 'person', ('people', 'individuals', 'nom_active'), {'dat_sg': 'sąsiadowi', 'dat_pl': 'sąsiadom', 'gen_pl': 'sąsiadów', 'abl_pl': 'sąsiadami', 'voc_sg': 'sąsiedzie', 'voc_pl': 'sąsiedzi'}),
        ('oculus', 'oko', 'm', 'oculi', ('oko', 'oko', 'oka', 'oku', 'oczy', 'oczy'), 'thing', (), {'gen_pl': 'oczu', 'abl_pl': 'oczami'}),
        ('numerus', 'liczba', 'm', 'numeri', ('liczba', 'liczbę', 'liczby', 'liczbie', 'liczby', 'liczby'), 'thing', (), {'gen_pl': 'liczb', 'abl_pl': 'liczbami'}),
        ('annus', 'rok', 'm', 'anni', ('rok', 'rok', 'roku', 'roku', 'lata', 'lata'), 'thing', (), {'gen_pl': 'lat', 'abl_pl': 'latami'}),
        ('ventus', 'wiatr', 'm', 'venti', ('wiatr', 'wiatr', 'wiatru', 'wietrze', 'wiatry', 'wiatry'), 'thing', ('nature',), {'gen_pl': 'wiatrów', 'abl_pl': 'wiatrami'}),
        ('rivus', 'strumień', 'm', 'rivi', ('strumień', 'strumień', 'strumienia', 'strumieniu', 'strumienie', 'strumienie'), 'thing', ('nature', 'scenery', 'visible'), {'gen_pl': 'strumieni', 'abl_pl': 'strumieniami'}),
        ('murus', 'mur', 'm', 'muri', ('mur', 'mur', 'muru', 'murze', 'mury', 'mury'), 'thing', ('scenery', 'visible', 'structures'), {'gen_pl': 'murów', 'abl_pl': 'murami'}),
        ('gladius', 'miecz', 'm', 'gladii', ('miecz', 'miecz', 'miecza', 'mieczu', 'miecze', 'miecze'), 'thing', ('visible', 'carriable', 'valuable'), {'gen_pl': 'mieczy', 'abl_pl': 'mieczami'}),
        ('nuntius', 'posłaniec', 'm', 'nuntii', ('posłaniec', 'posłańca', 'posłańca', 'posłańcu', 'posłańcy', 'posłańców'), 'person', ('people', 'individuals', 'travelers', 'nom_active'), {'dat_sg': 'posłańcowi', 'dat_pl': 'posłańcom', 'gen_pl': 'posłańców', 'abl_pl': 'posłańcami', 'voc_sg': 'posłańcze', 'voc_pl': 'posłańcy'}),
        ('caelum', 'niebo', 'n', 'caeli', ('niebo', 'niebo', 'nieba', 'niebie', None, None), 'thing', ('nature',)),
        ('signum', 'znak', 'n', 'signi', ('znak', 'znak', 'znaku', 'znaku', 'znaki', 'znaki'), 'thing', ('visible', 'carriable', 'everyday'), {'gen_pl': 'znaków', 'abl_pl': 'znakami'}),
        ('exemplum', 'przykład', 'n', 'exempli', ('przykład', 'przykład', 'przykładu', 'przykładzie', 'przykłady', 'przykłady'), 'thing', ('carriable', 'written'), {'gen_pl': 'przykładów', 'abl_pl': 'przykładami'}),
        ('auxilium', 'pomoc', 'n', 'auxilii', ('pomoc', 'pomoc', 'pomocy', 'pomocy', None, None), 'abstract', ('thoughts',)),
        ('consilium', 'plan; rada', 'n', 'consilii', ('plan', 'plan', 'planu', 'planie', 'plany', 'plany'), 'thing', ('written', 'thoughts'), {'gen_pl': 'planów', 'abl_pl': 'planami'}),
        ('imperium', 'władza; rozkaz', 'n', 'imperii', ('rozkaz', 'rozkaz', 'rozkazu', 'rozkazie', 'rozkazy', 'rozkazy'), 'thing', ('thoughts',), {'gen_pl': 'rozkazów', 'abl_pl': 'rozkazami'}),
        ('argentum', 'srebro', 'n', 'argenti', ('srebro', 'srebro', 'srebra', 'srebrze', None, None), 'thing', ('valuable',)),
    ],
}

# Interfejs listy słówek, wyprowadzany automatycznie z centralnego leksykonu.
WORD_GROUPS = {
    group: [(latin, polish) for latin, polish, *_ in entries]
    for group, entries in LEXICON.items()
}

# Indeks semantyczny używany przez bank zdań. Nie edytuj osobno!
WORDS_BY_TAG = {}
for entries in LEXICON.values():
    for record in entries:
        latin, _polish, _gender, _genitive, _forms, kind, tags = record[:7]
        for tag in set(tags) | {kind}:
            WORDS_BY_TAG.setdefault(tag, set()).add(latin)

def words_with_tag(tag):
    return ' '.join(sorted(WORDS_BY_TAG.get(tag, ())))
