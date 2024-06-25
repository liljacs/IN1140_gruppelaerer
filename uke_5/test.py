# oblig 2a
import nltk
from nltk.corpus import gutenberg, brown
from collections import Counter, defaultdict
from nltk import bigrams, trigrams
import numpy as np
from numpy import random

bibeltekst = gutenberg.raw('bible-kjv.txt')
# 3.1 antall ord
print("antall_ord:", len(bibeltekst.split()))

#3.2 antall unike ord
lower_bibeltekst = []
for word in bibeltekst.split():
    lower_bibeltekst.append(word.lower())
print(len(set(lower_bibeltekst)))

#3.3
ord_teller = Counter(lower_bibeltekst)
print("20 mest frekvente:", ord_teller.most_common(20)) 

#3.4

#3.5 bigram og 3.6 trigram
setninger = gutenberg.sents('bible-kjv.txt')
print(list(bigrams(setninger[6])))
print(list(trigrams(setninger[7])))

#3.7 tren en bigrammodell
tellinger = defaultdict(lambda: defaultdict(lambda: 0))
modell = defaultdict(lambda: defaultdict(lambda: 0.0))

# legger til tellinger 
for setning in setninger:
    for ord1, ord2 in bigrams(setning, pad_right=True, pad_left=True):
        tellinger[ord1][ord2] += 1 # inneholder antall, over brøkstreken

print("opprettet tellinger")
# Lager selve modellen med sannsynligheter
for forrige_ord in tellinger:
    tellinger_total = sum(tellinger[forrige_ord].values()) # under brøkstreken
    for neste_ord in tellinger[forrige_ord]:
        modell[forrige_ord][neste_ord] = tellinger[forrige_ord][neste_ord]/tellinger_total

print("opprettet modell")

ferdig = False
tekst = [None] # starter teksten på én setningsstart

while not ferdig:
    nøkkel = tekst[-1] # henter ut det foregående ordet, w-1. Tilsvarer alltid forrige orf før neste legges til
    mulige_ord = list(modell[nøkkel].keys())
    sannsynligheter = list(modell[nøkkel].values())

    # trekker et ord med tilhørende sannsynlighet
    tekst.append(np.random.choice(mulige_ord, p=sannsynligheter))

    # Hvis teksten slutter på en setningsslutt, er vi ferdige
    if tekst[-1] is None and len(tekst) >= 50:
        ferdig = True

# print(tekst)

#3.8 Sannsynlighet for den genererte teksten
# lag bigrams av teksten. For hvert bigram: tell antall, og del på antall foregående ord

genererte_bigrams = bigrams(tekst)
generert_sannsynlighet = []

for bigram in genererte_bigrams:
    generert_sannsynlighet.append(modell[bigram[0]][bigram[1]])

sannsynlighet_setning = np.prod(generert_sannsynlighet)
print("sannysnligheten for den genererte setninger er", sannsynlighet_setning)

# 4. Ordklassetagging med regulære uttrykk

patterns = [
    (r'\b[wW]at\b|\b[wW]\b', 'WP'), # wh-pronouns
    (r'\bhere\b', 'RN'), # here
    (r',', ','), # komma
    (r'\.', '.'), # punktum
    (r'\b[mM]y\b|\b[yY]our\b|\b[hH]is\b', 'PRP\$'),  # possessive pronouns my, your, his, ...
    (r'\b([sS]|[hH])e\b|\b[iI]\b|\b[yY]ou\b', 'PRP'), # personal pronouns I, you , he, she, ...
    (r'\b[oO]f\b|\b[iI]n\b|\b[bB]y\b', 'IN'), # preposition or subordinating conjunction of, in, by ...
    (r'\b[cC]an\b|\b[cC]ould\b|\b[sS]ould\b|\b[wW]ill\b|\b[wW]ould\b', 'MD'), # modal
    (r'.*est\$', 'JJS'), # adj. superlative (f.eks. wildest)
    (r'.*ly\$', 'RB'), # adverb (f.eks. strongly, massivly)
    (r'and\$|or\$', 'CC'), # conjunction and|or
    (r'\b[tT]he\b|\b[aA]n?\b|\bthat\b', 'DT'), # determiner T(t)he, a, an
    (r'.*able$', 'JJ'), # adjective (f.eks. printable, manageable)

    # Fra NLTK-boka/oppgavesettet
    (r'.*ing$', 'VBG'),
    (r'.*ed$', 'VBD'),
    (r'.*es$', 'VBZ'),
    (r'.*ould$', 'MD'),
    (r'.*\'s$', 'NN$'),
    (r'.*s$', 'NNS'),
    (r'ˆ-?[0-9]+(\.[0-9]+)?$', 'CD'),

    # Default-tag til slutt som en siste utvei
    (r'.*', 'NN')
]

regexp_tagger = nltk.RegexpTagger(patterns)

brown_tagged = brown.tagged_sents(categories='adventure')
brown_untagged = brown.sents(categories='adventure')

fiction_tagged = brown.tagged_sents(categories='fiction')

tagged_sent = regexp_tagger.tag(brown_untagged[0])
print(tagged_sent)
print(regexp_tagger.accuracy(fiction_tagged))