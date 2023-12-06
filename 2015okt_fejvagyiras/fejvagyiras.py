# 1. Szimuláljon egy pénzfeldobást, ahol azonos esélye van a fejnek és az írásnak is! 
# Az eredményt írassa ki a képernyőre a mintának megfelelően! 
import random
print("1. feladat")
dobas = random.choice(["F", "I"])
print("A pénzfeldobás eredménye: ", dobas)

# 2. Kérjen  be  a  felhasználótól  egy  tippet,  majd  szimuláljon  egy  pénzfeldobást!  Írassa  ki a képernyőre a felhasználó tippjét és a dobás eredményét is, majd tájékoztassa 
# a felhasználót  az  eredményről  következő  formában:  „Ön eltalálta.”  vagy  „Ön nem 
# találta el.”!
print("2. feladat")
tipp = input("Tippeljen! (F/I): ")
dobas = random.choice(["F", "I"])
print("A tipp", tipp, ", a pénzfeldobás eredménye: ", dobas)
if tipp == dobas:
    print("Ön eltalálta.")
else:
    print("Ön nem találta el.")

# A kiserlet.txt állományban egy pénzfeldobás-sorozat eredményét találja. Mivel 
# a sorozat  hossza  tetszőleges  lehet,  ezért  az  összes  adat  memóriában  történő  egyidejű 
# eltárolása  nélkül  oldja  meg  a  következő  feladatokat!  Feltételezheti,  hogy  egymilliónál  több adata nem lesz. 
# 3. Állapítsa meg, hány dobásból állt a kísérlet, és a választ a mintának megfelelően írassa ki 
# a képernyőre! 
dobasok = []
with open("kiserlet.txt", "r") as f:
    for sor in f:
        dob = sor.strip()
        dobasok.append(dob)
print("3. feladat")
print("A kísérlet ", len(dobasok), "dobásból állt.")

# 4. Milyen  relatív  gyakorisággal  dobtunk  a  kísérlet  során  fejet?  (A  fej  relatív  gyakorisága a fejet  eredményező  dobások  és  az  összes  dobás  hányadosa.)  A  relatív  gyakoriságot a mintának  megfelelően  két  tizedesjegy  pontossággal,  százalék  formátumban  írassa  ki  a képernyőre! 
rel_gyak = round(dobasok.count("F") / len(dobasok) * 100,2)
print("4. feladat")
print("A kísérlet során a fej relatív gyakorisága: ", rel_gyak, "%")

# 5. Hányszor  fordult  elő  ebben  a  kísérletben,  hogy  egymás  után  pontosan  két  fejet  dobtunk? A  választ a mintának megfelelően írassa ki a képernyőre! (Feltételezheti, hogy a kísérlet 
# legalább 3 dobásból állt.) Például az IFFFFIIFFIFFFIFF sorozatban kétszer fordult elő, hogy egymás után pontosan két fejet dobtunk. 
ketfejek = 0
if dobasok[0] == "F" and dobasok[1] == "F" and dobasok[1] == "I":
    ketfejek += 1
if dobasok[-3] == "I" and dobasok[-2] == "F" and dobasok[-1] == "F":
    ketfejek += 1
for i in range(len(dobasok)-3):
    if dobasok[i] == "I" and dobasok[i+1] == "F" and dobasok[i+2] == "F" and dobasok[i+3] == "I":
        ketfejek += 1
print("5. feladat")
print("A kísérlet során", ketfejek, "alkalommal dobtak egymás után pontosan két fejet.")

# 6. Milyen  hosszú  volt  a  leghosszabb,  csak  fejekből  álló  részsorozat?  Írassa  ki  a  választ a képernyőre  a  mintának  megfelelően,  és  adja  meg  egy  ilyen  részsorozat  első  tagjának helyét is! (A minta tagjainak számozását eggyel kezdjük.) 
print("6. feladat")
max_hossz = 0
max_hely = 0
hossz = 0
hely = 0
for i in range(len(dobasok)):
    hossz = 1
    if dobasok[i] == "F":
        while i+hossz < len(dobasok)-1 and dobasok[i+hossz] == "F":
            hossz += 1 
        if hossz > max_hossz:
            max_hossz = hossz
            max_hely = i + 1
print(f"A leghosszabb fejekből álló részsorozat a(z) {max_hely}. dobástól kezdődik, és {max_hossz} tagból áll.")

# 7. Állítson  elő  és  tároljon  a  memóriában  1000  db  négy  dobásból  álló  sorozatot!  Számolja  
# meg,  hogy  hány  esetben  követett  egy  háromtagú  „tisztafej”  sorozatot  fej,  illetve  hány  
# esetben írás! Az eredményt írassa ki a dobasok.txt állományba úgy, hogy az első sorba 
# kerüljön  az  eredmény,  a  második  sorban  pedig  egy-egy  szóközzel  elválasztva,  egyetlen  
# sorban szerepeljenek a dobássorozatok! 
# Például: 
# FFFF: 12, FFFI: 14 
# FIFI IIIF IFIF IIII FFII FFFF IIFI FFII FFFI ...
print("7. feladat")
dobasok = []
for i in range(1000):
    dobas = ""
    for j in range(4):
        dobas += random.choice(["F", "I"])
    dobasok.append(dobas)
with open("dobasok.txt", "w") as f:
    print(f"FFFF: {dobasok.count('FFFF')}, FFFI: {dobasok.count('FFFI')}", file=f)
    print(" ".join(dobasok), file=f)  



