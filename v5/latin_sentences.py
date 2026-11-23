"""Bank urozmaiconych, ręcznie sprawdzalnych konstrukcji zdań.

Każdy wpis określa kontekst, a nie pojedynczą odmianę jednego słowa.
Kandydaci są dobierani świadomie semantycznie: brak bezsensownych
kombinacji typu 'księżyc czyta książkę'.

Format: (dozwolone hasła, przypadek, liczba, zdanie LA z ____ ,
         zdanie PL z {x}). {x} jest wstawiane z jawnej fleksji polskiej.
"""
from dataclasses import dataclass

@dataclass(frozen=True)
class Pattern:
    words: frozenset
    case: str
    number: str
    latin: str
    polish: str

PATTERNS = []

def add(words, case, number, latin, polish):
    assert latin.count('____') == 1, latin
    assert (polish.count('{x}') + polish.count('{X}')) == 1, polish
    PATTERNS.append(Pattern(frozenset(words.split()), case, number, latin, polish))

# Kategorie semantyczne pobierane automatycznie z latin_data.py.
from latin_data import words_with_tag
PEOPLE = words_with_tag('people')
INDIVIDUALS = words_with_tag('individuals')
LEARNERS = words_with_tag('learners')
TRAVELERS = words_with_tag('travelers')
WRITERS = words_with_tag('writers')
LEADERS = words_with_tag('leaders')
NATURE = words_with_tag('nature')
SCENERY = words_with_tag('scenery')
VISIBLE = words_with_tag('visible')
CARRIABLE = words_with_tag('carriable')
WRITTEN = words_with_tag('written')
PLACES = words_with_tag('places')
SETTLEMENTS = words_with_tag('settlements')
INTERIORS = words_with_tag('interiors')
STRUCTURES = words_with_tag('structures')
THOUGHTS = words_with_tag('thoughts')
VALUABLE = words_with_tag('valuable')
EVERYDAY = words_with_tag('everyday')
NOM_ACTIVE = words_with_tag('nom_active')

# --- Wykonawcy czynności: Nominativus sing. ---
add(INDIVIDUALS, 'nom','sg','Hodie ____ in foro ambulat.','Dzisiaj {x} spaceruje po forum.')
add(INDIVIDUALS, 'nom','sg','Mane ____ ante portam stat.','Rano {x} stoi przed bramą.')
add(INDIVIDUALS, 'nom','sg','Sub arbore ____ quiescit.','Pod drzewem {x} odpoczywa.')
add(INDIVIDUALS, 'nom','sg','Post cenam ____ domum redit.','Po kolacji {x} wraca do domu.')
add(INDIVIDUALS, 'nom','sg','Nunc ____ aquam bibit.','Teraz {x} pije wodę.')
add(INDIVIDUALS, 'nom','sg','In villa ____ lucernam accendit.','W domu {x} zapala lampę.')
add(INDIVIDUALS, 'nom','sg','In horto ____ rosas spectat.','W ogrodzie {x} ogląda róże.')
add(INDIVIDUALS, 'nom','sg','Cum amicis ____ cenat.','Z przyjaciółmi {x} je kolację.')
add(INDIVIDUALS, 'nom','sg','Ad portam ____ festinat.','Do bramy {x} spieszy.')
add(TRAVELERS, 'nom','sg','Per silvam ____ iter facit.','Przez las {x} odbywa podróż.')
add(TRAVELERS, 'nom','sg','Prope flumen ____ ambulat.','W pobliżu rzeki {x} spaceruje.')
add(WRITERS, 'nom','sg','In tabula ____ verba scribit.','Na tablicy {x} zapisuje słowa.')
add(WRITERS, 'nom','sg','De historia ____ cogitat.','O historii {x} rozmyśla.')
add(LEARNERS, 'nom','sg','In schola ____ magistrum audit.','W szkole {x} słucha nauczyciela.')
add(LEARNERS, 'nom','sg','Post scholam ____ ludere vult.','Po szkole {x} chce się bawić.')
add(LEADERS, 'nom','sg','In aula ____ consilium explicat.','W sali {x} przedstawia plan.')
add(LEADERS, 'nom','sg','Servos ____ convocat.','{X} zwołuje niewolników.')

