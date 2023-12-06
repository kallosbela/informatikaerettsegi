import math

bemenet = open("jel.txt")
jelek = []
for sor in bemenet:
    jel = sor.strip().split()
    jelek.append(list(map(int, jel)))
bemenet.close()

print("2. feladat")
sorszám = int(input("Adja meg a jel sorszámát! "))
print(f"x={jelek[sorszám-1][3]} y={jelek[sorszám-1][4]}")

print("3. feladat")
def eltelt(jel1, jel2):
    return abs((jel2[0] - jel1[0]) * 3600 + (jel2[1] - jel1[1]) * 60 + (jel2[2]-jel1[2]))

print("4. feladat")
különbség = eltelt(jelek[0], jelek[-1])
óra = különbség // 3600
perc = (különbség % 3600) // 60
mperc = különbség % 60
print(f"Időtartam: {óra}:{perc}:{mperc}")

print("5. feladat")
minx = 10000
maxx = -10000
miny = 10000
maxy = -10000
for jel in jelek:
    minx = min(minx, jel[3])
    maxx = max(maxx, jel[3])
    miny = min(miny, jel[4])
    maxy = max(maxy, jel[4])
print(f"Bal alsó: {minx} {miny}, jobb felső: {maxx} {maxy}")

print("6. feladat")
jelek_száma = len(jelek)
def táv(jel1, jel2):
    return math.sqrt( (jel2[3]-jel1[3])**2 +  (jel2[4]-jel1[4])**2 )
összesen = 0
for index in range(jelek_száma-1):
    összesen += táv(jelek[index], jelek[index+1])
print(f"Elmozdulás: {összesen:0.3f} egység")

print("7. feladat")
kimenet = open("kimaradt.txt", "w", encoding="utf8")
for index in range(jelek_száma-1):
    kimaradt_távolság_szerint = 0
    kimaradt_idő_szerint = 0
    időkülönbség = eltelt(jelek[index], jelek[index+1])
    if időkülönbség > 300:
        kimaradt_idő_szerint = (időkülönbség-1)//300
    távolság = max( abs(jelek[index+1][3]-jelek[index][3]), abs(jelek[index+1][4]-jelek[index][4]) )
    if távolság > 10:
        kimaradt_távolság_szerint = (távolság-1) // 10
    if kimaradt_távolság_szerint > kimaradt_idő_szerint:
        print(jelek[index+1][0], jelek[index+1][1], jelek[index+1][2], "koordináta-eltérés", kimaradt_távolság_szerint, file=kimenet)
    if kimaradt_idő_szerint > kimaradt_távolság_szerint:
        print(jelek[index+1][0], jelek[index+1][1], jelek[index+1][2], "időeltérés", kimaradt_idő_szerint, file=kimenet)
kimenet.close()