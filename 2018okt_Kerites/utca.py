# 1.  Olvassa be és tárolja el a kerites.txt fájl tartalmát! 
kerites = []
with open('kerites.txt', 'r') as f:
    for sor in f:
        kerites.append(sor.strip().split())

# 2.  Írja a képernyőre, hogy hány telket adtak el az utcában! 
# 2. feladat 
# Az eladott telkek száma: 98 
print('2. feladat')
print(f'Az eladott telkek száma: {len(kerites)}')

# 3.  Jelenítse meg a képernyőn, hogy az utolsó eladott telek 
# a.  melyik (páros / páratlan) oldalon talált gazdára! 
# b.  milyen házszámot kapott! 
# 3. feladat 
# A páros oldalon adták el az utolsó telket. 
# Az utolsó telek házszáma: 78 
print('3. feladat')
paros_e = kerites[-1][0] == '0' 
parosoldal = [sor for sor in kerites if sor[0] == '0']
paratlanoldal = [sor for sor in kerites if sor[0] == '1']
if paros_e:
    print('A páros oldalon adták el az utolsó telket.')
    print(f'Az utolsó telek házszáma: {len(parosoldal)*2}') # n-edik páros szám = 2*n
else:
    print('A páratlan oldalon adták el az utolsó telket.')
    print(f'Az utolsó telek házszáma: {len(paratlanoldal)*2-1}') # n-edik páratlan szám = 2*n-1

# 4.  Írjon a képernyőre egy házszámot a páratlan oldalról, amely melletti telken ugyanolyan 
# színű a kerítés! (A hiányzó és a festetlen kerítésnek nincs színe.) Feltételezheti, hogy van 
# ilyen telek, a több ilyen közül elég az egyik ház számát megjeleníteni.
# 4. feladat 
# A szomszédossal egyezik a kerítés színe: 73
print('4. feladat')
for i in range(len(paratlanoldal)-1):
    if paratlanoldal[i][2] not in [':','#'] and paratlanoldal[i][2] == paratlanoldal[i+1][2] :
        print(f'A szomszédossal egyezik a kerítés színe: {2*i+1}')
        break

# 5.  Kérje be a felhasználótól egy eladott telek házszámát, majd azt felhasználva oldja meg a 
# következő feladatokat! 
# a.  Írja ki a házszámhoz tartozó kerítés színét, ha már elkészült és befestették, 
# egyébként az állapotát a „#” vagy „:” karakter jelöli! 
# b.  A házszámhoz tartozó kerítést szeretné tulajdonosa be- vagy átfesteni. Olyan 
# színt akar választani, amely különbözik a mellette lévő szomszéd(ok)tól és a 
# jelenlegi színtől is. Adjon meg egy lehetséges színt! A színt a teljes palettából 
# (A–Z) szabadon választhatja meg. 
# 5. feladat 
# Adjon meg egy házszámot! 83 
# A kerítés színe / állapota: A 
# Egy lehetséges festési szín: D
    
print('5. feladat')
abc = []
start = ord('A')
for i in range(26):
    abc.append(chr(start + i))

hazszam = int(input('Adjon meg egy házszámot! '))
if hazszam % 2 == 0:
    oldal = '0'
    index = hazszam // 2 - 1
else:
    oldal = '1'
    index = (hazszam - 1) // 2
teljesoldal = [sor for sor in kerites if sor[0] == oldal]
print(f'A kerítés színe / állapota: {teljesoldal[index][2]}')
szomszedok_es_sajat_szinek = []
if index == 0:
    szomszedok_es_sajat_szinek.append(teljesoldal[0][2])
    szomszedok_es_sajat_szinek.append(teljesoldal[1][2])
elif index == len(teljesoldal)-1:
    szomszedok_es_sajat_szinek.append(teljesoldal[index-1][2])
    szomszedok_es_sajat_szinek.append(teljesoldal[index][2])
else:
    szomszedok_es_sajat_szinek.append(teljesoldal[index-1][2])
    szomszedok_es_sajat_szinek.append(teljesoldal[index][2])
    szomszedok_es_sajat_szinek.append(teljesoldal[index+1][2])

for szin in abc:
    if szin not in szomszedok_es_sajat_szinek:
        ujszin = szin
        print(f'Egy lehetséges festési szín: {ujszin}')
        break

# 6.  Jelenítse meg az utcakep.txt fájlban a páratlan oldal utcaképét az alábbi mintának 
# megfelelően! 
# KKKKKKKK::::::::::SSSSSSSSSBBBBBBBBFFFFFFFFFKKKKKKKKKKIIIIIIII 
# 1       3         5        7       9        11        13 
# Az első sorban a páratlan oldal jelenjen meg, a megfelelő méternyi szakasz kerítésszínét 
# (vagy állapotát) jelző karakterrel! A második sorban a telek első karaktere alatt kezdődően 
# a házszám álljon!
utcakep1 = ''
utcakep2 = ''
for index, sor in enumerate(paratlanoldal):
    szin = sor[2]
    hazszam = 2*index + 1
    hossz = int(sor[1])
    utcakep1 += szin * hossz
    utcakep2 += str(hazszam) + ' ' * (hossz-len(str(hazszam)))
with open('utcakep.txt', 'w') as f:
    print(utcakep1, file=f)
    print(utcakep2, file=f)
