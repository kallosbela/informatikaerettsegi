# 1.  Olvassa be és tárolja el a meresek.txt állomány adatait! 
autok = []
with open('meresek.txt', 'r', encoding='utf-8') as file:
  sorok = file.readlines()
  autok = [sor.strip().split() for sor in sorok]

# 2.  Írja ki a képernyőre, hogy hány jármű adatait rögzítették a mérés során! 
print(f"2. feladat\nA mérés során {len(autok)} jármű adatait rögzítették.")

# 3.  Határozza meg a rendelkezésre álló adatok segítségével, hogy 9 óra előtt hány jármű haladt át a szakasz végpontján! A kapott értéket írja ki a képernyőre! 
print("3. feladat")
kilencelotti=[auto for auto in autok if int(auto[5])<9] 
print(f"9 óra előtt {len(kilencelotti)} jármű haladt el a végponti mérőnél.")

# 4.  Kérjen be a felhasználótól egy óra, perc értéket!  
# a.  Határozza  meg,  hogy  abban  a  percben  hány  jármű  haladt  el  a  kezdő méréspontnál! Ha az adott percben nem haladt el jármű a méréspontnál, akkor a 0 értéket jelenítse meg! 
# b.  Számítsa  ki  a  forgalomsűrűséget,  amely  a  megadott  időpontban  kezdődő percben  (pl.:  ha  a  megadott  óra  perc  08:09  volt,  akkor  08:09:00,000-08:09:59,999  között)  az  útszakaszon  lévő  járművek  száma  és  az  útszakasz hosszának hányadosa. Az értéket tizedes tört alakban jelenítse meg.
print("4. feladat") 
ora, perc = map(int,input("Adjon meg egy óra és perc értéket!").strip().split())

elhaladt = [auto for auto in autok if int(auto[1])==ora and int(auto[2])==perc]
print(f"a. A kezdeti méréspontnál elhaladt járművek száma: {len(elhaladt)}")

uton = [auto for auto in autok if (int(auto[1])==ora and int(auto[2])==perc) or (int(auto[5])==ora and int(auto[6])==perc) or (int(auto[1])*60+int(auto[2])<ora*60+perc and int(auto[5])*60+int(auto[6])>=ora*60+perc+1)] 
print(f"b. A forgalomsűrűség: {len(uton)/10}") 
 
# 5.  Mekkora  volt  a  legnagyobb  átlagsebességgel  haladó  járműnek  a  sebessége,  és  hány 
# járművet hagyott le a mért szakasz végére? Amennyiben több legnagyobb átlagsebesség 
# érték van, akkor elég az egyiket kiírnia. Az autó rendszámát, az átlagsebességet egész 
# számként és a lehagyott járművek számát jelenítse meg!
def ido_be(auto):
  return int(auto[1])*3600+int(auto[2])*60+int(auto[3])+int(auto[4])/1000 #másodpercben

def ido_ki(auto):
  return int(auto[5])*3600+int(auto[6])*60+int(auto[7])+int(auto[8])/1000 #másodpercben

print("5. feladat\nA legnagyobb sebességgel haladó jármű")
max_v = 0
max_v_auto = []
for auto in autok:
  ido_oraban = (ido_ki(auto)-ido_be(auto))/3600
  sebesseg = 10/ido_oraban
  if sebesseg>max_v:
    max_v = sebesseg
    max_v_auto = auto
lehagyott = [auto for auto in autok if ido_be(auto)<ido_be(max_v_auto) and ido_ki(auto)>ido_ki(max_v_auto)]
print(f"rendszáma: {max_v_auto[0]}")
print(f"átlagsebessége: {int(max_v)} km/h") 
print(f"által lehagyott járművek száma: {len(lehagyott)}")
 
# 6.  Határozza meg, hogy a járművek hány százalékának az átlagsebessége haladta meg az 
# útszakaszon megengedett legnagyobb sebességet (90 km/h)! Az értéket tizedes tört alakban 
# jelenítse meg a minta szerint! 
gyorshajto = [auto for auto in autok if 10/((ido_ki(auto)-ido_be(auto))/3600)>90]
print(f"6. feladat\nA járművek {len(gyorshajto)/len(autok)*100:.2f}%-a volt gyorshajtó.")

# 7.  Készítsen egy szöveges állományt buntetes.txt néven, amely a gyorshajtók adatait 
# tartalmazza! Ebbe a szöveges állományba azon járművek adatai kerüljenek be, amelyek 
# átlagsebessége 104 km/h-nál nagyobb! A fájlban a jármű rendszáma, az átlagsebesség egész 
# számként megjelenítve és a büntetés összege szerepeljen mértékegységgel, pontosvesszővel 
# vagy tabulátorokkal elválasztottan!
def buntetes(auto):
  sebesseg = 10/((ido_ki(auto)-ido_be(auto))/3600)
  if sebesseg>151:
    return 200000
  elif sebesseg>136:
    return 60000
  elif sebesseg>121:
    return 45000
  elif sebesseg>104:
    return 30000
  else:
    return 0
buntetett = [auto for auto in autok if buntetes(auto)>0]
with open("buntetes.txt", "w", encoding="utf-8") as fajl:
  for auto in buntetett:
    sebesseg = round(10/((ido_ki(auto)-ido_be(auto))/3600))
    print(auto[0]+"; "+str(int(sebesseg))+" km/h; "+str(buntetes(auto))+" Ft", file=fajl)
print("A fájl elkészült.")
