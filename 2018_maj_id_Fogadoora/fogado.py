# 1.  Olvassa be és tárolja el a fogado.txt fájl tartalmát! 
foglalasok = []
with open('fogado.txt', 'r') as f:
  for sor in f:
    foglalasok.append(sor.strip().split(' '))

# 2.  Írja a képernyőre, hogy hány foglalás adatait tartalmazza a fájl! 
# 2. feladat 
# Foglalások száma: 161 
print('2. feladat')
print('Foglalások száma: ', len(foglalasok))

# 3.  Kérje be a felhasználótól egy tanár nevét, majd jelenítse meg a mintának megfelelően 
# a képernyőn, hogy a megadott tanárnak hány időpontfoglalása van! Ha a megadott tanárhoz 
# – ilyen például Farkas Attila – még nem történt foglalás, akkor „A megadott néven nincs 
# időpontfoglalás.” üzenetet jelenítse meg! 
# 3. feladat 
# Adjon meg egy nevet: Nagy Ferenc 
# Nagy Ferenc néven 6 időpontfoglalás van. 
print('3. feladat')
vezeteknev, keresztnev = input('Adjon meg egy nevet: ').split(' ')
foglalasok_szama = len([f for f in foglalasok if f[0] == vezeteknev and f[1] == keresztnev])
if foglalasok_szama == 0:
  print('A megadott néven nincs időpontfoglalás.')
else:
  print(vezeteknev, keresztnev, 'néven', foglalasok_szama, 'időpontfoglalás van.')

# 4.  Kérjen be a felhasználótól egy érvényes időpontot a forrásfájlban található formátumban 
# (pl. 17:40)! A program írja a képernyőre a megadott időpontban foglalt tanárok névsorát! 
# Egy sorban egy név szerepeljen! A névsor ábécé szerint rendezett legyen! A rendezett 
# névsort írja ki fájlba is, és ott is soronként egy név szerepeljen! Az időpontnak megfelelő 
# fájlnevet használjon, például 17:40 esetén a 1740.txt fájlban tárolja el az adatokat! 
# Ügyeljen arra, hogy a fájlnév a kettőspont karaktert ne tartalmazza! (Amennyiben ezen 
# a néven nem tudja a fájlt létrehozni, használja az adatok.txt állománynevet!) 
# 4. feladat 
# Adjon meg egy érvényes időpontot (pl. 17:10): 17:40 
# Beke Bianka 
# Csorba Ede 
# Fodor Zsuzsanna 
# Hantos Hedvig 
# Keller Katalin 
# Magos Magdolna 
# Nagy Marcell 
# Olasz Ferenc 
# Papp Lili 
# Szalai Levente 
# Veres Gergely 
print('4. feladat')
idopont = input('Adjon meg egy érvényes időpontot (pl. 17:10): ')
tanarok = [f[0] + ' ' + f[1] for f in foglalasok if f[2] == idopont]
tanarok.sort()
print('\n'.join(tanarok))
with open(idopont[0:2] + idopont[3:] + '.txt', 'w') as f:
  print('\n'.join(tanarok), file=f)

# 5.  Határozza meg, majd írja ki a képernyőre a legkorábban lefoglalt időpont minden adatát! 
# Az adatok megjelenítésénél pontosan kövesse a feladat végén szereplő mintát!
# 5. feladat 
# Tanár neve: Csorba Ede 
# Foglalt időpont: 16:30 
# Foglalás ideje: 2017.10.28-18:48 
print('5. feladat')
legkorabbifoglalas = min(foglalasok, key=lambda f: f[3]) 
print('Tanár neve:', legkorabbifoglalas[0], legkorabbifoglalas[1])
print('Foglalt időpont:', legkorabbifoglalas[2])
print('Foglalás ideje:', legkorabbifoglalas[3])

# 6.  Írja ki a képernyőre „Barna Eszter” tanárnő szabad időpontjait! Tudjuk, hogy a tanárnőnek 
# legalább egy foglalt és több szabad időpontja is van. A tanárnő a legutolsó szülő fogadása 
# után távozhat az iskolából. Mikor távozhat legkorábban? Az időpontot azonosíthatóan írja 
# ki a képernyőre!
# 6. feladat 
# 16:00 
# 16:10 
# 17:00 
# 17:40 
# 17:50 
# Barna Eszter legkorábban távozhat: 17:40
print('6. feladat')
barna_foglalasok = [f for f in foglalasok if f[0] == 'Barna' and f[1] == 'Eszter']
barna_foglalasok.sort(key=lambda f: f[2])
idopontok = ['16:00', '16:10', '16:20', '16:30', '16:40', '16:50', '17:00', '17:10', '17:20', '17:30', '17:40', '17:50']
for idopont in idopontok:
  if idopont not in [f[2] for f in barna_foglalasok]:
    print(idopont)
tavozas_ora, tavozas_perc = barna_foglalasok[-1][2].split(':')
if tavozas_perc == '50':
  tavozas_ora = str(int(tavozas_ora) + 1)
  tavozas_perc = '00'
else:
  tavozas_perc = str(int(tavozas_perc) + 10)
print(f'Barna Eszter legkorábban távozhat: {tavozas_ora}:{tavozas_perc}')