# 1. Olvassa  be  és  tárolja  el  a  beosztas.txt  állományban  talált  adatokat,  és  annak 
# felhasználásával oldja meg a következő feladatokat! 

adatok = []
with open('beosztas.txt', 'r') as f:
    for sor in f:
        adatok.append(sor.strip())
tantargyfelosztas = []
for i in range(0, len(adatok), 4):
    tantargyfelosztas.append(adatok[i:i+4]) 

# 2. Hány bejegyzés található az állományban? Az eredményt írassa ki a képernyőre! 
# 2. feladat 
# A fájlban 329 bejegyzés van.
print('2. feladat')
print(f'A fájlban {len(tantargyfelosztas)} bejegyzés van.') 

# 3. A fenntartó számára fontos információ, hogy az iskolában hetente összesen hány tanítási 
# óra van. Határozza meg ezt az adatot és írassa ki a képernyőre! 
# 3. feladat 
# Az iskolában a heti összóraszám: 1016 
print('3. feladat')
orak = sum([int(tantargy[3]) for tantargy in tantargyfelosztas])
print(f'Az iskolában a heti összóraszám: {orak}')

# 4. Kérje be a felhasználótól egy tanár nevét, és írassa ki a képernyőre, hogy hetente hány 
# órában tanít!
# 4. feladat 
# Egy tanár neve= Albatrosz Aladin 
# A tanár heti óraszáma: 24 
print('4. feladat')
tanar = input('Egy tanár neve= ')
tanarorak = sum([int(tantargy[3]) for tantargy in tantargyfelosztas if tantargy[0] == tanar])
print(f'A tanár heti óraszáma: {tanarorak}')

# 5. Készítse el az of.txt fájlt, amely az osztályfőnökök nevét tartalmazza osztályonként 
# az alábbi formában (az osztályok megjelenítésének sorrendje a mintától eltérhet): 
# 9.a - Albatrosz Aladin 
# 9.b - Hangya Hanna 
# 9.c - Zerge Zenina 
# ... 
with open('of.txt', 'w') as f:
    for osztaly in sorted(list(set([tantargy[2] for tantargy in tantargyfelosztas]))):
        if osztaly[-1] == 'x':
            continue
        of = [elem[0] for elem in tantargyfelosztas if (elem[2] == osztaly and elem[1] == 'osztalyfonoki')][0]
        print(f'{osztaly} - {of}', file=f)

# 6. Egyes osztályokban bizonyos tantárgyakat a tanulók csoportbontásban tanulnak: ekkor az 
# adott tantárgyra és osztályra két bejegyzést is tartalmaz a tantárgyfelosztás. Kérje be egy 
# osztály azonosítóját, valamint egy tantárgy nevét, és írassa ki a képernyőre, hogy az adott 
# osztály  a  megadott  tantárgyat  csoportbontásban  vagy  osztályszinten  tanulja-e! 
# (Feltételezheti, hogy a megadott osztály tanulja a megadott tantárgyat.) 
# 6. feladat 
# Osztály= 10.b 
# Tantárgy= kemia 
# Csoportbontásban tanulják. 
print('6. feladat')
osztaly = input('Osztály= ')
tantargy = input('Tantárgy= ')
if len([elem for elem in tantargyfelosztas if (elem[2] == osztaly and elem[1] == tantargy)]) == 2:
    print('Csoportbontásban tanulják.')
else: 
    print('Osztályszinten tanulják.')

# 7. A fenntartó számára az is fontos információ, hogy hány tanár dolgozik az iskolában. Írassa 
# ki ezt az adatot a képernyőre!
# 7. feladat 
# Az iskolában 49 tanár tanít.
print('7. feladat')
tanarok = len(list(set([tantargy[0] for tantargy in tantargyfelosztas])))
print(f'Az iskolában {tanarok} tanár tanít.')