# a. Les inn fil
fil = open('in01.txt')
filinnhold = fil.readlines()

for linje in filinnhold:
    for ord in linje.split():
        print(ord)

# b. Tell forekomster

antall_er = 0
for ord in filinnhold:
    if 'er' in ord:
        antall_er += 1

print("antall er:", antall_er) 

# endelser
er_endelser = 0
for ord in filinnhold:
    if ord.endswith('er'):
        er_endelser += 1

print('antall er-endelser:', er_endelser)


