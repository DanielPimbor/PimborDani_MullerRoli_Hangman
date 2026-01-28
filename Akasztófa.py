import random

#helytelen betűk listája
helytelen_betűk = []

#szo tippek szama
tipp_szo_szama = 3

#random szavak
szavak =["alma", "asztal", "autó", "banán", "bicikli", "ceruza", "cipő", "dió", "elefánt", "erdő", "fa", "fagyi", "hal", "ház", "iskola", "kabát", "kutya", "lámpa", "macska", "nadrág", "narancs", "olló", "póló", "szék", "szilva", "táska", "telefon", "toll", "vonat", "zebra"]



#///////////////////////////////////////////////////////////////////

#kepek

HANGMANPICS = [
'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''',
'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''',
'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''',
'''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
''',
'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''',
'''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''',
'''
  +---+
  |   |
      |
      |
      |
      |
=========
''',
'''
  +---+
      |
      |
      |
      |
      |
=========
''',
'''
      +
      |
      |
      |
      |
      |
=========
''',
'''
      '


      |
      |
      |
=========
''',
'''
      '


      
      
      
=========
'''

]
#///////////////////////////////////////////////////////////////////


megoldas = random.choice(szavak)
megoldas_rejtett = ['X' for _ in megoldas]



print('SZIAAAAAA, mielőtt játszol itt van pár szabály, ha esetleg nem ismernéd a játékot.')
print('---------------------------------------------')
print('!Szabályok!')
print('')
print('Kapsz egy szót, amit nem látsz.')
print('Tippelj betűket!')
print('A helyesen eltalált betűket befogom írni az adott szóban a helyére.')
print('A helyteleneket kiírom, nehogy elfelejtsd vagy újratippeld őket.')
print('Az akasztófa bábú fogja jelezni mennyi helytelen betűtipped lehet még.')
print('Összesen 3-szor tippelheted meg a szavat, ha ennyiből nem sikerül, veszítettél.')
print('Szavat úgy tudsz tippelni, ha a betű helyett egy 0-át írsz.')
print('')
print('FONTOS, HOGY A KÉT VAGY TÖBB BETŰ HOSSZÚSÁGÚ BETŰKET KÜLÖN VESZI!!!!!!!!!')
print('')
print('---------------------------------------------')
print('')
print('Jó szórakozást!')
print('')

while True:
    try:
        nehezseg_valasztas = int(input(
            'Milyen nehézségen akarsz játszani?\n \n'
            '1 - Könnyű (10 élet)\n'
            '2 - Közepes (7 élet)\n'
            '3 - Nehéz (5 élet)\n \n'
            'Választás:'
        ))
        print('')

        if nehezseg_valasztas == 1:
            eletek = 10
            break
        elif nehezseg_valasztas == 2:
            eletek = 7
            break
        elif nehezseg_valasztas == 3:
            eletek = 5
            break
        else:
            print("Csak 1, 2 vagy 3 lehet! \n")
    except ValueError:
        print("Számot adj meg! \n")


while True:
    while True:
        try:
            tipp_betű = input("Írj ide egy betűt (tippeléshez 0-át): ").lower()
            engedélyezett_betu = ['a','á','b','c','cs','d','dz','dzs','e','é','f','g','gy','h','i','í','j','k','l','ly','m','n','ny','o','ó','ö','ő','p','q','r','s','sz','t','ty','u','ú','ü','ű','v','w','x','y','z','zs']            
            if tipp_betű not in engedélyezett_betu and tipp_betű != '0':
                raise ValueError("Helytelen bemenet, próbáld újra!")
            # csak akkor törünk ki a try-except-ből, ha helyes a betű
            break
        except ValueError as e:
            print(e)
    
    if tipp_betű == '0':
        if eletek > 0:
                print(HANGMANPICS[int(eletek)])
        print('')
        print(megoldas_rejtett)
        print('')
        tipp_szo = input(f'Tippeld meg a szót: (Ennyi tipped van még hátra: {tipp_szo_szama})')
        tipp_szo_szama -= 1
        print('')

        if tipp_szo.lower() == megoldas:
            print('Helyesen megtippelted a szót, nyertél!')
            break

        elif tipp_szo !=  megoldas: 
            print("Nem találtad el a szót!")
            print('')
            print(f'Már csak {tipp_szo_szama} tipped van hátra.')
            print('')

    else:
        if tipp_betű in megoldas:
            print('')
            print('Helyesen eltaláltál egy betűt.')
            print('')
            if tipp_betű not in megoldas_rejtett:
                #itt alakitja at az xes megoldas helyes betuit
                for i, betu in enumerate(megoldas):
                    if betu == tipp_betű:
                        megoldas_rejtett[i] = tipp_betű
            else:
                print("Már megtippelted ezt a betűt!")
            if eletek > 0:
                print(HANGMANPICS[int(eletek)])
            print('Megoldásod eddig:')
            print(megoldas_rejtett)
            print('')
            print('Helytelen betűk eddig:')
            print(f'{helytelen_betűk} ')
            print('')
        
        elif tipp_betű not in megoldas:
            print('')
            print('Nem találtad el a betűt.')
            print('')
            if tipp_betű not in helytelen_betűk:
                helytelen_betűk.append(tipp_betű)
                
            else:
                print("Már megtippelted ezt a betűt!")
            print('')
            print('Megoldásod eddig:')
            print(megoldas_rejtett)
            print('')
            print('Helytelen betűk eddig:')
            print(helytelen_betűk)
            print('')
            eletek -= 1
            if eletek > 0:
                print(HANGMANPICS[int(eletek)])
            if eletek == 0:
                print(HANGMANPICS[int(eletek)])
                print('Meghaltál, vége a játéknak.')
                print('')
                print(f'A megoldás ez volt: {megoldas}')
                print('')
                break

    if 'X' not in megoldas_rejtett:
        print('Eltaláltad az összes betűt, nyertél!')
        break