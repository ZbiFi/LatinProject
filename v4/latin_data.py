"""JEDYNE miejsce edycji słownictwa: wszystkie grupy, formy i kategorie zdań.

Każdy wpis ma postać:
  (łacina, polski, rodzaj m/f/n, Gen. sg., polskie_formy, typ, kategorie)

polskie_formy: (mian.sg, bier.sg, dop.sg, forma po 'o/w', mian.pl, bier.pl)
Niedostępne formy można zapisać jako None.
Kategorie (tags) sterują doborem pasujących zdań w latin_sentences.py.
Aby dodać słowo do istniejącej deklinacji, skopiuj jeden wpis, zmień dane i
przypisz kategorie (np. individuals, learners, visible, thoughts, nature).
Aby dodać kolejną grupę 20 słów, dopisz nowy klucz do LEXICON.
W trybie słówek nowa grupa pojawi się automatycznie w GUI.
Tryb zdań wymaga reguł odmiany dla danej deklinacji; obecnie I i II.
"""

LEXICON = {
    'I deklinacja': [
        ('puella', 'dziewczyna', 'f', 'puellae', ('dziewczyna', 'dziewczynę', 'dziewczyny', 'dziewczynie', 'dziewczęta', 'dziewczęta'), 'person', ('people', 'individuals', 'learners', 'writers', 'nom_active')),
        ('rosa', 'róża', 'f', 'rosae', ('róża', 'różę', 'róży', 'róży', 'róże', 'róże'), 'thing', ('nature', 'visible', 'carriable', 'everyday')),
        ('aqua', 'woda', 'f', 'aquae', ('woda', 'wodę', 'wody', 'wodzie', None, None), 'thing', ('nature', 'carriable', 'everyday')),
        ('terra', 'ziemia', 'f', 'terrae', ('ziemia', 'ziemię', 'ziemi', 'ziemi', 'ziemie', 'ziemie'), 'thing', ('nature', 'places')),
        ('via', 'droga', 'f', 'viae', ('droga', 'drogę', 'drogi', 'drodze', 'drogi', 'drogi'), 'thing', ('nature', 'scenery', 'visible', 'places')),
        ('silva', 'las', 'f', 'silvae', ('las', 'las', 'lasu', 'lesie', 'lasy', 'lasy'), 'thing', ('nature', 'scenery', 'visible', 'places', 'interiors')),
        ('femina', 'kobieta', 'f', 'feminae', ('kobieta', 'kobietę', 'kobiety', 'kobiecie', 'kobiety', 'kobiety'), 'person', ('people', 'individuals', 'nom_active')),
        ('vita', 'życie', 'f', 'vitae', ('życie', 'życie', 'życia', 'życiu', None, None), 'abstract', ('thoughts',)),
        ('insula', 'wyspa', 'f', 'insulae', ('wyspa', 'wyspę', 'wyspy', 'wyspie', 'wyspy', 'wyspy'), 'thing', ('nature', 'scenery', 'visible', 'places', 'settlements')),
        ('patria', 'ojczyzna', 'f', 'patriae', ('ojczyzna', 'ojczyznę', 'ojczyzny', 'ojczyźnie', 'ojczyzny', 'ojczyzny'), 'abstract', ('places', 'settlements', 'thoughts')),
        ('familia', 'rodzina', 'f', 'familiae', ('rodzina', 'rodzinę', 'rodziny', 'rodzinie', 'rodziny', 'rodziny'), 'person', ('people',)),
        ('amica', 'przyjaciółka', 'f', 'amicae', ('przyjaciółka', 'przyjaciółkę', 'przyjaciółki', 'przyjaciółce', 'przyjaciółki', 'przyjaciółki'), 'person', ('people', 'individuals', 'learners')),
        ('filia', 'córka', 'f', 'filiae', ('córka', 'córkę', 'córki', 'córce', 'córki', 'córki'), 'person', ('people', 'individuals', 'learners', 'nom_active')),
        ('villa', 'dom wiejski; willa', 'f', 'villae', ('willa', 'willę', 'willi', 'willi', 'wille', 'wille'), 'thing', ('scenery', 'visible', 'places', 'settlements', 'interiors', 'structures')),
        ('porta', 'brama', 'f', 'portae', ('brama', 'bramę', 'bramy', 'bramie', 'bramy', 'bramy'), 'thing', ('scenery', 'visible', 'places', 'structures')),
        ('stella', 'gwiazda', 'f', 'stellae', ('gwiazda', 'gwiazdę', 'gwiazdy', 'gwieździe', 'gwiazdy', 'gwiazdy'), 'thing', ('nature', 'scenery', 'visible')),
        ('luna', 'księżyc', 'f', 'lunae', ('księżyc', 'księżyc', 'księżyca', 'księżycu', None, None), 'thing', ('nature', 'scenery', 'visible')),
        ('cura', 'troska; opieka', 'f', 'curae', ('troska', 'troskę', 'troski', 'trosce', 'troski', 'troski'), 'abstract', ('thoughts',)),
        ('nauta', 'żeglarz', 'm', 'nautae', ('żeglarz', 'żeglarza', 'żeglarza', 'żeglarzu', 'żeglarze', 'żeglarzy'), 'person', ('people', 'individuals', 'travelers', 'nom_active')),
        ('poeta', 'poeta', 'm', 'poetae', ('poeta', 'poetę', 'poety', 'poecie', 'poeci', 'poetów'), 'person', ('people', 'individuals', 'writers', 'nom_active')),
    ],
    'II deklinacja': [
        ('servus', 'niewolnik', 'm', 'servi', ('niewolnik', 'niewolnika', 'niewolnika', 'niewolniku', 'niewolnicy', 'niewolników'), 'person', ('people', 'individuals', 'travelers', 'nom_active')),
        ('dominus', 'pan; właściciel', 'm', 'domini', ('pan', 'pana', 'pana', 'panu', 'panowie', 'panów'), 'person', ('people', 'individuals', 'leaders', 'nom_active')),
        ('amicus', 'przyjaciel', 'm', 'amici', ('przyjaciel', 'przyjaciela', 'przyjaciela', 'przyjacielu', 'przyjaciele', 'przyjaciół'), 'person', ('people', 'individuals', 'learners', 'travelers', 'nom_active')),
        ('puer', 'chłopiec', 'm', 'pueri', ('chłopiec', 'chłopca', 'chłopca', 'chłopcu', 'chłopcy', 'chłopców'), 'person', ('people', 'individuals', 'learners', 'travelers', 'writers', 'nom_active')),
        ('ager', 'pole', 'm', 'agri', ('pole', 'pole', 'pola', 'polu', 'pola', 'pola'), 'thing', ('nature', 'scenery', 'visible', 'places')),
        ('filius', 'syn', 'm', 'filii', ('syn', 'syna', 'syna', 'synu', 'synowie', 'synów'), 'person', ('people', 'individuals', 'nom_active')),
        ('equus', 'koń', 'm', 'equi', ('koń', 'konia', 'konia', 'koniu', 'konie', 'konie'), 'thing', ('nature', 'visible')),
        ('magister', 'nauczyciel', 'm', 'magistri', ('nauczyciel', 'nauczyciela', 'nauczyciela', 'nauczycielu', 'nauczyciele', 'nauczycieli'), 'person', ('people', 'individuals', 'writers', 'leaders', 'nom_active')),
        ('populus', 'lud; naród', 'm', 'populi', ('lud', 'lud', 'ludu', 'ludzie', 'ludy', 'ludy'), 'person', ()),
        ('hortus', 'ogród', 'm', 'horti', ('ogród', 'ogród', 'ogrodu', 'ogrodzie', 'ogrody', 'ogrody'), 'thing', ('nature', 'scenery', 'visible', 'places', 'interiors')),
        ('deus', 'bóg', 'm', 'dei', ('bóg', 'boga', 'boga', 'bogu', None, None), 'person', ()),
        ('locus', 'miejsce', 'm', 'loci', ('miejsce', 'miejsce', 'miejsca', 'miejscu', 'miejsca', 'miejsca'), 'thing', ('places',)),
        ('animus', 'duch; umysł', 'm', 'animi', ('duch', 'ducha', 'ducha', 'duchu', 'duchy', 'duchy'), 'abstract', ('thoughts',)),
        ('liber', 'książka', 'm', 'libri', ('książka', 'książkę', 'książki', 'książce', 'książki', 'książki'), 'thing', ('carriable', 'written', 'valuable', 'everyday')),
        ('bellum', 'wojna', 'n', 'belli', ('wojna', 'wojnę', 'wojny', 'wojnie', 'wojny', 'wojny'), 'abstract', ('thoughts',)),
        ('templum', 'świątynia', 'n', 'templi', ('świątynia', 'świątynię', 'świątyni', 'świątyni', 'świątynie', 'świątynie'), 'thing', ('scenery', 'visible', 'places', 'interiors', 'structures')),
        ('donum', 'dar; prezent', 'n', 'doni', ('dar', 'dar', 'daru', 'darze', 'dary', 'dary'), 'thing', ('carriable', 'valuable', 'everyday')),
        ('verbum', 'słowo', 'n', 'verbi', ('słowo', 'słowo', 'słowa', 'słowie', 'słowa', 'słowa'), 'thing', ('carriable', 'written', 'everyday')),
        ('oppidum', 'miasto; miasteczko', 'n', 'oppidi', ('miasteczko', 'miasteczko', 'miasteczka', 'miasteczku', 'miasteczka', 'miasteczka'), 'thing', ('scenery', 'visible', 'places', 'settlements', 'interiors', 'structures')),
        ('periculum', 'niebezpieczeństwo', 'n', 'periculi', ('niebezpieczeństwo', 'niebezpieczeństwo', 'niebezpieczeństwa', 'niebezpieczeństwie', 'niebezpieczeństwa', 'niebezpieczeństwa'), 'abstract', ('thoughts',)),
    ],
    'I deklinacja – zestaw 2': [
        ('ancilla', 'służąca', 'f', 'ancillae', ('służąca', 'służącą', 'służącej', 'służącej', 'służące', 'służące'), 'person', ('people', 'individuals', 'nom_active')),
        ('domina', 'pani', 'f', 'dominae', ('pani', 'panią', 'pani', 'pani', 'panie', 'panie'), 'person', ('people', 'individuals', 'leaders', 'nom_active')),
        ('regina', 'królowa', 'f', 'reginae', ('królowa', 'królową', 'królowej', 'królowej', 'królowe', 'królowe'), 'person', ('people', 'individuals', 'leaders', 'nom_active')),
        ('discipula', 'uczennica', 'f', 'discipulae', ('uczennica', 'uczennicę', 'uczennicy', 'uczennicy', 'uczennice', 'uczennice'), 'person', ('people', 'individuals', 'learners', 'writers', 'nom_active')),
        ('magistra', 'nauczycielka', 'f', 'magistrae', ('nauczycielka', 'nauczycielkę', 'nauczycielki', 'nauczycielce', 'nauczycielki', 'nauczycielki'), 'person', ('people', 'individuals', 'writers', 'leaders', 'nom_active')),
        ('agricola', 'rolnik', 'm', 'agricolae', ('rolnik', 'rolnika', 'rolnika', 'rolniku', 'rolnicy', 'rolników'), 'person', ('people', 'individuals', 'travelers', 'nom_active')),
        ('incola', 'mieszkaniec', 'm', 'incolae', ('mieszkaniec', 'mieszkańca', 'mieszkańca', 'mieszkańcu', 'mieszkańcy', 'mieszkańców'), 'person', ('people', 'individuals', 'travelers', 'nom_active')),
        ('pecunia', 'pieniądze; majątek', 'f', 'pecuniae', ('majątek', 'majątek', 'majątku', 'majątku', None, None), 'abstract', ('carriable', 'valuable')),
        ('cena', 'posiłek; kolacja', 'f', 'cenae', ('kolacja', 'kolację', 'kolacji', 'kolacji', 'kolacje', 'kolacje'), 'thing', ('everyday',)),
        ('mensa', 'stół', 'f', 'mensae', ('stół', 'stół', 'stołu', 'stole', 'stoły', 'stoły'), 'thing', ('visible', 'structures', 'everyday')),
        ('sella', 'krzesło', 'f', 'sellae', ('krzesło', 'krzesło', 'krzesła', 'krześle', 'krzesła', 'krzesła'), 'thing', ('visible', 'structures', 'everyday')),
        ('fenestra', 'okno', 'f', 'fenestrae', ('okno', 'okno', 'okna', 'oknie', 'okna', 'okna'), 'thing', ('visible', 'structures', 'everyday')),
        ('epistula', 'list', 'f', 'epistulae', ('list', 'list', 'listu', 'liście', 'listy', 'listy'), 'thing', ('carriable', 'written', 'valuable', 'everyday')),
        ('lingua', 'język', 'f', 'linguae', ('język', 'język', 'języka', 'języku', 'języki', 'języki'), 'thing', ()),
        ('historia', 'historia; opowieść', 'f', 'historiae', ('opowieść', 'opowieść', 'opowieści', 'opowieści', 'opowieści', 'opowieści'), 'thing', ('written', 'thoughts')),
        ('fortuna', 'los; szczęście', 'f', 'fortunae', ('los', 'los', 'losu', 'losie', None, None), 'abstract', ('thoughts',)),
        ('victoria', 'zwycięstwo', 'f', 'victoriae', ('zwycięstwo', 'zwycięstwo', 'zwycięstwa', 'zwycięstwie', 'zwycięstwa', 'zwycięstwa'), 'abstract', ('thoughts',)),
        ('sapientia', 'mądrość', 'f', 'sapientiae', ('mądrość', 'mądrość', 'mądrości', 'mądrości', None, None), 'abstract', ('thoughts',)),
        ('memoria', 'pamięć', 'f', 'memoriae', ('pamięć', 'pamięć', 'pamięci', 'pamięci', None, None), 'abstract', ('thoughts',)),
        ('provincia', 'prowincja', 'f', 'provinciae', ('prowincja', 'prowincję', 'prowincji', 'prowincji', 'prowincje', 'prowincje'), 'thing', ('places', 'settlements', 'interiors')),
    ],
    'II deklinacja – zestaw 2': [
        ('medicus', 'lekarz', 'm', 'medici', ('lekarz', 'lekarza', 'lekarza', 'lekarzu', 'lekarze', 'lekarzy'), 'person', ('people', 'individuals', 'leaders', 'nom_active')),
        ('discipulus', 'uczeń', 'm', 'discipuli', ('uczeń', 'ucznia', 'ucznia', 'uczniu', 'uczniowie', 'uczniów'), 'person', ('people', 'individuals', 'learners', 'writers', 'nom_active')),
        ('faber', 'rzemieślnik', 'm', 'fabri', ('rzemieślnik', 'rzemieślnika', 'rzemieślnika', 'rzemieślniku', 'rzemieślnicy', 'rzemieślników'), 'person', ('people', 'individuals', 'nom_active')),
        ('socius', 'towarzysz', 'm', 'socii', ('towarzysz', 'towarzysza', 'towarzysza', 'towarzyszu', 'towarzysze', 'towarzyszy'), 'person', ('people', 'individuals', 'travelers', 'nom_active')),
        ('vicinus', 'sąsiad', 'm', 'vicini', ('sąsiad', 'sąsiada', 'sąsiada', 'sąsiedzie', 'sąsiedzi', 'sąsiadów'), 'person', ('people', 'individuals', 'nom_active')),
        ('oculus', 'oko', 'm', 'oculi', ('oko', 'oko', 'oka', 'oku', 'oczy', 'oczy'), 'thing', ()),
        ('numerus', 'liczba', 'm', 'numeri', ('liczba', 'liczbę', 'liczby', 'liczbie', 'liczby', 'liczby'), 'thing', ()),
        ('annus', 'rok', 'm', 'anni', ('rok', 'rok', 'roku', 'roku', 'lata', 'lata'), 'thing', ()),
        ('ventus', 'wiatr', 'm', 'venti', ('wiatr', 'wiatr', 'wiatru', 'wietrze', 'wiatry', 'wiatry'), 'thing', ('nature',)),
        ('rivus', 'strumień', 'm', 'rivi', ('strumień', 'strumień', 'strumienia', 'strumieniu', 'strumienie', 'strumienie'), 'thing', ('nature', 'scenery', 'visible')),
        ('murus', 'mur', 'm', 'muri', ('mur', 'mur', 'muru', 'murze', 'mury', 'mury'), 'thing', ('scenery', 'visible', 'structures')),
        ('gladius', 'miecz', 'm', 'gladii', ('miecz', 'miecz', 'miecza', 'mieczu', 'miecze', 'miecze'), 'thing', ('visible', 'carriable', 'valuable')),
        ('nuntius', 'posłaniec', 'm', 'nuntii', ('posłaniec', 'posłańca', 'posłańca', 'posłańcu', 'posłańcy', 'posłańców'), 'person', ('people', 'individuals', 'travelers', 'nom_active')),
        ('caelum', 'niebo', 'n', 'caeli', ('niebo', 'niebo', 'nieba', 'niebie', None, None), 'thing', ('nature',)),
        ('signum', 'znak', 'n', 'signi', ('znak', 'znak', 'znaku', 'znaku', 'znaki', 'znaki'), 'thing', ('visible', 'carriable', 'everyday')),
        ('exemplum', 'przykład', 'n', 'exempli', ('przykład', 'przykład', 'przykładu', 'przykładzie', 'przykłady', 'przykłady'), 'thing', ('carriable', 'written')),
        ('auxilium', 'pomoc', 'n', 'auxilii', ('pomoc', 'pomoc', 'pomocy', 'pomocy', None, None), 'abstract', ('thoughts',)),
        ('consilium', 'plan; rada', 'n', 'consilii', ('plan', 'plan', 'planu', 'planie', 'plany', 'plany'), 'thing', ('written', 'thoughts')),
        ('imperium', 'władza; rozkaz', 'n', 'imperii', ('rozkaz', 'rozkaz', 'rozkazu', 'rozkazie', 'rozkazy', 'rozkazy'), 'thing', ('thoughts',)),
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
    for latin, _polish, _gender, _genitive, _forms, kind, tags in entries:
        for tag in set(tags) | {kind}:
            WORDS_BY_TAG.setdefault(tag, set()).add(latin)

def words_with_tag(tag):
    return ' '.join(sorted(WORDS_BY_TAG.get(tag, ())))
