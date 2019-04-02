
rodne_cislo = input("Zadejte své rodné číslo:")
x = int(rodne_cislo)

#je cislo delitelne 11-ti?
pocet= x % 11 == 0
print(pocet)

#Vypise, jestli je rodne cislo zadane spravne
mesic = int(rodne_cislo[2:4])

if mesic > 50:
    mesic = mesic - 50

if mesic > 1 and mesic <= 12 and len(rodne_cislo) == 10 and pocet:
    print("Rodné číslo má správny tvar.")
else:
    print("Rodné číslo má nesprávny tvar.")

#Vypise datum narozeni
    if rok == int(2019 - (rodne_cislo[0:2]):
        print(rok)
        mesic = int(rodne_cislo[2:4])
den = int(rodne_cislo[4:6])
print(den, '.', mesic,'.', rok, '.')

