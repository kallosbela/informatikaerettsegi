# 1.  Olvassa  be  és  tárolja  el  az  utca.txt  állományban  talált  adatokat,  és  annak 
# felhasználásával oldja meg a következő feladatokat! 
adosavok = []
telek_adatok = []
A, B, C = 0, 0, 0
with open('utca.txt', 'r', encoding='utf8') as file:
  sorok = file.readlines()
  A, B, C = list(map(int, sorok[0].split()))
  telek_adatok = [sor.strip().split() for sor in sorok[1:]]

# 2.  Hány  telek  adatai  találhatók  az  állományban?  Az  eredményt  írassa  ki  a  mintának  
# megfelelően a képernyőre! 
print(f"2. feladat. A mintában {len(telek_adatok)} telek szerepel.")

# 3.  Kérje be egy tulajdonos adószámát, és írassa ki a mintához hasonlóan, hogy melyik utcában, 
# milyen  házszám  alatt  van  építménye!  Ha  a  megadott  azonosító  nem  szerepel  az 
# adatállományban, akkor írassa ki a „Nem szerepel az adatállományban.” hibaüzenetet! 
print("3. feladat. Egy tulajdonos adószáma: ")
adoszam = input()
talalatok = [telek for telek in telek_adatok if telek[0] == adoszam]

if talalatok:
    for talalat in talalatok:
        print(f"{talalat[1]} utca {talalat[2]}")
else:
    print("Nem szerepel az adatállományban.")

# 4.  Készítsen függvényt ado néven, amely meghatározza egy adott építmény után fizetendő 
# adót! A függvény paraméterlistájában szerepeljen az adósáv és az alapterület, visszaadott 
# értéke  pedig  legyen  a  fizetendő  adó!  A  következő  feladatokban  ezt  a  függvényt  is 
# felhasználhatja. 
def ado(adosav, alapterulet):
    adosav_dict = {'A': A, 'B': B, 'C': C}
    ado = adosav_dict[adosav] * int(alapterulet)
    return ado if ado >= 10000 else 0

# 5.  Határozza meg, hogy hány építmény esik az egyes adósávokba, és mennyi az adó összege 
# adósávonként! Az eredményt a mintának megfelelően írassa ki a képernyőre! 
Aado, Bado, Cado = 0, 0, 0
Atelek, Btelek, Ctelek = 0, 0, 0
for (_, _, _, sav, terulet) in telek_adatok:
  if sav == 'A': 
    Aado += ado(sav, terulet)
    Atelek += 1
  elif sav == 'B': 
    Bado += ado(sav, terulet)
    Btelek += 1
  elif sav == 'C': 
    Cado += ado(sav, terulet)
    Ctelek += 1
print(f"5. feladat \nA sávba {Atelek} telek esik, az adó {Aado} Ft.\nB sávba {Btelek} telek esik, az adó {Bado} Ft.\nC sávba {Ctelek} telek esik, az adó {Cado} Ft.")  

# 6.  Bár az utcák többé-kevésbé párhuzamosak a tó partjával, az egyes porták távolsága a parttól 
# az utcában nem feltétlenül ugyanannyi. Emiatt néhány utcában – az ottani tulajdonosok 
# felháborodására – egyes telkek eltérő sávba esnek. Listázza ki a képernyőre, hogy melyek 
# azok az utcák, ahol a telkek sávokba sorolását emiatt felül kell vizsgálni! Feltételezheti, 
# hogy minden utcában van legalább két telek. 
utcak = {}
for (_, utca, _, sav, _) in telek_adatok:
  if utca not in utcak:
    utcak[utca] = [sav]
  elif sav not in utcak[utca]:
    utcak[utca].append(sav)
print('6. feladat. A több sávba sorolt utcák:') 
for utca in utcak:
   if len(utcak[utca])>1: print(utca)  

# 7.  Határozza meg a fizetendő adót tulajdonosonként! A tulajdonos adószámát és a fizetendő 
# összeget írassa ki a mintának megfelelően a fizetendo.txt állományba! A fájlban 
# minden tulajdonos adatai új sorban szerepeljenek, a tulajdonos adószámát egy szóközzel 
# elválasztva kövesse az általa fizetendő adó teljes összege. 
tulajdonos_adok = {}

for (adoszam, _, _, sav, terulet) in telek_adatok:
    if adoszam in tulajdonos_adok:
        tulajdonos_adok[adoszam] += ado(sav,terulet)
    else:
        tulajdonos_adok[adoszam] = ado(sav,terulet)

with open('fizetendo.txt', 'w', encoding='utf8') as file:
        for adoszam in tulajdonos_adok:
            file.write(f"{adoszam} {tulajdonos_adok[adoszam]}\n")