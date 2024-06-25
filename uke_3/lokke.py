# FOR-LØKKER

"""En for-løkke er noe vi kan bruke for å nå elementer på et dypere nivå- for eksempel alle elemntene 
i en liste, eller hver bokstav i en streng. Har vi brukt .split() i en tekst, vil ordene være skilt fra hverandre.
Hvis vi vil nå hvert ord, kan vi gjøre det i en for-løkke. Da kan vi for eksempel vise hvert ord, eller endre hvert ord,
for eksempel gjøre de til store eller små bokstaver, fjerne bokstaver, legge til bokstaver, og masse annet! """

# Vi begynner med å opprette en liste:
handleliste = ["brød", "smør", "melk"]
print(handleliste)
# nå ser vi hele handlelista, men kan ikke egentlig gjøre noe elementvis med den

# nå vil vi gjerne nå hvert element på lista, og gjøre de til store bokstaver:
for element in handleliste:
    element = element.upper()
    print(element)


"""'element' er en slags variabel vi bruker for å referere til hvert element i lista vår.
Variabelnavnet kan også hete hva som helst annet, så lenge det ikke er et reservert ord i python, som f.eks.
'in'. Variabelen fungerer som en peker, som endrer seg til neste element i lista vår, for hver iterasjon den tar.
Når det ikke er flere elementer igjen, slutter løkka."""


"""Når vi bruker en for-løkke må det vi går gjennom være 'itererbart'. Det vil si at vi må kunne gå gjennom
elementene en og en. En variabel som inneholder bare ett tall vil for eksempel ikke være itererbart."""

# Vi kan iterere gjennom en streng:
tekst = "Velkommen til gruppetime!"

for bokstav in tekst:
    print(bokstav)

# hvis vi splitter teksten, vil vi få hvert ord i teksten:
tekst = tekst.split()

for ord in tekst:
    print(ord)
    #vi kan lage en 'nøstet' løkke hvis vi vil nå enda lengre inn:
    for bokstav in ord:
        print(bokstav)