# --- Nominativus pluralis: inne czasowniki i sceny ---
add(INDIVIDUALS, 'nom','pl','____ prope portam exspectant.','{X} czekają przy bramie.')
add(INDIVIDUALS, 'nom','pl','Post laborem ____ quiescunt.','Po pracy {x} odpoczywają.')
add(INDIVIDUALS, 'nom','pl','____ ad oppidum contendunt.','{X} zmierzają do miasteczka.')
add(INDIVIDUALS, 'nom','pl','In foro ____ verba audiunt.','Na forum {x} słuchają słów.')
add(INDIVIDUALS, 'nom','pl','____ cum amicis ambulant.','{X} spacerują z przyjaciółmi.')
add(LEARNERS, 'nom','pl','Post scholam ____ ludunt.','Po szkole {x} się bawią.')
add(TRAVELERS, 'nom','pl','____ per vias festinant.','{X} spieszą przez ulice.')

# --- Accusativus singularis: zdania dobierane do rzeczy, osób, pojęć ---
add(INDIVIDUALS, 'acc','sg','Ad portam poeta ____ vocat.','Przy bramie poeta woła {x}.')
add(INDIVIDUALS, 'acc','sg','In foro magister ____ salutat.','Na forum nauczyciel pozdrawia {x}.')
add(INDIVIDUALS, 'acc','sg','Post cenam amicus ____ exspectat.','Po kolacji przyjaciel czeka na {x}.')
add(INDIVIDUALS, 'acc','sg','In via puella ____ convenit.','Na drodze dziewczyna spotyka {x}.')
add(INDIVIDUALS, 'acc','sg','Mater ____ ad cenam invitat.','Matka zaprasza {x} na kolację.')
add(INDIVIDUALS, 'acc','sg','Rex ____ in forum mittit.','Król wysyła {x} na forum.')
add(INDIVIDUALS, 'acc','sg','Servus ____ per silvam ducit.','Niewolnik prowadzi {x} przez las.')
add(SCENERY, 'acc','sg','De colle puer ____ spectat.','Ze wzgórza chłopiec ogląda {x}.')
add(VISIBLE, 'acc','sg','Sub luce solis agricola ____ videt.','W świetle słońca rolnik widzi {x}.')
add(VISIBLE, 'acc','sg','In itinere nauta ____ animadvertit.','W podróży żeglarz dostrzega {x}.')
add(VISIBLE, 'acc','sg','Puella prope flumen ____ invenit.','Dziewczyna znajduje {x} w pobliżu rzeki.')
add(CARRIABLE, 'acc','sg','Ad villam servus ____ portat.','Do willi niewolnik niesie {x}.')
add(CARRIABLE, 'acc','sg','Servus in mensa ____ ponit.','Niewolnik kładzie {x} na stole.')
add(CARRIABLE, 'acc','sg','Puer ____ in villa relinquit.','Chłopiec zostawia {x} w willi.')
add(CARRIABLE, 'acc','sg','In itinere mercator ____ servat.','Podczas podróży kupiec pilnuje {x}.')
add(WRITTEN, 'acc','sg','Ad lucernam magister ____ legit.','Przy lampie nauczyciel czyta {x}.')
add(WRITTEN, 'acc','sg','Puella ____ in mensa invenit.','Dziewczyna znajduje {x} na stole.')
add(THOUGHTS, 'acc','sg','Poeta ____ saepe memorat.','Poeta często wspomina {x}.')
add(THOUGHTS, 'acc','sg','Magister ____ discipulis explicat.','Nauczyciel wyjaśnia uczniom {x}.')
add(THOUGHTS, 'acc','sg','Senex ____ diu considerat.','Starzec długo rozważa {x}.')
add(VALUABLE, 'acc','sg','Mercator ____ diligenter custodit.','Kupiec starannie strzeże {x}.')
add(VALUABLE, 'acc','sg','Puer ____ sub mensa invenit.','Chłopiec znajduje {x} pod stołem.')

# --- Accusativus pluralis ---
add(INDIVIDUALS, 'acc','pl','In foro poeta ____ salutat.','Na forum poeta pozdrawia {x}.')
add(INDIVIDUALS, 'acc','pl','Magister ____ ad scholam vocat.','Nauczyciel woła {x} do szkoły.')
add(INDIVIDUALS, 'acc','pl','Ad portam servus ____ exspectat.','Przy bramie niewolnik czeka na {x}.')
add(INDIVIDUALS, 'acc','pl','Rex ____ in urbem mittit.','Król wysyła {x} do miasta.')
add(SCENERY, 'acc','pl','De colle nauta ____ spectat.','Ze wzgórza żeglarz ogląda {x}.')
add(VISIBLE, 'acc','pl','Puer in itinere ____ numerat.','Podczas podróży chłopiec liczy {x}.')
add(CARRIABLE, 'acc','pl','Puella ____ in villam portat.','Dziewczyna niesie {x} do willi.')
add(CARRIABLE, 'acc','pl','Servus ____ in mensa ponit.','Niewolnik kładzie {x} na stole.')
add(WRITTEN, 'acc','pl','Discipulus ____ diligenter legit.','Uczeń uważnie czyta {x}.')

