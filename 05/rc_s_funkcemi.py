def format(rodne_cislo):                           #("Zadejte své rodné číslo:")
    rok = int(rodne_cislo[0:2])               #x = int(rodne_cislo)
    mesic = int(rodne_cislo[2:4])            # {"rodne_cislo":["rok", "mesic", "den"]} или rodne_cislo = {"den":[0:2], "mesic":[2:4], "den":[4:6]]}
    den = int(rodne_cislo[4:6])                  #Може ли така като речник?
    if len(rodne_cislo) != 11:
        return False
        print('Zadejte správný tvar svého rodného čísa!')
    elif rodne_cislo[6] != ('/'):
        return False
        print('Zadejte správný tvar svého rodného čísa!')
    rc = ''.join(rodne_cislo.split('/'))
    for n in range(0,9):
        if ord(rc[n]) in range(48,58):
            return True
        else:
            return False
    try:
        rc = int (''.join(rodne_cislo.split('/')))
    except ValueError:
        return False
    else:
        if rc % 11 == 0:
            return True
        else:
            return False

# je delitelne 11?
def delitelnost(rodne_cislo):
    rc = int(''.join(rodne_cislo.split('/')))
    if rc % 11 == 0:
        return True
    else:
        return False

#Vypise pohlavi
def pohlavi(rodne_cislo):
    rok = int(rodne_cislo[0:2])               
    mesic = int(rodne_cislo[2:4])          
    den = int(rodne_cislo[4:6])
    while mesic > 50:
            mesic = mesic - 50
            if mesic > 1 and mesic <= 12:
                print("Rodné číslo má správny tvar.")
            else:
                print("Rodné číslo má nesprávny tvar.")
    while True:
        if mesic > 13:
            print('Jste žena')
        if mesic < 13:
            print('Jste muž')
            print(den, '.', mesic,'.', rok, '.')
            break

#Vypise datum narozeni
def datum_narozeni(rodne_cislo):
    rok = rodne_cislo[:2]
    den = rodne_cislo[4:6]
    kod_mesic = rodne_cislo[2:4]
    if kod_mesic[0] == '5':
        mesic = '0' + kod_mesic[1]
    elif kod_mesic[0] == '6':
        mesic = '1' + kod_mesic[1]
    else:
        mesic = kod_mesic
    return den, mesic, rok

rodne_cislo = input('Napis rodne cislo: ')
while format(rodne_cislo) == False or delitelnost(rodne_cislo) == False:
    print('Rodne cislo ma spatny format.')
    rodne_cislo = input('Napis rodne cislo: ')

print('{} je skutecne rodne cislo.'.format(rodne_cislo))  

data = datum_narozeni(rodne_cislo)
gender = pohlavi(rodne_cislo)
print('Datum narozeni: {} {} 19{}'.format(*data))
print('Pohlavi: {}'.format(gender))


