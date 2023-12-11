# 1.  Olvassa be és tárolja el a lista.txt fájl tartalmát! 
filmek = []
with open("lista.txt", "r", encoding="utf8") as f:
  while True:
    film = {}
    film['datum'] = f.readline().strip()
    if film['datum'] == "":
      break #elértem a fájl végét
    film['cim'] = f.readline().strip()
    film['epizod'] = f.readline().strip()
    film['ido'] = int(f.readline().strip())
    film['megnezett'] = int(f.readline().strip())     # 0 nem látta, 1 látta
    filmek.append(film)

# 2.  Írassa ki a képernyőre, hogy hány olyan epizód adatait tartalmazza a fájl, amelynek ismert 
# az adásba kerülési dátuma! 
db = 0
for film in filmek:
  if film['datum'] != "NI":
    db += 1
print('2. feladat') 
print(f"A listában {db} db vetítési dátummal rendelkező epizód van.")

# 3.  Határozza meg, hogy a fájlban lévő epizódok hány százalékát látta már a listát rögzítő 
# személy! A százalékértéket a minta szerint, két tizedesjeggyel jelenítse meg a képernyőn! 
latta = 0
for film in filmek:
  if film['megnezett'] == 1:
    latta += 1
print("3. feladat")
print(f"A listában lévő epizódok {round(latta/len(filmek)*100,2)}%-át látta.")

# 4.  Számítsa ki, hogy összesen mennyi időt töltött a személy az epizódok megnézésével! 
# Az eredményt a minta szerint nap, óra, perc formában adja meg! 
total = 0
for film in filmek:
  if film['megnezett'] == 1:
    total += film['ido']
nap = total // (24*60)
ora = (total % (24*60)) // 60
perc = total %  60
print("4. feladat")
print(f"Sorozatnézéssel {nap} napot {ora} órát és {perc} percet töltött.")

# 5.  Kérjen be a felhasználótól egy dátumot „éééé.hh.nn” formában! Határozza meg, hogy 
# az adott dátumig megjelent epizódokból melyeket nem látta még! Az aznapi epizódokat is 
# számolja  bele!  A  feltételnek  megfelelő  epizódok  esetén  írja  a  képernyőre  tabulátorral 
# elválasztva az évad- és az epizódszámot, valamint a sorozat címét a minta szerint!
print("5. feladat")
datum = input("Adjon meg egy dátumot! Dátum= ")
for film in filmek:
  if film['datum'] <= datum and film['megnezett'] == 0:
    print(f"{film['epizod']}\t{film['cim']}")

# 6. Készítse el az alábbi algoritmus alapján a hét napját meghatározó függvényt! A függvény
# neve Hetnapja legyen! A függvény az év, hónap és nap megadása után szöveges
# eredményként visszaadja, hogy az adott nap a hét melyik napja volt. (Az a és b egész
# számok maradékos osztása esetén az a div b kifejezés adja meg a hányadost,
# az a mod b pedig a maradékot, például 17 div 7 = 2 és 17 mod 7 = 3.)
# Függvény hetnapja(ev, ho, nap : Egész) : Szöveg
#  napok: Tömb(0..6: Szöveg)= (″v″, ″h″, ″k″, ″sze″,
# ″cs″, ″p″, ″szo″)
#  honapok: Tömb(0..11: Egész)= (0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4)
#  Ha ho < 3 akkor ev := ev -1
#  hetnapja := napok[(ev + ev div 4 – ev div 100 +
#  ev div 400 + honapok[ho-1] + nap) mod 7]
# Függvény vége
def hetnapja(ev, ho, nap):
  napok = ["v", "h", "k", "sze", "cs", "p", "szo"]
  honapok = [0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4]
  if ho < 3:
    ev -= 1
  return napok[(ev + ev // 4 - ev // 100 + ev // 400 + honapok[ho-1] + nap) % 7]

# 7. Kérjen be a felhasználótól egy napot az előző feladatban látható rövidített alakban!
# A napokat egy (h, k, p, v), kettő (cs), vagy három (sze, szo) karakterrel adja meg! Határozza
# meg, hogy a fájlban lévő sorozatok közül melyike(ke)t vetítik az adott napon! A sorozatok
# nevét a minta szerint jelenítse meg a képernyőn! Ha az adott napon egy sorozatot sem adtak
# adásba, akkor „Az adott napon nem kerül adásba sorozat.” üzenetet jelenítse meg!
print("7. feladat")
nap = input("Adja meg a hét egy napját (például cs)! Nap= ")
van = False
vetitettek = []
for film in filmek:
  if film['datum'] != "NI" and hetnapja(int(film['datum'][0:4]), int(film['datum'][5:7]), int(film['datum'][8:10]))==nap and (film['cim'] not in vetitettek):
    van = True
    vetitettek.append(film['cim'])
if van:
  for cim in vetitettek:
    print(cim)
else:
  print("Az adott napon nem kerül adásba sorozat.")

# 8. Határozza meg sorozatonként az epizódok összesített vetítési idejét és az epizódok számát!
# A számításnál vegye figyelembe a vetítési dátummal nem rendelkező epizódokat is!
# A megoldás során felhasználhatja, hogy egy sorozat epizódjainak adatai egymást követik
# a forrásállományban. A listát írja ki a summa.txt fájlba! A fájl egy sorában a sorozat címe,
# az adott sorozatra vonatkozó összesített vetítési idő percben és az epizódok száma
# szerepeljen szóközzel elválasztva! 
osszesites = {}
for film in filmek:
  if film['cim'] in osszesites:
    osszesites[film['cim']]['ido'] += film['ido']
    osszesites[film['cim']]['db'] += 1
  else:
    osszesites[film['cim']] = {'ido':film['ido'], 'db':1}
with open("summa.txt", "w", encoding="utf8") as f:
  for cim in osszesites:
    print(f"{cim} {osszesites[cim]['ido']} {osszesites[cim]['db']}", file=f )
