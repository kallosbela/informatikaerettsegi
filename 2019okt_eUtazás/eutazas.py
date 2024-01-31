# 1.  Olvassa be és tárolja el az utasadat.txt fájl tartalmát! 
utasok = []
with open('utasadat.txt', 'r') as f:
  for sor in f:
    utasok.append(sor.strip().split())

# 2.  Adja meg, hogy hány utas szeretett volna felszállni a buszra! 
# 2. feladat 
# A buszra 699 utas akart felszállni. 
print('2. feladat')
print(f'A buszra {len(utasok)} utas akart felszállni.')

# 3.  A közlekedési társaság szeretné, ha a járművőn csak az érvényes jeggyel vagy bérlettel 
# rendelkezők utaznának. Ezért a jegyeket és bérleteket a buszvezető a felszálláskor ellenőrzi. 
# (A bérlet  még  érvényes  a  lejárat  napján.)  Adja  meg,  hogy  hány  esetben  kellett 
# a buszvezetőnek elutasítania az utas felszállását, mert lejárt a bérlete vagy már nem volt 
# jegye! 
# 3. feladat 
# A buszra 21 utas nem szállhatott fel. 
nem_ervenyes = 0
for utas in utasok:
  if utas[4] == '0': 
    nem_ervenyes += 1
  elif (len(utas[4])>2 and (utas[1][:8] > utas[4])):
    nem_ervenyes += 1
print('3. feladat')
print(f'A buszra {nem_ervenyes} utas nem szállhatott fel.')

# 4.  Adja meg, hogy melyik megállóban próbált meg felszállni a legtöbb utas! (Több azonos 
# érték esetén a legkisebb sorszámút adja meg!) 
# 4. feladat 
# A legtöbb utas (39 fő) a 8. megállóban próbált felszállni. 
max_megallo = 0
max_utasszam = 0
for megallo in range(30):
  utasszam = len([utas for utas in utasok if utas[0] == str(megallo)])
  if utasszam > max_utasszam:
    max_utasszam = utasszam
    max_megallo = megallo
print('4. feladat')
print(f'A legtöbb utas ({max_utasszam} fő) a {max_megallo}. megállóban próbált felszállni.')

# 5.  A közlekedési társaságnak kimutatást kell készítenie, hogy hányszor utaztak valamilyen 
# kedvezménnyel a járművön. Határozza meg, hogy hány kedvezményes és hány ingyenes 
# utazó szállt fel a buszra! (Csak az érvényes bérlettel rendelkező szállhatott fel a buszra!) 
# 5. feladat 
# Ingyenesen utazók száma: 133 fő 
# A kedvezményesen utazók száma: 200 fő
ingyenes = 0
kedvezmenyes = 0
for utas in utasok:
  if (utas[3] in ['NYP','RVS','GYK']) and (utas[1][:8] <= utas[4]):
    ingyenes += 1
  elif (utas[3] in ['TAB','NYB']) and (utas[1][:8] <= utas[4]):
    kedvezmenyes += 1
print('5. feladat')
print(f'Ingyenesen utazók száma: {ingyenes} fő')
print(f'A kedvezményesen utazók száma: {kedvezmenyes} fő')

# 6.  Készítsen  függvényt  napokszama  néven  az  alábbi  algoritmus  alapján.  Az  algoritmus 
# a paraméterként megadott két dátumhoz (év, hónap, nap) megadja a közöttük eltelt napok 
# számát! (A MOD a maradékos osztást, a DIV az egészrészes osztást jelöli.) Az algoritmust 
# a fuggveny.txt fájlban is megtalálja. A függvényt a következő feladat megoldásához 
# felhasználhatja.
# Függvény napokszama(e1:egész, h1:egész, n1: egész, e2:egész, h2: egész, n2: egész): egész
# 	h1 = (h1 + 9) MOD 12
# 	e1 = e1 - h1 DIV 10
# 	d1= 365*e1 + e1 DIV 4 - e1 DIV 100 + e1 DIV 400 + (h1*306 + 5) DIV 10 + n1 - 1
# 	h2 = (h2 + 9) MOD 12
# 	e2 = e2 - h2 DIV 10
# 	d2= 365*e2 + e2 DIV 4 - e2 DIV 100 + e2 DIV 400 + (h2*306 + 5) DIV 10 + n2 - 1
# 	napokszama:= d2-d1
# Függvény vége
def napokszama(e1,h1,n1,e2,h2,n2):
  h1 = (h1 + 9) % 12
  e1 = e1 - h1 // 10
  d1= 365*e1 + e1 // 4 - e1 // 100 + e1 // 400 + (h1*306 + 5) // 10 + n1 - 1
  h2 = (h2 + 9) % 12
  e2 = e2 - h2 // 10
  d2= 365*e2 + e2 // 4 - e2 // 100 + e2 // 400 + (h2*306 + 5) // 10 + n2 - 1
  return d2-d1

# 7.  A közlekedési társaság azoknak az utasoknak, akiknek még érvényes, de 3 napon belül lejár 
# a bérlete, figyelmeztetést szeretne küldeni e-mailben. (Például, ha a felszállás időpontja 
# 2019. február 5., és a bérlet érvényessége 2019. február 8., akkor már kap az utas levelet, 
# ha 2019. február 9. az érvényessége, akkor még nem kap levelet.) Válogassa ki és írja a 
# figyelmeztetes.txt  állományba  ezen  utasok  kártyaazonosítóját  és  a  bérlet 
# érvényességi idejét (éééé-hh-nn formátumban) szóközzel elválasztva!
with open('figyelmeztetes.txt', 'w') as f:
  for utas in utasok:
    if len(utas[4])>2 and (0<= napokszama(int(utas[1][:4]),int(utas[1][4:6]),int(utas[1][6:8]),int(utas[4][:4]),int(utas[4][4:6]),int(utas[4][6:])) <= 3):
      print(f'{utas[2]} {utas[4][:4]}-{utas[4][4:6]}-{utas[4][6:8]}', file=f)


