# 1.  Olvassa be és tárolja el az osvenyek.txt és a dobasok.txt állományok tartalmát! 
osvenyek = []
with open("osvenyek.txt", "r") as file:
    for sor in file:
        osvenyek.append(list(sor.strip()))

with open("dobasok.txt", "r") as file:
    dobasok = list(map(int,file.readline().strip().split(" ")))

# 2.  Jelenítse meg a képernyőn, hogy hány ösvény adatait tartalmazza az osvenyek.txt fájl, 
# és mennyi dobás szerepel a dobasok.txt fájlban! 
# 2. feladat 
# A dobások száma: 1956 
# Az ösvények száma: 43 
print("2. feladat")
print(f"A dobások száma: {len(dobasok)}")
print(f"Az ösvények száma: {len(osvenyek)}")

# 3.  Határozza meg, hogy melyik ösvény áll a legtöbb mezőből, és jelenítse meg az ösvény 
# sorszámát és a mezők számát! Ha több ilyen is van, elegendő egyet megjelenítenie. 
# 3. feladat 
# Az egyik leghosszabb a(z) 11. ösvény, hossza: 206 
print("3. feladat")
max_i = 0  
max_hossz = 0
for i in range(1,len(osvenyek)+1):
    if len(osvenyek[i-1]) > max_hossz:
        max_hossz = len(osvenyek[i-1])
        max_i = i      
print(f"Az egyik leghosszabb a(z) {max_i}. ösvény, hossza: {max_hossz}")

# 4.  Olvassa be és tárolja el egy ösvény sorszámát és a játékot játszók számát (legalább 2, 
# legfeljebb 5)! A későbbiekben ezekkel az adatokkal dolgozzon! 
# 4. feladat 
# Adja meg egy ösvény sorszámát! 9 
# Adja meg a játékosok számát! 5 
print("4. feladat")
osveny = int(input("Adja meg egy ösvény sorszámát! "))
jatekosok = int(input("Adja meg a játékosok számát! "))

# 5.  Készítsen statisztikát a megadott sorszámú ösvény mezőiből! Jelenítse meg, hogy ez milyen 
# típusú mezőből mennyit tartalmaz! Ha egy adott típusú mező nem szerepel, akkor azt ne 
# jelenítse meg! (Megoldása teszteléséhez használja az első három ösvényt is, ezek ugyanis 
# nem tartalmaznak minden karaktert!) 
# 5. feladat 
# M: 185 darab 
# V: 8 darab 
# E: 8 darab 
print("5. feladat")
m_lista = [betu for betu in osvenyek[osveny-1] if betu == "M"]
v_lista = [betu for betu in osvenyek[osveny-1] if betu == "V"]
e_lista = [betu for betu in osvenyek[osveny-1] if betu == "E"]
if len(m_lista) > 0:
    print(f"M: {len(m_lista)} darab")
if len(v_lista) > 0:
    print(f"V: {len(v_lista)} darab")
if len(e_lista) > 0:
    print(f"E: {len(e_lista)} darab")

# 6.  Írja  a  kulonleges.txt  fájlba,  hogy  a  választott  ösvény  mely  mezői  különlegesek! 
# Soronként egy mezőt adjon meg a mező sorszámával és a mező típusát megadó karakterrel! 
# A két értéket egy tabulátor karakterrel válassza el egymástól!
# (A fájlban a mezők sorszámozása 1-től kezdődik! A különleges mezők típusai: V, E. A fájl az 5. ösvényhez készült.) 
with open("kulonleges.txt", "w") as f:
    for i in range(len(osvenyek[osveny-1])):
        if osvenyek[osveny-1][i] != "M":
            print(f"{i+1}\t{osvenyek[osveny-1][i]}", file=f)

# 7.  Határozza meg, hogy melyik játékos jutna a legmesszebb, ha a választott ösvényen minden 
# mező M típusú lenne! Jelenítse meg a legtávolabb jutó(k) sorszámát és azt, hogy a dobások 
# hányadik körében alakult ki a végeredmény! Ha több ilyen játékos van, elegendő csak egyet 
# megjelenítenie. 
# 7. feladat 
# A játék a(z) 54. körben fejeződött be. A legtávolabb jutó(k) sorszáma: 5 
print("7. feladat")
pozicio = [0]*jatekosok
osveny_hossza = len(osvenyek[osveny-1])
for i in range(len(dobasok)):
    pozicio[i%jatekosok] += dobasok[i]
    if pozicio[i%jatekosok] >= osveny_hossza:
        print(f"A játék a(z) {i//jatekosok+1}. körben fejeződött be. A legtávolabb jutó(k) sorszáma: {i%jatekosok+1}")
        break

# 8.  Határozza meg, ki nyer, ha figyelembe veszi a mezők típusát is! Jelenítse meg a nyertes(ek) 
# sorszámát és azt, hogy a többi bábu milyen sorszámú mezőn áll az utolsó teljes kör végén!
# 8. feladat 
# Nyertes(ek): 4 5  
# A többiek pozíciója: 
# 1. játékos, 153. mező 
# 2. játékos, 185. mező 
# 3. játékos, 183. mező 
print("8. feladat")
pozicio = [0]*jatekosok
van_nyertes = False

for i in range(0,len(dobasok),jatekosok):
    for j in range(jatekosok):
        if pozicio[j] + dobasok[i+j] >= osveny_hossza:
            pozicio[j] += dobasok[i+j]
        elif osvenyek[osveny-1][pozicio[j] + dobasok[i+j]-1] == "M":
            pozicio[j] += dobasok[i+j]
        elif osvenyek[osveny-1][pozicio[j] + dobasok[i+j]-1] == "E": 
            pozicio[j] += dobasok[i+j]*2
  
        if pozicio[j] >= osveny_hossza:
            van_nyertes = True
      
    if van_nyertes:
        break
nyertesek = [str(i+1) for i in range(jatekosok) if pozicio[i] >= osveny_hossza]
print(f"Nyertes(ek): {' '.join(nyertesek)}")
print("A többiek pozíciója:")
for i in range(jatekosok):
    if pozicio[i] < osveny_hossza:
        print(f"{i+1}. játékos, {pozicio[i]} mező")    


    