rodnecislo = input('zadej rodne cislo i s lomitkem:')
cislo = (rodnecislo[0:6]) + (rodnecislo[7:11])
delenec = int(cislo)
delitel = 11

def pohlavi(rodnecislo):
    'Vyhodnoti pohlavi ze zadaneho rodneho cisla'
    if (rodnecislo[2] > '1'):
        pohlavi = 'zena'
    else:
        pohlavi = 'muz'
    return pohlavi

def format(rodnecislo):
    'Vyhodnoti format zadaneho rodneho cisla, ma-li 11 znaku, 7. znak lomitko a delitelne 11'
    if (len(rodnecislo) == 11) and (rodnecislo[6] == '/') and (delenec % delitel == 0):
        return True
    else:
        return False

def datumnarozeni(rodnecislo):
    'Vypise z rodneho cisla den, mesic a rok'
    den = rodnecislo [4:6]
    rok = rodnecislo[0:2]
    mesic_muzi = rodnecislo[2:4]
    if mesic_muzi[0] == '5':
        mesic = '0' + mesic_muzi[1]
    elif mesic_muzi[0] == '6':
        mesic = '1' + mesic_muzi[1]
    else:
        mesic = mesic_muzi
    return den, mesic, rok


#vyhodnoceni formatu rodneho cisla
if format(rodnecislo) == True:
    print('Zadane rodne cislo ma spravny format')
else: 
    print('Zadane rodne cislo je nespravne')

#vyhodnoceni pohlavi
gender = pohlavi(rodnecislo)
print('Pohlavi: {}'.format(gender))

#ukaze cele datum narozeni
datum = datumnarozeni(rodnecislo)
print('Datum narozeni: {} {} 19{}'.format(*datum))
