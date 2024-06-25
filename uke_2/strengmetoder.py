fil = open("test.txt", encoding="utf-8")
filinnhold = fil.read()
fil.close()

filinnhold = filinnhold.split()
# print(filinnhold.count("å"))

ordliste = []

for ord in filinnhold:
    if ord.endswith("r"):
        ordliste.append(ord)

#print(ordliste)
#print(len(set(ordliste)))
print(ordliste[0].upper())
