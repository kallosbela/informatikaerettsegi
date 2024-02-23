# 1.  Olvassa be a kep.txt állomány tartalmát, és tárolja el a 640×360 képpont színét! 
kep = []
with open("kep.txt", "r") as file:
    for sor in file:
        kep.append(sor.strip().split(" "))

# 2.  Kérje be a felhasználótól a kép egy pontjának sor- és oszlopszámát (a számozás mindkét 
# esetben 1-től indul), és írja a képernyőre az adott képpont RGB színösszetevőit a minta 
# szerint! 
# 2. feladat: 
# Kérem egy képpont adatait! 
# Sor:180 
# Oszlop:320 
# A képpont színe RGB(184,183,181) 
print('2. feladat:')
sor = int(input('Kérem egy képpont adatait!\nSor: '))
oszlop = int(input('Oszlop: '))
print(f'A képpont színe RGB({kep[sor-1][(oszlop-1)*3]},{kep[sor-1][(oszlop-1)*3+1]},{kep[sor-1][(oszlop-1)*3+2]})')

# 3.  Világosnak tekintjük az olyan képpontot, amely RGB-értékeinek összege 600-nál nagyobb. 
# Számolja meg és írja ki, hogy a teljes képen hány világos képpont van! 
# 3. feladat: 
# A világos képpontok száma: 7837 
print('3. feladat:')
vilagos = 0
for sor in kep:
    for i in range(0, len(sor), 3):
        if int(sor[i])+int(sor[i+1])+int(sor[i+2]) > 600:
            vilagos += 1
print(f'A világos képpontok száma: {vilagos}')

# 4.  A kép legsötétebb pontjainak azokat a pontokat tekintjük, amelyek RGB-értékeinek összege 
# a legkisebb. Adja meg, hogy mennyi a legkisebb összeg, illetve keresse meg az ilyen RGB 
# összegű  pixeleket,  és  írja  ki  mindegyik  színét  RGB(r,g,b)  formában  a  mintának 
# megfelelően! 
# 4. feladat: 
# A legsötétebb pont RGB összege: 197 
# A legsötétebb pixelek színe: 
# RGB(0,85,112) 
# RGB(0,86,111) 
# RGB(0,86,111) 
print('4. feladat:')
legsotetebb = 255*3
for sor in kep:
    for i in range(0, len(sor), 3):
        if int(sor[i])+int(sor[i+1])+int(sor[i+2]) < legsotetebb:
            legsotetebb = int(sor[i])+int(sor[i+1])+int(sor[i+2])
print(f'A legsötétebb pont RGB összege: {legsotetebb}')
for sor in kep:
    for i in range(0, len(sor), 3):
        if int(sor[i])+int(sor[i+1])+int(sor[i+2]) == legsotetebb:
            print(f'RGB({sor[i]},{sor[i+1]},{sor[i+2]})')
            
# 5.  A képen a kék ég látható közepén egy felhővel. Az ég és a felhő színe között jelentős 
# különbség  van,  így  az  ég-felhő  határvonal  programmal  is  felismerhető.  Ennek 
# megtalálásához készítsen függvényt hatar néven, amely megadja, hogy egy adott sorban 
# van-e olyan hely a képen, ahol az egymás melletti képpontok kék színösszetevőinek eltérése 
# meghalad egy adott értéket! A függvény kapja meg paraméterként a sor számát, illetve 
# az eltérés értékét, melyek egészek! A függvény visszatérési értéke egy logikai érték legyen, 
# amely megadja, hogy az adott sorban volt-e az eltérést meghaladó különbség az egymás 
# melletti képpontok kék színében! 
def hatar(sor, elteres):
    for i in range(0, len(kep[sor-1]), 3):
        if i+5 < len(kep[sor-1]): # ha nincs elég képpont a sor végén, akkor nem vizsgáljuk
            if abs(int(kep[sor-1][i+2])-int(kep[sor-1][i+5])) > elteres:
                return True
    return False

# 6.  Keresse  meg  a  képen  a  felhő  első  és  utolsó  sorát  az  előzőleg  elkészített  függvény 
# segítségével úgy, hogy eltérésként 10-et ad meg a függvénynek bemenetként! Adja meg 
# az első és az utolsó olyan sor sorszámát, ahol az eltérés a soron belül valahol 10-nél 
# nagyobb!
# 6. feladat: 
# A felhő legfelső sora: 103 
# A felhő legalsó sora: 280
print('6. feladat:')
felso = 0
also = 0
for i in range(1, len(kep)+1):
    if hatar(i, 10):
        felso = i
        break
for i in range(len(kep), 0, -1):
    if hatar(i, 10):
        also = i
        break
print(f'A felhő legfelső sora: {felso}')
print(f'A felhő legalsó sora: {also}')

