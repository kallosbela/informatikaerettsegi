# 1.  Olvassa be és tárolja el a vonat.txt fájl tartalmát! 
print("1. feladat")
menetrend = []
with open("vonat.txt", "r") as f:
    for sor in f:
        menetrend.append(sor.strip().split("\t"))  #itt tabulátor van a részek között 

# 2.  Írja  a  képernyőre  a  fájlban  tárolt  vonatok  és  állomások  darabszámát  –  a  kezdő  és 
# végállomást is beleértve! 
# 2. feladat 
# Az állomások száma: 11 
# A vonatok száma: 12 
print("2. feladat")
vonatok = set([sor[0] for sor in menetrend])
allomasok = set([sor[1] for sor in menetrend])
print("Az állomások száma: ", len(allomasok))
print("A vonatok száma: ", len(vonatok))

# 3.  Határozza meg, hogy melyik állomáson állt legtöbbet vonat! Adja meg a vonat és az állomás 
# azonosítóját, valamint az állás idejét! Ha több ilyen volt, elég csak az egyiket megadnia. 
# 3. feladat 
# A(z) 5. vonat a(z) 6. állomáson 10 percet állt. 
print("3. feladat")
max_vonat = ""
max_allomas = ""
max_ido = 0
for vonat in range(1,len(vonatok)+1):      #vonatok számozása 1-től
    for allomas in range(len(allomasok)):  #allomások számozása 0-tól
        idok = [int(sor[2])*60+int(sor[3]) for sor in menetrend if sor[0] == str(vonat) and sor[1] == str(allomas)]
        if len(idok) == 2:
            ido = idok[1] - idok[0]
            if ido > max_ido:
                max_ido = ido
                max_vonat = vonat
                max_allomas = allomas 
print("A(z)", max_vonat, ". vonat a(z)", max_allomas, ". állomáson", max_ido, "percet állt.")

# 4.  Olvassa be egy vonat azonosítóját, valamint egy időpont óra és perc értékét! A későbbi 
# feladatokban használja ezeket! 
# 4. feladat 
# Adja meg egy vonat azonosítóját! 2 
# Adjon meg egy időpontot (óra perc)! 7 16 
print("4. feladat")
vonat = input("Adja meg egy vonat azonosítóját! ")
ora, perc = input("Adjon meg egy időpontot (óra perc)! ").split(" ")
idopont = int(ora)*60+int(perc) #éjfél óta eltelt percek száma

# 5.  Ezen a vonalon az előírt menetidő 2 óra 22 perc. Írja a képernyőre, hogy a beolvasott 
# azonosítójú vonat hány perccel tért el ettől! Például: „A(z) 5. vonat útja 2 perccel rövidebb 
# volt az előírtnál.”, „A(z) 5. vonat útja pontosan az előírt ideig tartott.” vagy „A(z) 5. vonat 
# útja 3 perccel hosszabb volt az előírtnál.” 
# 5. feladat 
# A(z) 2. vonat útja 2 perccel hosszabb volt az előírtnál.
print("5. feladat")
eloirva = 2*60 + 22
idok = [int(sor[2])*60+int(sor[3]) for sor in menetrend if sor[0] == vonat]
eltelt = idok[-1] - idok[0]
if eloirva > eltelt:
    print("A(z)", vonat, ". vonat útja", eloirva-eltelt, "perccel rövidebb volt az előírtnál.")
elif eloirva == eltelt:
    print("A(z)", vonat, ". vonat útja pontosan az előírt ideig tartott.")
else:
    print("A(z)", vonat, ". vonat útja", eltelt-eloirva, "perccel hosszabb volt az előírtnál.")

# 6.  Írja a haladX.txt fájlba, hogy a beolvasott azonosítójú vonat melyik állomásra mikor 
# érkezett! A fájlnévben az X helyére a beolvasott vonatazonosító kerüljön! 
erkezesek = [sor for sor in menetrend if sor[0] == vonat and sor[4] == "E"]
with open("halad" + vonat + ".txt", "w", encoding="utf8") as f:
    for sor in erkezesek:
        print(f"{sor[1]}. állomás: {sor[2]}:{sor[3]}" , file=f)

# 7.  Adja meg, hogy a beolvasott időpontban úton lévő, azaz a már elindult, de a végállomást 
# még el nem érő vonatok közül melyik hol tartott! A tesztelés során a következő időpontokra 
# érdemes figyelni: 6:50, 8:45, 9:05, 10:04, 10:20. 
# 7. feladat 
# A(z) 1. vonat a 6. állomáson állt. 
# A(z) 2. vonat a 2. és a 3. állomás között járt.
print("7. feladat")
for iVonat in range(1,len(vonatok)-1):
    idok = [[sor[1], int(sor[2])*60+int(sor[3]), sor[4]] for sor in menetrend if sor[0] == str(iVonat)]
    vegallomasra_ert = idok[-1][1]<= idopont and idok[-1][0] == str(len(allomasok))
    if not vegallomasra_ert:
        for i in range(len(idok)-1):
            if idok[i][1] <= idopont and idopont < idok[i+1][1]:
                if idok[i][2] == "E":
                    print(f"A(z) {iVonat}. vonat a(z) {idok[i][0]}. állomáson állt.")
                else:
                    print(f"A(z) {iVonat}. vonat a(z) {idok[i][0]}. és {idok[i+1][0]}. állomás között járt.")



