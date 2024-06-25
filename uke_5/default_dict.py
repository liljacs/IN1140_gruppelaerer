""" ----- DEFAULTDICT ----- """
# vi starter med å opprette en vanlig ordbok:

alder = {}
alder["Ole"] = 20
alder["Emilie"] = 5
print(alder["Ole"])  # Her får vi ut verdien av nøkkelen, "Ole"
# print(alder["Anders"]) # her får vi i en feilmelding, fordi "Anders" ikke finnes i ordboka vår

from collections import defaultdict  # vi importerer 'defaultdict'

# denne vil nå overkjøre den forrige 'alder'-ordboka
# det vi skriver bak 'lambda', vil være 'default-verdien' som en nøkkel får hvis den ikke eksisterer
# da får vi ikke lenger feilmeldinger!

alder = defaultdict(lambda: "vet ikke alder")
# vi tilordner verdier som i en vanlig ordbok:

alder["Ole"] = 20
alder["Emilie"] = 5
print(alder["Anders"])  # 'Anders' vil nå ha verdien 'vet ikke alder'
print(alder) # vi printer ut hele ordboka, og ser at 'Anders' automatisk ble lagt til med default-verdien
