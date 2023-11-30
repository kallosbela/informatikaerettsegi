# 1. Olvassa be egy fájl nevét, egy sor és egy oszlop sorszámát (1 és 9 közötti számot)! A későbbi feladatokat ezen értékek felhasználásával kell megoldania!
print("1. feladat") 
fajlnev = "konnyu.txt" #input("Fájl neve: ")
sor = 2 #int(input("Sor sorszáma: "))
oszlop = 3 #int(input("Oszlop sorszáma: "))
# 2. Az előző feladatban beolvasott névnek megfelelő fájl tartalmát olvassa be, és tárolja el a táblázat adatait! Ha ezt nem tudja megtenni, akkor használja forrásként a rendelkezésre álló állományok egyikét!
print("2. feladat")
with open(fajlnev, "r") as f:
    tabla = []
    lepesek = []
    for teljessor in f:
        sor1 = teljessor.strip().split()
        if len(sor1) == 9:
          tabla.append(sor1)
        elif len(sor1) == 3:
          lepesek.append(sor1)
# 3. Írja ki a képernyőre, hogy a beolvasott sor és oszlop értékének megfelelő hely…
# a. milyen értéket tartalmaz! Ha az adott helyen a 0 olvasható, akkor az „Az adott
# helyet még nem töltötték ki.” szöveget jelenítse meg!
# b. melyik résztáblázathoz tartozik! A résztáblázatokat a következőképpen jelölje:
# 1 2 3
# 4 5 6
# 7 8 9
print("3. feladat")
if tabla[sor-1][oszlop-1] == "0":
  print("Az adott helyet még nem töltötték ki.")
else:
  print("Az adott helyen szereplő szám: ",tabla[sor-1][oszlop-1])
if sor<=3:
  if oszlop<=3:
    print("A hely a(z) 1 résztáblázathoz tartozik.")
  elif oszlop<=6:
    print("A hely a(z) 2 résztáblázathoz tartozik.")
  else:
    print("A hely a(z) 3 résztáblázathoz tartozik.")
elif sor<=6:
  if oszlop<=3:
    print("A hely a(z) 4 résztáblázathoz tartozik.")
  elif oszlop<=6:
    print("A hely a(z) 5 résztáblázathoz tartozik.")
  else:
    print("A hely a(z) 6 résztáblázathoz tartozik.")
else:
  if oszlop<=3:
    print("A hely a(z) 7 résztáblázathoz tartozik.")
  elif oszlop<=6:
    print("A hely a(z) 8 résztáblázathoz tartozik.")
  else:
    print("A hely a(z) 9 résztáblázathoz tartozik.")

# 4. Határozza meg a táblázat hány százaléka nincs még kitöltve! Az eredményt egy tizedesjegy pontossággal jelenítse meg a képernyőn!
print("4. feladat")
ures = 0
for sor in tabla:
  for elem in sor:
    if elem == "0":
      ures += 1
print("A táblázat ",round(ures/81*100,1),"% -a nincs még kitöltve.")

# 5. Vizsgálja meg, hogy a fájlban szereplő lépések lehetségesek-e a beolvasott táblázaton! Tekintse mindegyiket úgy, mintha az lenne az egyetlen lépés az eredeti táblázaton, de ne hajtsa azt végre! Állapítsa meg, hogy okoz-e valamilyen ellentmondást a lépés végrehajtása! Írja ki a lépéshez tartozó három értéket, majd a következő sorba írja az alábbi megállapítások egyikét! Ha több megállapítás is igaz, elegendő csak egyet megjelenítenie. 
# • „A helyet már kitöltötték”
# • „Az adott sorban már szerepel a szám”
# • „Az adott oszlopban már szerepel a szám”
# • „Az adott résztáblázatban már szerepel a szám”
# • „A lépés megtehető”
print("5. feladat")
for lepes in lepesek:
  sor = int(lepes[1])
  oszlop = int(lepes[2])
  szam = lepes[0]
  resztabla = []
  for teljessor in tabla[(sor-1)//3*3:(sor-1)//3*3+3]:
    for elem in teljessor[(oszlop-1)//3*3:(oszlop-1)//3*3+3]:
      resztabla.append(elem)
  print(f"A kiválasztott sor: {sor}, oszlop: {oszlop}, a szám: {szam}")
  if tabla[sor-1][oszlop-1] != "0":
    print("A helyet már kitöltötték")
  elif szam in tabla[sor-1]:
    print("Az adott sorban már szerepel a szám")
  elif szam in [sor[oszlop-1] for sor in tabla]:
    print("Az adott oszlopban már szerepel a szám")
  elif szam in resztabla:
    print("Az adott résztáblázatban már szerepel a szám")
  else:
    print("A lépés megtehető")