# --- Genetivus singularis: relacja przynależności bez zgodności z celem ---
add(INDIVIDUALS, 'gen','sg','Nomen ____ in tabula scriptum est.','Imię {x} jest zapisane na tablicy.')
add(INDIVIDUALS, 'gen','sg','Vox ____ e villa auditur.','Głos {x} słychać z willi.')
add(INDIVIDUALS, 'gen','sg','Amicus ____ advenit.','Przyjaciel {x} przybywa.')
add(INDIVIDUALS, 'gen','sg','In horto vestigia ____ sunt.','W ogrodzie są ślady {x}.')
add(INDIVIDUALS, 'gen','sg','Fabula de vita ____ narratur.','Opowiada się historię życia {x}.')
add(NATURE, 'gen','sg','Pulchritudo ____ poetam delectat.','Piękno {x} zachwyca poetę.')
add(NATURE, 'gen','sg','Color ____ puellae placet.','Kolor {x} podoba się dziewczynie.')
add(STRUCTURES, 'gen','sg','Forma ____ in tabula depicta est.','Kształt {x} jest narysowany na tablicy.')
add(WRITTEN, 'gen','sg','Sensus ____ mihi clarus est.','Znaczenie {x} jest dla mnie jasne.')
add(WRITTEN, 'gen','sg','Finis ____ puero placet.','Koniec {x} podoba się chłopcu.')
add(SETTLEMENTS, 'gen','sg','Nomen ____ omnibus notum est.','Nazwa {x} jest wszystkim znana.')
add(THOUGHTS, 'gen','sg','Memoria ____ diu manet.','Pamięć o {x} długo trwa.')
add(THOUGHTS, 'gen','sg','Causa ____ nondum nota est.','Przyczyna {x} nie jest jeszcze znana.')
add(THOUGHTS, 'gen','sg','Vis ____ magna esse potest.','Siła {x} może być wielka.')
add(VALUABLE, 'gen','sg','Pretium ____ mercator quaerit.','Kupiec pyta o cenę {x}.')
add(VALUABLE, 'gen','sg','Dominus ____ in villa habitat.','Właściciel {x} mieszka w willi.')

# --- Ablativus singularis z de / in ---
add(INDIVIDUALS, 'abl','sg','Poeta de ____ carmen scribit.','Poeta pisze pieśń o {x}.')
add(INDIVIDUALS, 'abl','sg','In foro puella de ____ narrat.','Na forum dziewczyna opowiada o {x}.')
add(NATURE, 'abl','sg','Magister de ____ discipulos docet.','Nauczyciel uczy uczniów o {x}.')
add(THOUGHTS, 'abl','sg','In villa poeta de ____ cogitat.','W willi poeta rozmyśla o {x}.')
add(THOUGHTS, 'abl','sg','Senex de ____ multa narrat.','Starzec opowiada wiele o {x}.')
add(WRITTEN, 'abl','sg','Discipulus de ____ magistrum interrogat.','Uczeń pyta nauczyciela o {x}.')
add(SETTLEMENTS, 'abl','sg','Poeta de ____ carmen canit.','Poeta śpiewa pieśń o {x}.')
add(INTERIORS, 'abl','sg','Servus in ____ laborat.','Niewolnik pracuje w {x}.')
add(INTERIORS, 'abl','sg','In ____ puella amicum quaerit.','W {x} dziewczyna szuka przyjaciela.')
add(INTERIORS, 'abl','sg','Nauta in ____ diu manet.','Żeglarz długo zostaje w {x}.')
add(STRUCTURES, 'abl','sg','Puer de ____ cum patre disputat.','Chłopiec rozmawia z ojcem o {x}.')

# --- Jednostkowe sceny z dawnych ćwiczeń, włączone jako bank historyczny
# (w latin_legacy.py); powyższe konstrukcje są wielokrotnego użytku.

