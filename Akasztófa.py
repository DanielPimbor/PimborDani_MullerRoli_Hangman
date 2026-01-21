import random

#szo tippek szama
tipp_szo_szama = 3

#random szavak
szavak = ["ablak", "asztal", "barát", "ceruza", "cipő", "csillag", "erdő", "eső", "iskola", "játék", "kenyér", "könyv", "kutya", "szék", "telefon", "tenger", "tükör", "város", "virág", "vonat"]

megoldas = print(random.choice(szavak))

print('SZIAAAAAA, mielőtt játszol itt van pár szabály, ha esetleg nem ismernéd a játékot.')
print('---------------------------------------------')
print('!Szabályok!')
print('Kapsz egy szót, amit nem látsz.')
print('Tippelj betűket!')
print('A helyesen eltalált betűket befogom írni az adott szóban a helyére')
print('A helyteleneket kiírom, nehogy elfelejtsd vagy újratippeld őket')
print('Az akasztófa bábú fogja jelezni mennyi helytelen betűtipped lehet még')
print('Összesen 3-szor tippelheted meg a szavat, ha ennyiből nem sikerül, veszítettél.')
print('Szavat úgy tudsz tippelni, ha a betű helyett egy 0-át írsz.')
print('---------------------------------------------')
print('Jó szórakozást!')

tipp_betű = input('Írj ide egy betűt: ')
if tipp_betű == 0:
    tipp_szo = input(f'Tippeld meg a szót: (Ennyi tipped van még hátra: {tipp_szo_szama})')
    tipp_szo_szama -= 1

else:
    if tipp_betű in megoldas:
        pozicio = megoldas.index(tipp_betű)
        


