import re

tekst = "Kari Nordmann studerer på IFI, Institutt for Informatikk, og er der hver uke fra mandag til fredag. Byggets adresse er Gastaudalléen 23B."

# vi kan ekstrahere egennavn fra teksten slik:
egennavn = r"[A-Z][a-z]+\s[A-Z][a-z]+"
egennavn_tokens = re.findall(egennavn, tekst)
print(egennavn_tokens)

# så, vil vi ekstrahere ukedagene i teksten:
ukedager = r"(man|fre)(dag)"

"""siden vi bruker flere grupper, får vi litt rare resultater, der hver match er fordelt i 'tupler'. 
For å unngå dette, endrer vi uttrykket til å bli en 'non-capturing group' med '?:' i hver gruppe. 
Prøv å bruk begge versjoner for å se forskjellen! NB: dette er ikke pensum, men kan gjøre det litt lettere for en selv."""

ukedager = r"(?:man|fre)(?:dag)"

ukedager_tokens = re.findall(ukedager, tekst)

""" Hvis vi printer ukedager_tokens her, vil matchene være slått sammen, slik vi vil ha dem. En metode som vil gjøre det samme, 
er .join(), som vi allerede har lært. Da trenger vi ikke å bruke non-capturing groups, men vi får noen flere kodelinjer:"""

for i in ukedager_tokens:
    print("".join(i))

# Til slutt, vil vi ekstrahere adressen i teksten:
adresse = r"[A-Z][a-zé]+\s[0-9]{2}[A-Z]"
adresse_tokens = re.findall(adresse, tekst)
print(adresse_tokens)

# TIPS: Hvis du vil teste om et uttrykk fungerer uten å bruke python- bruk 'regex101.com'! Husk å velge 'python' på venstresiden.
