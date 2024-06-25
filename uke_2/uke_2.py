
# først må vi åpne filen
fil = open("test.txt", encoding="utf-8") # vi bruker 'encoding' siden vi har æøå i norsk
filinnhold = fil.read() # gir lesetilgang
fil.close() # å lukke filen etter lesetilgang er god praksis

filinnhold = filinnhold.split() # når vi bruker split, deler vi på mellomrom, og innholdet blir lagt i en liste

# vi kan gå gjennom hvert ord med en for-løkke:
for ord in filinnhold:
    print(ord) # her printer vi hvert ord
    # vi kan også sjekke flere egenskaper ved ordene i en if-sjekk:
    if ord.endswith("r"):
        print(ord)


# vi kan lage en egen liste med ordene slik vi vil ha dem:
ordliste = []

for ord in filinnhold:
    ordliste.append(ord.upper())


print(ordliste) # nå er alle ordene i store bokstaver!
print(ordliste[0]) # printer første element med indeksering
print(ordliste[-1]) # printer siste element
print(ordliste[0:2]) # slicing: printer fra og med første ord, til tredje ord

