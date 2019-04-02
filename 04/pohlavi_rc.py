rodne_cislo = input("Zadejte své rodné číslo:")
x = int(rodne_cislo)

#Vypise datum narozeni
rok = int(rodne_cislo[0:2])
mesic = int(rodne_cislo[2:4])
den = int(rodne_cislo[4:6])


if mesic > 13:
    print('Jste žena')
if mesic < 13:
    print('Jste muž')
    print(den, '.', mesic,'.', rok, '.')