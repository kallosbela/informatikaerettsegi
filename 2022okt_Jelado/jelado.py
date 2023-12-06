# 1.  Olvassa  be  a  jel.txt  állomány  tartalmát,  tárolja  el  a  rögzített  jelek  adatait,  és  azok felhasználásával oldja meg a következő feladatokat! 
jelek = []
with open("jel.txt", "r") as f:
    for line in f:
        line = line.strip().split()
        jelek.append(line)

# 2.  Kérje be a felhasználótól egy jel sorszámát (a sorszámozás 1-től indul), és írja a képernyőre 
# az adott jeladáshoz tartozó x és y koordinátát!
print("2. feladat")
print("Adja meg a jel sorszámát!", end=" ")
jel = int(input()) #3
print(f"x={jelek[jel-1][3]} y={jelek[jel-1][4]}") # x=126 y=639

# 3.  Készítsen  függvényt  eltelt  néven,  amely  megadja,  hogy  a  paraméterként  átadott  két 
# időpont között hány másodperc telik el! A két időpontot, mint paramétert tetszőleges módon 
# átadhatja. Használhat három-három számértéket, két tömböt vagy listát, de más, a célnak 
# megfelelő  típusú  változót  is.  Ezt  a függvényt  később  használja  fel  legalább  egy  feladat 
# megoldása során! 
def eltelt(idopont1, idopont2):     #idopont1, idopont2: [óra, perc, másodperc]
    idopont_1 = int(idopont1[0])*3600 + int(idopont1[1])*60 + int(idopont1[2])
    idopont_2 = int(idopont2[0])*3600 + int(idopont2[1])*60 + int(idopont2[2])
    return idopont_2 - idopont_1

# 4.  Adja meg, mennyi idő telt el az első és az utolsó észlelés között! Az időt óra:perc:mperc 
# alakban írja a képernyőre! 
print("4. feladat")
ido = eltelt(jelek[0][0:3], jelek[-1][0:3])
ora = ido // 3600
if ora < 10:
    ora = "0" + str(ora)
perc = ido % 3600 // 60
if perc < 10:
    perc = "0" + str(perc)
mperc = ido % 60
if mperc < 10:
    mperc = "0" + str(mperc)
print(f"Időtartam: {ora}:{perc}:{mperc}") # 18:52:40

# 5.  Határozza  meg  azt  a  legkisebb,  a  koordináta-rendszer  tengelyeivel  párhuzamos  oldalú 
# téglalapot, amelyből nem lépett ki a  jeladó! Adja meg a téglalap  bal alsó és jobb felső 
# sarkának koordinátáit!
print("5. feladat")
x = [int(jel[3]) for jel in jelek]
y = [int(jel[4]) for jel in jelek]
print(f"Bal alsó: {min(x)} {min(y)}, jobb felső: {max(x)} {max(y)}") # Bal alsó: 4 639, jobb felső: 147 727 

# 6.  Írja a képernyőre, hogy mennyi volt a jeladó elmozdulásainak összege! Úgy tekintjük, hogy 
# a jeladó két pozíciója közötti elmozdulása a pozíciókat összekötő egyenes mentén történt. 
# Az  összeget  három  tizedes  pontossággal  jelenítse  meg!  A  kiírásnál  a  tizedesvessző  és 
# tizedespont  kiírása  is  elfogadott.  Az  i-edik  és  az  i+1-edik  pontok  távolságát  a 
# sqrt((x_i-x_i+1)^2+(y_i-y_i+1)^2) képlet segítségével határozhatja meg.
print("6. feladat")
elmozdulas = 0
for i in range(len(jelek)-1):
    elmozdulas += ((int(jelek[i][3])-int(jelek[i+1][3]))**2 + (int(jelek[i][4])-int(jelek[i+1][4]))**2)**0.5
print(f"Elmozdulás: {elmozdulas:.3f}") # Elmozdulás: 2007.677

# 7.  Írja a kimaradt.txt fájlba a kimaradt észlelésekkel kapcsolatos adatokat! A kimeneti 
# fájlban azok a bemeneti állományban rögzített vételi időpontok jelenjenek meg, amelyek 
# előtt  közvetlenül  egy  vagy  több  észlelés  kimaradt!  Az  időpont  mellett  –  a  mintának 
# megfelelően  –  jelenjen  meg,  hogy  legalább  hány  jel  maradt  ki,  és  az  is,  hogy  miből 
# következtet  a  hiányra!  Ha  idő-  és  koordináta-eltérésből  is  adódik  jelkimaradás,  akkor  a 
# nagyobb értéket írja ki! Ha az időeltérés és a koordináták eltérése alapján is ugyanannyi 
# jelkimaradásra következtetünk, akkor bármelyiket kiírhatja.
kimaradt = []
for i in range(len(jelek)-1):
    kimaradt_ido, kimaradt_x, kimaradt_y, kimaradt_tav = 0, 0, 0, 0
    if eltelt(jelek[i][0:3], jelek[i+1][0:3]) > 300:
        kimaradt_ido = (eltelt(jelek[i][0:3], jelek[i+1][0:3])-1)//300
    if abs(int(jelek[i][3])-int(jelek[i+1][3])) > 10:
        kimaradt_x = (abs(int(jelek[i][3])-int(jelek[i+1][3]))-1)//10
    if abs(int(jelek[i][4])-int(jelek[i+1][4])) > 10:
        kimaradt_y = (abs(int(jelek[i][4])-int(jelek[i+1][4]))-1)//10
    kimaradt_tav = max(kimaradt_x, kimaradt_y)
    if kimaradt_ido == 0 and kimaradt_tav == 0:
        continue
    if kimaradt_tav > kimaradt_ido:
        kimaradt.append(f"{jelek[i+1][0]} {jelek[i+1][1]} {jelek[i+1][2]} koordináta-eltérés {kimaradt_tav}")
    else:
        kimaradt.append(f"{jelek[i+1][0]} {jelek[i+1][1]} {jelek[i+1][2]} időeltérés {kimaradt_ido}")
with open("kimaradt.txt", "w", encoding="utf8") as f:
    for sor in kimaradt:
        print(sor, file=f)     



 
