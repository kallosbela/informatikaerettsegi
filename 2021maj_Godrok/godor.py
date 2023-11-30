# 1.  Olvassa be és tárolja el a melyseg.txt fájl tartalmát! Írja ki a képernyőre, hogy az 
# adatforrás hány adatot tartalmaz! 
print("1. feladat")
melyseg = []
with open("melyseg.txt", "r") as f:
    for mely in f.readlines():
        melyseg.append(int(mely))
    print("Adatok száma: ", len(melyseg))

# 2.  Olvasson be egy távolságértéket, majd írja a képernyőre, hogy milyen mélyen van a gödör 
# alja azon a helyen! Ezt a távolságértéket használja majd a 6. feladat megoldása során is! 
print("2. feladat")
tav = int(input("Adjon meg egy távolságot! "))
print("A felszín", melyseg[tav-1], "méter mélyen van a", tav, ". méteren.")

# 3.  Határozza meg, hogy a felszín hány százaléka maradt érintetlen és jelenítse meg 2 tizedes 
# pontossággal! 
print("3. feladat")
erintetlen = [mely for mely in melyseg if mely == 0]
print("A felszín", round(len(erintetlen)/len(melyseg)*100, 2), "%-a maradt érintetlen.")

# 4.  Írja ki a godrok.txt fájlba a gödrök leírását, azaz azokat a számsorokat, amelyek egy-egy 
# gödör méterenkénti mélységét adják meg! Minden gödör leírása külön sorba kerüljön! Az 
# állomány pontosan a gödrök számával egyező számú sort tartalmazzon! 
print("4. feladat")
godrok = []
with open("godrok.txt", "w") as f:
    for mely in melyseg:
        if mely != 0:
            godrok.append(mely)
        else:
            if len(godrok) > 0:
                f.write(" ".join([str(m) for m in godrok]) + "\n")
                godrok = []
    #utolsot is ki kell irni            
    if len(godrok) > 0:
        f.write(" ".join([str(m) for m in godrok]) + "\n")

# 5.  Határozza meg a gödrök számát és írja a képernyőre! 
print("5. feladat")
godrok = []
with open("godrok.txt", "r") as f:
    for sor in f.readlines():
        godrok.append(sor.strip().split())
print("A gödrök száma: ", len(godrok))

# 6.  Ha a 2. feladatban beolvasott helyen nincs gödör, akkor „Az adott helyen nincs gödör.” 
# üzenetet jelenítse meg, ha ott gödör található, akkor határozza meg, hogy 
# a)  mi a gödör kezdő és végpontja! A meghatározott értékeket írja a képernyőre! 
# (Ha nem tudja meghatározni, használja a további részfeladatoknál a 7 és 22 
# értéket, mint a kezdő és a végpont helyét) 
print("6. feladat")
if melyseg[tav-1] == 0:
    print("Az adott helyen nincs gödör.")
else:
    kezd = tav
    while melyseg[kezd-1] != 0:
        kezd -= 1
    veg = tav
    while melyseg[veg-1] != 0:
        veg += 1
    print("A gödör kezdete:", kezd+1, ", vége:", veg-1)
# b)  a legmélyebb pontja felé mindkét irányból folyamatosan mélyül-e! Azaz a gödör 
# az egyik szélétől monoton mélyül egy pontig, és onnantól monoton emelkedik a 
# másik széléig. Az eredménytől függően írja ki a képernyőre a „Nem mélyül 
# folyamatosan.” vagy a „Folyamatosan mélyül.” mondatot! 
 

# c)  mekkora a legnagyobb mélysége! A meghatározott értéket írja a képernyőre! 
# d)  mekkora a térfogata, ha szélessége minden helyen 10 méternyi! A meghatározott 
# értéket írja a képernyőre! 
# e)  a félkész csatorna esőben jelentős mennyiségű vizet fogad be. Egy gödör annyi 
# vizet képes befogadni anélkül, hogy egy nagyobb szélvihar hatására se öntsön 
# ki, amennyi esetén a víz felszíne legalább 1 méter mélyen van a külső felszínhez 
# képest. Írja a képernyőre ezt a vízmennyiséget!