def rodne_cislo(x):                           #("Zadejte své rodné číslo:")
    rok = int(rodne_cislo[0:2])               #x = int(rodne_cislo)
    mesic = int(rodne_cislo[2:4])
    den = int(rodne_cislo[4:6])
    x % 11 == 0
while True:
        if len(rodne_cislo) == 11 and rodne_cislo[6] == ('/'):
            print('Zadali jste správné rodné číslo!')
            break
        print('Zadejte správný tvar svého rodného čísa!')
#Vypise, zda rodne cislo ma spravny tvar
while mesic > 50:
        mesic = mesic - 50
        if mesic > 1 and mesic <= 12:
            print("Rodné číslo má správny tvar.")
        else:
            print("Rodné číslo má nesprávny tvar.")
     #Vypise pohlavi
while True:
    if mesic > 13:
        print('Jste žena')
    if mesic < 13:
        print('Jste muž')
        print(den, '.', mesic,'.', rok, '.')
#Vypise datum narozeni
    if rok == int(2019 - (rodne_cislo[0:2])):
        print(rok)
        print('Vas datum narozeni je: ', den, '.', mesic,'.', rok, '.')

