# 1.  Olvassa be és tárolja el az autok.txt fájl tartalmát! 
autok = []
with open("autok.txt", "r") as f:
    for sor in f:
        autok.append(sor.strip().split())
    
# 2.  Adja meg,  hogy melyik autót vitték el utoljára a parkolóból! Az eredményt a mintának 
# megfelelően írja a képernyőre! 
# 2. feladat 
# 30. nap rendszám: CEG300 
for i in range(len(autok)-1, -1, -1):
    if autok[i][5] == "0":
        print(f"{autok[i][0]}. nap rendszám: {autok[i][2]}")
        break
       
# 3.  Kérjen be egy napot és írja ki a képernyőre a minta szerint, hogy mely autókat vitték ki és hozták vissza az adott napon! 
# 3. feladat 
# Nap: 4 
# Forgalom a(z) 4. napon: 
# 12:50 CEG303 561 ki 
# 19:17 CEG308 552 be 
print("3. feladat")
nap = input("Nap: ")
print(f"Forgalom a(z) {nap}. napon:")
for sor in autok:
    if sor[0] == nap:
        if sor[5] == "0":
            print(f"{sor[1]} {sor[2]} {sor[3]} ki")
        else:
            print(f"{sor[1]} {sor[2]} {sor[3]} be")

# 4.  Adja meg, hogy hány autó nem volt bent a hónap végén a parkolóban! 
# 4. feladat 
# A hónap végén 4 autót nem hoztak vissza. 
print("4. feladat")
ki, be = 0, 0
for sor in autok:
    if sor[5] == "0":
        ki += 1
    else:
        be += 1
print(f"A hónap végén {ki-be} autót nem hoztak vissza.")

# 5.  Készítsen statisztikát, és írja ki a képernyőre mind a 10 autó esetén az ebben a hónapban 
# megtett  távolságot  kilométerben!  A  hónap  végén  még  kint  lévő  autók  esetén  az  utolsó rögzített kilométerállással számoljon! A kiírásban az autók sorrendje tetszőleges lehet. 
# 5. feladat 
# CEG300 6751 km 
# CEG301 5441 km 
# CEG302 5101 km 
# CEG303 7465 km 
# CEG304 6564 km 
# CEG305 5232 km 
# CEG306 7165 km 
# CEG307 6489 km 
# CEG308 6745 km 
# CEG309 1252 km 
print("5. feladat")
autorendszamok = sorted(set([sor[2] for sor in autok])) # a sorted már nem feltétlenül szükséges, de így szebb...
for rendszam in autorendszamok:
    km_allas = [int(sor[4]) for sor in autok if sor[2] == rendszam]
    print(f"{rendszam} {max(km_allas)-min(km_allas)} km")

# 6.  Határozza  meg,  melyik  személy  volt  az,  aki  az  autó  egy  elvitele  alatt  a  leghosszabb távolságot tette meg! A személy azonosítóját és a megtett kilométert a minta szerint írja a képernyőre! (Több legnagyobb érték esetén bármelyiket kiírhatja.) 
# 6. feladat 
# Leghosszabb út: 1551 km, személy: 506 
print("6. feladat")
max_km = 0
max_szemely = ""
for i in range(len(autok)):
    if autok[i][5] == "0": # kivitel történt, ezután megkeressük a visszahozatalt
        for j in range(i+1, len(autok)):
            if autok[i][2] == autok[j][2]: # visszahozatal történt
                km = int(autok[j][4]) - int(autok[i][4])
                if km > max_km:
                    max_km = km
                    max_szemely = autok[i][3]
                break
print(f"Leghosszabb út: {max_km} km, személy: {max_szemely}")

        
# 7.  Az  autók  esetén  egy  havi  menetlevelet  kell  készíteni!  Kérjen  be  a  felhasználótól  egy rendszámot!  Készítsen  egy  X_menetlevel.txt  állományt,  amelybe  elkészíti  az  adott 
# rendszámú  autó  menetlevelét! (Az  X  helyére  az  autó  rendszáma  kerüljön!)  A  fájlba 
# soronként  tabulátorral  elválasztva  a  személy  azonosítóját,  a  kivitel  időpontját  (nap. 
# óra:perc),  a  kilométerszámláló  állását,  a  visszahozatal  időpontját  (nap.  óra:perc),  és a kilométerszámláló állását írja a minta szerint! (A tabulátor karakter ASCII-kódja: 9.)
# 7. feladat 
# Rendszám: CEG304 
# Menetlevél kész 
print("7. feladat")
rendszam = input("Rendszám: ")
with open(f"{rendszam}_menetlevel.txt", "w") as f:
    for sor in autok:
        if sor[2] == rendszam:
            if sor[5] == "0":
                print(f"{sor[3]}\t{sor[0]}. {sor[1]}\t {sor[4]} km\t", end="", file=f)
            else:
                print(f"{sor[0]}. {sor[1]}\t {sor[4]} km", file=f)
                # \t helyett a következő is jó a tabulátor karakter ASCII-kódjával:
                # print(f"{sor[0]}. {sor[1]}{chr(9)} {sor[4]} km", file=f)
print("Menetlevél kész")