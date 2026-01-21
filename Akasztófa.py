import random

#helytelen betűk listája
helytelen_betűk = []

#szo tippek szama
tipp_szo_szama = 3

#random szavak
szavak = ["ablak"]

megoldas = random.choice(szavak)
megoldas_rejtett = ['X' for _ in megoldas]



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


while True:
    while True:
        try:
            tipp_betű = input("Írj ide egy betűt: ").lower()
            engedélyezett_betu = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','sz','gy','ty','zs','cs','ly']
            
            if tipp_betű not in engedélyezett_betu and tipp_betű != '0':
                raise ValueError("Helytelen betű, próbáld újra!")
            # csak akkor törünk ki a try-except-ből, ha helyes a betű
            break
        except ValueError as e:
            print(e)
    
    if tipp_betű == '0':
        tipp_szo = input(f'Tippeld meg a szót: (Ennyi tipped van még hátra: {tipp_szo_szama})')
        tipp_szo_szama -= 1

    else:
        if tipp_betű in megoldas:
            print('Helyesen eltaláltál egy betűt.')

            for i, betu in enumerate(megoldas):

                if betu == tipp_betű:
                    megoldas_rejtett[i] = betu
        
            print(megoldas_rejtett)
        
        elif tipp_betű not in megoldas:
            print('Nem találtad el a betűt.')
            helytelen_betűk.append(tipp_betű)
            

    if 'X' not in megoldas_rejtett:
        print('Nyertél!')
        break