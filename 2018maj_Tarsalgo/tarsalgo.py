# 1. Olvassa be és tárolja el az ajto.txt fájl tartalmát! 
with open("ajto.txt", "r") as f:
    sorok = f.readlines()
adatok = [sor.split() for sor in sorok]

# 2.  Írja a képernyőre annak a személynek az azonosítóját, aki a vizsgált időszakon belül először 
# lépett be az ajtón, és azét, aki utoljára távozott a megfigyelési időszakban! 
# 2. feladat 
# Az első belépő: 2 
# Az utolsó kilépő: 6 
print('2. feladat')
print(f"Az első belépő: {adatok[0][2]}") 
print(f"Az utolsó kilépő: {adatok[-1][2]}")

# 3.  Határozza meg a fájlban szereplő személyek közül, ki hányszor haladt át a társalgó ajtaján! 
# A meghatározott értékeket azonosító szerint növekvő sorrendben írja az athaladas.txt 
# fájlba! Soronként egy személy azonosítója, és tőle egy szóközzel elválasztva az áthaladások 
# száma szerepeljen! 
print('3. feladat')
athaladasok_szama = {}
for sor in adatok:
    if sor[2] not in athaladasok_szama:
        athaladasok_szama[sor[2]] = 1
    else:
        athaladasok_szama[sor[2]] += 1
    # ez rövidebben: 
    # athaladasok_szama[sor[2]] = athaladasok_szama.get(sor[2], 0) + 1

#rendezzük kulcs szerint növekvő sorrendbe a szótár elemeit
athaladasok_szama = sorted(athaladasok_szama.items(), key=lambda x: int(x[0]))
#írjuk ki a fájlba
with open("athaladas.txt", "w") as f:
    for szemely, athaladasok in athaladasok_szama:
        print(szemely, athaladasok, file=f)

# 4.  Írja a képernyőre azon személyek azonosítóját, akik a vizsgált időszak végén a társalgóban 
# tartózkodtak! 
# 4. feladat 
# A végén a társalgóban voltak: 1 11 22 24 29 30 35 37 
print('4. feladat')
print("A végén a társalgóban voltak:", end=" ")
for szemely, athaladasok in athaladasok_szama:
    if athaladasok % 2 == 1:
        print(szemely, end=" ")
print()

# 5.  Hányan voltak legtöbben egyszerre a társalgóban? Írjon a képernyőre egy olyan időpontot 
# (óra:perc), amikor a legtöbben voltak bent! 
# 5. feladat 
# Például 10:44-kor voltak a legtöbben a társalgóban. 
print('5. feladat')
bentlevok = 0
idopontok = []
for sor in adatok:
    if sor[3] == "be":
        bentlevok += 1
    else:
        bentlevok -= 1
    idopontok.append((sor[0]+':'+sor[1], bentlevok))
max_bentlevo_idopont = max(idopontok, key=lambda x: x[1])[0]
print(f"Például {max_bentlevo_idopont}-kor voltak a legtöbben a társalgóban.")

# 6.  Kérje be a felhasználótól egy személy azonosítóját! A további feladatok megoldásánál ezt 
# használja fel! 
# Feltételezheti, hogy a megadott azonosítóhoz tartozik adat a forrásfájlban. 
# 6. feladat 
# Adja meg a személy azonosítóját! 22 
print('6. feladat')
szemely = input("Adja meg a személy azonosítóját! ")

# 7.  Írja  a  képernyőre,  hogy  a  beolvasott  azonosítóhoz  tartozó  személy  mettől  meddig 
# tartózkodott a társalgóban!  
# A kiírást az alábbi, 22-es személyhez tartozó példának megfelelően alakítsa ki!
# 11:22-11:27 
# 13:45-13:47 
# 13:53-13:58 
# 14:17-14:20 
# 14:57- 
print('7. feladat')
for sor in adatok:
    if sor[2] == szemely:
        if sor[3] == "be":
            print(f"{sor[0]}:{sor[1]}-", end="")
        else:
            print(f"{sor[0]}:{sor[1]}")

# 8.  Határozza meg, hogy a megfigyelt időszakban a beolvasott azonosítójú személy összesen 
# hány percet töltött a társalgóban! Az előző feladatban példaként szereplő 22-es személy 
# 5 alkalommal járt bent, a megfigyelés végén még bent volt. Róla azt tudjuk, hogy 18 percet 
# töltött bent a megfigyelés végéig. A 39-es személy 6 alkalommal járt bent, a vizsgált időszak 
# végén nem tartózkodott a helyiségben. Róla azt tudjuk, hogy 39 percet töltött ott. Írja ki, 
# hogy a beolvasott azonosítójú személy mennyi időt volt a társalgóban, és a megfigyelési 
# időszak végén bent volt-e még!
# 8. feladat 
# A(z) 22. személy összesen 18 percet volt bent, a megfigyelés 
# végén a társalgóban volt. 
print('8. feladat')
szemely_idopontok = [int(sor[0])*60+int(sor[1]) for sor in adatok if sor[2] == szemely]
szemely_bent = 0
for i in range(1, len(szemely_idopontok), 2):
    szemely_bent += szemely_idopontok[i] - szemely_idopontok[i-1]
if len(szemely_idopontok) % 2 == 1:
    szemely_bent += 15*60 - szemely_idopontok[-1]
    print(f"A(z) {szemely}. személy összesen {szemely_bent} percet volt bent, a megfigyelés végén a társalgóban volt.")
else:
    print(f"A(z) {szemely}. személy összesen {szemely_bent} percet volt bent, a megfigyelés végén nem volt a társalgóban.")