#rodne_cislo = input('Zadejte své rodné číslo:')
#r_cislo = list(rodne_cislo)
#r_cislo.pop(6)
rodne_cislo = input("Zadejte své rodné číslo:")
x = int(rodne_cislo)

#Vypise datum
rok = int(rodne_cislo[0:2])
mesic = int(rodne_cislo[2:4])
den = int(rodne_cislo[4:6])


if mesic > 50:
    mesic = mesic - 50
    print(den, '.', mesic,'.', rok, '.')






