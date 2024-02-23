# 1.  Olvassa  be  a  szallit.txt  állomány  adatait,  és  annak  felhasználásával  oldja meg a következő feladatokat! 
szallitas =[]
with open("szallit.txt", "r", encoding="utf-8") as f:
    for sor in f:
        #minden adatból int szám lesz:
        szallitas.append(list(map(int,sor.strip().split()))) 
hossz = int(szallitas[0][0])
lepesido = int(szallitas[0][1])

# 2.  Kérje be egy szállítás sorszámát, majd írassa ki annak indulási és célhelyét! (A szállításokat 1-től sorszámozzuk.)
# 2. feladat 
# Adja meg, melyik adatsorra kíváncsi! 3 
# Honnan: 135 Hova: 54 
print('2. feladat')
szallitasszam = int(input('Adja meg, melyik adatsorra kíváncsi! '))
print(f'Honnan: {szallitas[szallitasszam][1]} Hova: {szallitas[szallitasszam][2]}')                    

# 3.  Készítsen függvényt tav néven, amely megadja a szállítás távolságát a szalag hosszának, valamint az indulási és a célhelynek ismeretében! A függvényt használja fel a későbbi feladatok  megoldása  során.  A  függvényfejet  az  alábbiaknak  megfelelően  készítse  el, 
# megoldásában az ott szereplő változóneveket használja! 
# Függvény tav(szalaghossz, indulashelye, erkezeshelye : egész szám): 
# egész szám 
def tav(szalaghossz, indulashelye, erkezeshelye):
    if indulashelye < erkezeshelye:
        return (erkezeshelye - indulashelye)
    else:
        return (szalaghossz + erkezeshelye - indulashelye)

# 4.  Határozza meg, hogy a rendelkezésre álló szállítások során mekkora volt a legnagyobb szállítási távolság! Írja a képernyőre a maximális távolságot és az összes ilyen hosszúságú 
# szállítás sorszámát! 
# 4. feladat 
# A legnagyobb távolság: 195 
# A maximális távolságú szállítások sorszáma: 31 33 
tavok = [[i,tav(hossz,szallitas[i][1],szallitas[i][2])] for i in range(1,len(szallitas))]
maxtav = (max(tavok, key=lambda x: x[1]))[1]
print('4. feladat')
print(f'A legnagyobb távolság: {maxtav}')
maxszallitasok = [str(tav[0]) for tav in tavok if tav[1] == maxtav]
print(f'A maximális távolságú szállítások sorszáma: {" ".join(maxszallitasok)}')

# 5.  Adja meg, mekkora tömeg haladt el összesen a 0 pozíciójú hely előtt! Az onnan induló vagy oda érkező rekeszeket ne vegye figyelembe! 
# 5. feladat 
# A kezdőpont előtt elhaladó rekeszek össztömege: 957 
print('5. feladat')
tomeg = 0
for i in range(1,len(szallitas)):
    if szallitas[i][1] > szallitas[i][2] and szallitas[i][2] != 0:
        tomeg += szallitas[i][3]
print(f'A kezdőpont előtt elhaladó rekeszek össztömege: {tomeg}')

# 6.  Kérjen  be  egy  időpontot,  és  határozza  meg  az  adott  időpontban  szállított rekeszek sorszámát! Az éppen akkor induló rekeszeket vegye figyelembe, de a célba érőket ne! 
# Ha nem volt szállított rekesz, akkor a rekeszek sorszáma helyett az „üres” szót írja ki! 
# 6. feladat 
# Adja meg a kívánt időpontot! 300 
# A szállított rekeszek halmaza: 1 2 3 6 7 10 11
print('6. feladat')
idopont = int(input('Adja meg a kívánt időpontot! '))
halmaz = []
for i in range(1,len(szallitas)):
    kezdet = szallitas[i][0]
    veg = szallitas[i][0]+tav(hossz,szallitas[i][1],szallitas[i][2])*lepesido
    if kezdet <= idopont < veg:
        halmaz.append(str(i))
# rövidebben:
# halmaz = [str(i) for i in range(1,len(szallitas)) if szallitas[i][0]<=idopont<szallitas[i][0]+tav(hossz,szallitas[i][1],szallitas[i][2])*lepesido]
print(f'A szállított rekeszek halmaza: {" ".join(halmaz)}')

# 7.  Hozza létre a tomeg.txt fájlt, amely megadja, hogy az egyes helyekről összességében 
# mennyi tömeget szállítottak el! Azok a helyek ne jelenjenek meg a fájlban, ahonnan nem 
# történt szállítás! (A fájlba írt adatok sorrendje tetszőleges.) 
szallitott_tomegek = [0]*hossz
for i in range(1,len(szallitas)):
    honnan = szallitas[i][1]
    tomeg = szallitas[i][3]
    szallitott_tomegek[honnan] += tomeg
with open("tomeg.txt", "w", encoding="utf-8") as f:
    for i in range(hossz):
        if szallitott_tomegek[i] != 0:
            print(f'{i} {szallitott_tomegek[i]}', file=f)
    
