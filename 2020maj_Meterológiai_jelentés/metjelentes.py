# 1.  Olvassa be és tárolja el a tavirathu13.txt állomány adatait! 
adatok = []
with open("tavirathu13.txt", "r") as f:
    for sor in f:
        adatok.append(sor.strip().split())

# 2.  Kérje be a felhasználótól egy város kódját! Adja meg, hogy az adott városból mikor érkezett 
# az utolsó mérési adat! A kiírásban az időpontot óó:pp formátumban jelenítse meg! 
# 2. feladat 
# Adja meg egy település kódját! Település: SM 
# Az utolsó mérési adat a megadott településről 23:45-kor érkezett. 
telepules = input("Adja meg egy település kódját! Település: ")
telepules_adatai = [sor for sor in adatok if sor[0] == telepules]
utolso_meres = telepules_adatai[-1]
ora = utolso_meres[1][:2]
perc = utolso_meres[1][2:]
print("2. feladat")
print(f"Az utolsó mérési adat a megadott településről {ora}:{perc}-kor érkezett.")

# 3.  Határozza  meg,  hogy  a  nap  során  mikor  mérték  a  legalacsonyabb  és  a  legmagasabb 
# hőmérsékletet!  Jelenítse  meg  a  méréshez  kapcsolódó  település  nevét,  az  időpontot  és 
# a hőmérsékletet!  Amennyiben  több  legnagyobb  vagy  legkisebb  érték  van,  akkor  elég 
# az egyiket kiírnia. 
# 3. feladat 
# A legalacsonyabb hőmérséklet: SM 23:45 16 fok. 
# A legmagasabb hőmérséklet: DC 13:15 35 fok. 
min_homerseklet = int(adatok[0][3])
max_homerseklet = int(adatok[0][3])
min_homerseklet_adatai = adatok[0]
max_homerseklet_adatai = adatok[0]
for sor in adatok:
    homerseklet = int(sor[3])
    if homerseklet < min_homerseklet:
        min_homerseklet = homerseklet
        min_homerseklet_adatai = sor
    if homerseklet > max_homerseklet:
        max_homerseklet = homerseklet
        max_homerseklet_adatai = sor
print("3. feladat")
print(f"A legalacsonyabb hőmérséklet: {min_homerseklet_adatai[0]} {min_homerseklet_adatai[1][:2]}:{min_homerseklet_adatai[1][2:]} {min_homerseklet_adatai[3]} fok.")
print(f"A legmagasabb hőmérséklet: {max_homerseklet_adatai[0]} {max_homerseklet_adatai[1][:2]}:{max_homerseklet_adatai[1][2:]} {max_homerseklet_adatai[3]} fok.")

# 4.  Határozza meg, azokat a településeket és időpontokat, ahol és amikor a mérések idején 
# szélcsend volt! (A szélcsendet a táviratban 00000 kóddal jelölik.) Ha nem volt ilyen, akkor 
# a „Nem volt szélcsend a mérések idején.” szöveget írja ki! A kiírásnál a település kódját és 
# az időpontot jelenítse meg. 
# 4. feladat 
# BP 01:00 
# DC 02:15 
# SN 03:15 
# BC 04:45 
# DC 04:45 
# SN 05:15 
# SN 05:45 
# KE 08:45 
# BC 11:45 
print("4. feladat")
szelcsendek = [sor for sor in adatok if sor[2] == "00000"]
if len(szelcsendek) == 0:
    print("Nem volt szélcsend a mérések idején.")
else:
    for sor in szelcsendek:
        print(f"{sor[0]} {sor[1][:2]}:{sor[1][2:]}")

# 5.  Határozza meg a települések napi középhőmérsékleti adatát és a hőmérséklet-ingadozását! 
# A kiírásnál a település kódja szerepeljen a sor elején a minta szerint! A kiírásnál csak 
# a megoldott feladatrészre vonatkozó szöveget és értékeket írja ki! 
# a. A középhőmérséklet azon hőmérsékleti adatok átlaga, amikor a méréshez tartozó óra 
# értéke 1., 7., 13., 19. Ha egy településen a felsorolt órák valamelyikén nem volt mérés, 
# akkor a kiírásnál az „NA” szót jelenítse meg! Az adott órákhoz tartozó összes adat 
# átlagaként határozza meg a középhőmérsékletet, azaz minden értéket azonos súllyal 
# vegyen figyelembe! A középhőmérsékletet egészre kerekítve jelenítse meg! 
# b. A hőmérséklet-ingadozás számításhoz az adott településen a napi legmagasabb és
# legalacsonyabb hőmérséklet különbségét kell kiszámítania! (Feltételezheti,  hogy 
# minden település esetén volt legalább két mérési adat.) 
# 5. feladat 
# BP Középhőmérséklet: 23; Hőmérséklet-ingadozás: 8 
# DC Középhőmérséklet: 29; Hőmérséklet-ingadozás: 15 
# SM Középhőmérséklet: 22; Hőmérséklet-ingadozás: 8 
# PA Középhőmérséklet: 21; Hőmérséklet-ingadozás: 7 
# SN Középhőmérséklet: 26; Hőmérséklet-ingadozás: 13 
# PR Középhőmérséklet: 21; Hőmérséklet-ingadozás: 8 
# BC NA; Hőmérséklet-ingadozás: 14 
# PP NA; Hőmérséklet-ingadozás: 6 
# KE NA; Hőmérséklet-ingadozás: 13
        
# 6.  Hozzon létre településenként egy szöveges állományt, amely első sorában a település kódját 
# tartalmazza!  A  további  sorokban  a  mérési  időpontok  és  a  hozzá  tartozó  szélerősségek 
# jelenjenek  meg!  A  szélerősséget  a  minta  szerint  a  számértéknek  megfelelő  számú 
# kettőskereszttel  (#)  adja  meg!  A  fájlban  az  időpontokat  és  a  szélerősséget  megjelenítő 
# kettőskereszteket  szóközzel  válassza  el  egymástól!  A  fájl  neve  X.txt  legyen,  ahol 
# az X helyére a település kódja kerüljön!
print("5. feladat")
telepulesek = set([sor[0] for sor in adatok])
for telepules in telepulesek:
    telepules_adatai = [sor for sor in adatok if sor[0] == telepules]
    orak = ['01', '07', '13', '19']
    homersekletek01 = [int(sor[3]) for sor in telepules_adatai if int(sor[1][:2]) == 1]
    homersekletek07 = [int(sor[3]) for sor in telepules_adatai if int(sor[1][:2]) == 7]
    homersekletek13 = [int(sor[3]) for sor in telepules_adatai if int(sor[1][:2]) == 13]
    homersekletek19 = [int(sor[3]) for sor in telepules_adatai if int(sor[1][:2]) == 19]
    homersekletek = homersekletek01 + homersekletek07 + homersekletek13 + homersekletek19
    if len(homersekletek01) == 0 or len(homersekletek07) == 0 or len(homersekletek13) == 0 or len(homersekletek19) == 0:
        print(f"{telepules} Középhőmérséklet: NA; Hőmérséklet-ingadozás: {max(homersekletek) - min(homersekletek)}")
    else:
        print(f"{telepules} Középhőmérséklet: {round(sum(homersekletek) / len(homersekletek))}; Hőmérséklet-ingadozás: {max(homersekletek) - min(homersekletek)}")
    
    with open(f"{telepules}.txt", "w") as f:
        print(telepules, file=f)
        for sor in telepules_adatai:
            print(f"{sor[1][:2]}:{sor[1][2:]} {'#' * int(sor[2][3:])}", file=f)

print("6. feladat") 
print("A fájlok elkészültek.")