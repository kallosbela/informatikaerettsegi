# 1.  Olvassa be és tárolja el a melyseg.txt állomány adatait, és annak felhasználásával oldja 
# meg a következő feladatokat! 
to = []
with open('melyseg.txt', 'r') as f:
    for sor in f:
        to.append(list(map(int, sor.strip().split())))
sorok = to[0][0]
oszlopok = to[1][0] 
to = to[2:]

# 2.  Kérje be egy mérési eredmény sor- és oszlopazonosítóját, majd írassa ki az adott helyen 
# mért adatot a képernyőre! (A sorok és oszlopok számozása kezdődjön 1-gyel!) 
print('2. feladat')
sor = int(input('A mérés sorának azonosítója='))  # 12
oszlop = int(input('A mérés oszlopának azonosítója='))  # 6
print(f'A mért mélység az adott helyen {to[sor-1][oszlop-1]} dm') # 33

# 3.  Határozza meg a tó (vagyis az ábrán szürkével jelölt rész) felszínének területét, valamint 
# a tó átlagos mélységét! Írassa ki a két eredményt a mintának megfelelően a képernyőre! 
# A tó átlagos mélysége méterben kifejezve, két tizedesjegy pontossággal jelenjen meg! 
print('3. feladat')
terulet = 0
melyseg = 0
for sor in range(sorok):
    for oszlop in range(oszlopok):
        if to[sor-1][oszlop-1] != 0:
            terulet += 1
            melyseg += to[sor-1][oszlop-1]
atlag = round((melyseg/10)/terulet, 2)
print(f'A tó felszíne: {terulet} m2, átlagos mélysége: {atlag} m') # A tó felszíne: 646 m2, átlagos mélysége: 4,28 m

# 4.  Mekkora  a  tó  legnagyobb  mélysége,  és  hol  a  legmélyebb  a  tó?  Jelenítse  meg  a  választ a képernyőn!  A  legmélyebb  pont  koordinátáit  a  mintának  megfelelően  (sor;  oszlop) 
# formában  írassa  ki!  Ha  több  ilyen  mérési  eredmény  is  van,  mindegyik  koordinátapárja 
# jelenjen meg!  
alja = max([max(sor) for sor in to]) #max-nál lesz a legmélyebb!!
print('4. feladat')
print(f'A tó legnagyobb mélysége: {alja} dm')  #98dm
print('A legmélyebb helyek sor-oszlop koordinátái:')
for sor in range(sorok):
    for oszlop in range(oszlopok):
        if to[sor-1][oszlop-1] == alja:
            print(f'({sor}; {oszlop})', end='  ') # (14; 20)   (26; 11)   (32; 16)

# 5.  Milyen hosszú a tó partvonala, vagyis az ábrán a szürkével jelölt részt határoló vastag fekete 
# vonal hossza? A partvonalhoz vegye hozzá a tóban  lévő  szigetek kerületét is! Írassa ki 
# az eredményt a mintának megfelelően a képernyőre! (A megoldás során felhasználhatja, 
# hogy a táblázat első és utolsó sorában és oszlopában minden adat 0.)
print('\n5. feladat')
part = 0
for sor in range(1,sorok):
    for oszlop in range(1,oszlopok):
        if to[sor][oszlop] != 0:
            if to[sor][oszlop-1] == 0:
                part += 1   
            if to[sor-1][oszlop] == 0: 
                part += 1
        if to[sor][oszlop] == 0:
            if to[sor][oszlop-1] != 0:
                part += 1   
            if to[sor-1][oszlop] != 0: 
                part += 1
print(f'A tó partvonala {part} m hosszú') # A tó partvonala 270 m hosszú

# 6.  Kérje  be  a  felhasználótól  egy  oszlop  azonosítóját,  és  szemléltesse  a  diagram.txt 
# szöveges  állományban  „sávdiagramon”  a  tó  mélységét  az  adott  oszlopban  a  következő 
# módon!  A  sor  elején  jelenjen  meg  a  mérési  adat  sorának  azonosítója  pontosan  két 
# számjeggyel, majd tegyen egymás mellé annyi csillagot (*), ahány méter az adott helyen 
# a tó mélysége! A mérési adatokat a matematika szabályainak megfelelően kerekítse!
print('6. feladat')
oszlop = int(input('A vizsgált szelvény oszlopának azonosítója=')) # 6
with open('diagram.txt', 'w') as f:
    for sor in range(sorok):
        print(f'{str(sor+1) if sor>=9 else "0"+str(sor+1)}{"*" * round(to[sor][oszlop-1]/10)}', file=f)