# Mini-leksykony dla słów, których nie można bez sensu mieszać z ogólnymi.
add('cena','nom','sg','____ iam parata est.','{X} jest już gotowa.')
add('cena','acc','sg','Ancilla ____ parat.','Służąca przygotowuje {x}.')
add('cena','gen','sg','Hora ____ appropinquat.','Zbliża się pora {x}.')
add('cena','abl','sg','Poeta de ____ loquitur.','Poeta mówi o {x}.')
add('cena','acc','pl','Regina ____ parat.','Królowa przygotowuje {x}.')
add('lingua','acc','sg','Magister ____ discit.','Nauczyciel poznaje {x}.')
add('lingua','gen','sg','Historia ____ longa est.','Historia {x} jest długa.')
add('lingua','nom','sg','____ difficilis est.','{X} jest trudny.')
add('lingua','abl','sg','Discipuli de ____ discunt.','Uczniowie uczą się o {x}.')
add('lingua','acc','pl','Discipulus ____ discit.','Uczeń poznaje {x}.')
add('oculus','acc','pl','Puer ____ claudit.','Chłopiec zamyka {x}.')
add('oculus','acc','sg','Medicus ____ inspicit.','Lekarz bada {x}.')
add('oculus','gen','sg','Color ____ pulcher est.','Kolor {x} jest piękny.')
add('oculus','nom','pl','____ lucent.','{X} błyszczą.')
add('numerus','acc','sg','Magister ____ in tabula scribit.','Nauczyciel zapisuje {x} na tablicy.')
add('numerus','gen','sg','Sensus ____ notus est.','Znaczenie {x} jest znane.')
add('numerus','nom','pl','____ in tabula apparent.','{X} pojawiają się na tablicy.')
add('numerus','acc','pl','Puer ____ discit.','Chłopiec poznaje {x}.')
add('annus','nom','sg','____ cito transit.','{X} szybko mija.')
add('annus','gen','sg','Finis ____ adest.','Zbliża się koniec {x}.')
add('annus','acc','sg','Poeta ____ memorat.','Poeta wspomina {x}.')
add('annus','nom','pl','____ cito transeunt.','{X} szybko mijają.')
add('annus','acc','pl','Senex ____ numerat.','Starzec liczy {x}.')
add('familia','nom','sg','____ in villa habitat.','{X} mieszka w willi.')
add('familia','gen','sg','Membra ____ adveniunt.','Członkowie {x} przybywają.')
add('familia','acc','sg','Puer ____ amat.','Chłopiec kocha {x}.')
add('familia','nom','pl','____ ad oppidum veniunt.','{X} przychodzą do miasteczka.')
add('populus','nom','sg','____ in foro convenit.','{X} gromadzi się na forum.')
add('populus','gen','sg','Vox ____ auditur.','Słychać głos {x}.')
add('populus','acc','sg','Regina ____ salutat.','Królowa pozdrawia {x}.')
add('locus','nom','sg','____ omnibus notus est.','{X} jest wszystkim znane.')
add('locus','acc','sg','Puer ____ monstrat.','Chłopiec wskazuje {x}.')
add('locus','gen','sg','Nomen ____ pulchrum est.','Nazwa {x} jest piękna.')
add('deus','gen','sg','Templum ____ magnum est.','Świątynia {x} jest wielka.')
add('deus','acc','sg','Poeta ____ laudat.','Poeta chwali {x}.')
add('ventus','nom','sg','____ per silvam flat.','{X} wieje przez las.')
add('ventus','gen','sg','Vis ____ magna est.','Siła {x} jest wielka.')
add('ventus','nom','pl','____ fortes flant.','{X} wieją silnie.')
add('caelum','nom','sg','____ serenum est.','{X} jest pogodne.')
add('caelum','gen','sg','Color ____ pulcher est.','Kolor {x} jest piękny.')
add('caelum','acc','sg','Poeta ____ spectat.','Poeta ogląda {x}.')
add('argentum','acc','sg','Mercator ____ servat.','Kupiec przechowuje {x}.')
add('argentum','gen','sg','Pretium ____ altum est.','Cena {x} jest wysoka.')
add('argentum','nom','sg','____ in mensa iacet.','{X} leży na stole.')

# Zdania awaryjne dla NOWYCH słów, nawet bez przypisania dodatkowych tagów.
# "kind" (person / thing / abstract) jest pobierany z centralnego leksykonu.
for category in ('person', 'thing', 'abstract'):
    add(words_with_tag(category), 'acc', 'sg',
        'Auctor ____ memorat.', 'Autor wspomina {x}.')
    add(words_with_tag(category), 'gen', 'sg',
        'De origine ____ disputant.', 'Dyskutują o pochodzeniu {x}.')
    add(words_with_tag(category), 'abl', 'sg',
        'Poeta de ____ scribit.', 'Poeta pisze o {x}.')

