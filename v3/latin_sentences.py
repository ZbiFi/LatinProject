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

# Słowa są grupowane według sensu, a nie wyłącznie deklinacji.
PEOPLE = 'puella femina familia amica filia nauta poeta servus dominus amicus puer filius magister ancilla domina regina discipula magistra agricola incola medicus discipulus faber socius vicinus nuntius'
INDIVIDUALS = 'puella femina amica filia nauta poeta servus dominus amicus puer filius magister ancilla domina regina discipula magistra agricola incola medicus discipulus faber socius vicinus nuntius'
LEARNERS = 'puella puer filia discipula discipulus amica amicus'
TRAVELERS = 'nauta agricola incola puer servus nuntius amicus socius'
WRITERS = 'poeta magister magistra discipula discipulus puella puer'
LEADERS = 'dominus domina regina magister magistra medicus'
NATURE = 'rosa aqua terra via silva insula stella luna ager equus hortus ventus rivus caelum'
SCENERY = 'silva via insula villa porta stella luna templum oppidum ager hortus rivus murus'
VISIBLE = 'rosa via silva insula villa porta stella luna templum oppidum ager hortus equus mensa sella fenestra murus gladius rivus signum'
CARRIABLE = 'rosa aqua liber donum verbum epistula gladius signum exemplum pecunia'
WRITTEN = 'liber epistula verbum historia exemplum consilium'
PLACES = 'terra via silva insula patria villa porta templum oppidum ager hortus provincia locus'
SETTLEMENTS = 'insula villa oppidum provincia patria'
INTERIORS = 'villa templum oppidum hortus silva provincia'
STRUCTURES = 'villa porta templum oppidum murus fenestra mensa sella'
THOUGHTS = 'vita cura patria animus bellum periculum fortuna victoria sapientia memoria historia auxilium consilium imperium'
VALUABLE = 'donum liber epistula pecunia argentum gladius'
EVERYDAY = 'rosa aqua mensa sella fenestra epistula liber donum verbum c ena signum'.replace('c ena','cena')
NOM_ACTIVE = 'puella femina filia nauta poeta servus dominus amicus puer filius magister ancilla domina regina discipula magistra agricola incola medicus discipulus faber socius vicinus nuntius'

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