# --- Rozbudowa: celownik, dopełniacz i ablatyw w liczbie mnogiej, wołacz ---
# Grupy semantyczne pozostają pobierane wyłącznie z latin_data.py.
# Każde zdanie ma dopasowaną, jawnie zapisaną polską formę.
add(INDIVIDUALS, 'dat','sg','Poeta ____ librum dat.','Poeta daje {x} książkę.')
add(INDIVIDUALS, 'dat','sg','Magister ____ viam monstrat.','Nauczyciel pokazuje {x} drogę.')
add(INDIVIDUALS, 'dat','sg','Mater ____ epistulam mittit.','Matka wysyła {x} list.')
add(INDIVIDUALS, 'dat','sg','Servus ____ aquam portat.','Niewolnik niesie {x} wodę.')
add(INDIVIDUALS, 'dat','sg','Auctor ____ fabulam narrat.','Autor opowiada {x} historię.')
add(INDIVIDUALS, 'dat','pl','Poeta ____ carmen recitat.','Poeta recytuje {x} pieśń.')
add(INDIVIDUALS, 'dat','pl','Magister ____ exemplum dat.','Nauczyciel podaje {x} przykład.')
add(INDIVIDUALS, 'dat','pl','Nuntius ____ epistulam tradit.','Posłaniec przekazuje {x} list.')
add(INDIVIDUALS, 'dat','pl','Regina ____ dona mittit.','Królowa wysyła {x} dary.')
add(INDIVIDUALS, 'dat','pl','Puer ____ viam monstrat.','Chłopiec pokazuje {x} drogę.')
add(INDIVIDUALS, 'gen','pl','Voces ____ in foro audiuntur.','Na forum słychać głosy {x}.')
add(INDIVIDUALS, 'gen','pl','Nomina ____ in tabula scripta sunt.','Imiona {x} są zapisane na tablicy.')
add(INDIVIDUALS, 'gen','pl','Vestigia ____ in via apparent.','Na drodze widać ślady {x}.')
add(INDIVIDUALS, 'gen','pl','Amici ____ adveniunt.','Przybywają przyjaciele {x}.')
add(INDIVIDUALS, 'gen','pl','Vita ____ difficilis est.','Życie {x} jest trudne.')
add(INDIVIDUALS, 'abl','pl','Poeta cum ____ ambulat.','Poeta spaceruje z {x}.')
add(INDIVIDUALS, 'abl','pl','Magister cum ____ loquitur.','Nauczyciel rozmawia z {x}.')
add(INDIVIDUALS, 'abl','pl','Servus cum ____ ad villam venit.','Niewolnik przychodzi do willi z {x}.')
add(INDIVIDUALS, 'abl','pl','Puer cum ____ in horto sedet.','Chłopiec siedzi w ogrodzie z {x}.')
add(INDIVIDUALS, 'voc','sg','____, audi verba mea!','{X}, słuchaj moich słów!')
add(INDIVIDUALS, 'voc','sg','____, ad me veni!','{X}, przyjdź do mnie!')
add(INDIVIDUALS, 'voc','sg','____, hanc epistulam lege!','{X}, przeczytaj ten list!')
add(INDIVIDUALS, 'voc','sg','____, festina!','{X}, pospiesz się!')
add(INDIVIDUALS, 'voc','pl','____, audite verba mea!','{X}, słuchajcie moich słów!')
add(INDIVIDUALS, 'voc','pl','____, ad me venite!','{X}, przyjdźcie do mnie!')
add(INDIVIDUALS, 'voc','pl','____, festinate!','{X}, pospieszcie się!')
# Rzeczy i miejsca: liczba mnoga z Gen. i Abl. bez antropomorfizacji.
add(VISIBLE, 'gen','pl','Forma ____ puero placet.','Kształt {x} podoba się chłopcu.')
add(VISIBLE, 'gen','pl','Nomina ____ scripta sunt.','Nazwy {x} są zapisane.')
add(SCENERY, 'gen','pl','Pulchritudo ____ nota est.','Piękno {x} jest znane.')
add(VALUABLE, 'gen','pl','Pretium ____ magnum est.','Cena {x} jest wysoka.')
add(WRITTEN, 'gen','pl','Numerus ____ magnus est.','Liczba {x} jest duża.')
add(VISIBLE, 'abl','pl','Puella ____ gaudet.','Dziewczyna cieszy się {x}.')
add(NATURE, 'abl','pl','Poeta ____ delectatur.','Poeta zachwyca się {x}.')
add(WRITTEN, 'abl','pl','Magister ____ utitur.','Nauczyciel posługuje się {x}.')
add(THOUGHTS, 'abl','pl','Populus ____ gaudet.','Lud cieszy się {x}.')
add(PLACES, 'abl','pl','Mercator ____ delectatur.','Kupiec zachwyca się {x}.')
