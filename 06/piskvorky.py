#pridavam komentar pro Git
def vyhodnot(radek):
    if  'xxx' in radek:
        return ('\'x\'')
    elif 'ooo' in radek:
        return('\'o\'')
    elif '-' not in radek:
        return('\'!\'')
    else:
        return('\'-\'')

def tah(pole, cislo_policka, symbol):
    return pole[:cislo_policka] + symbol + pole[cislo_policka + 1:]
#tah hrace
def tah_hrace(pole, otazka):
    while True:
        cislo_policka=int(input(otazka))
        if cislo_policka<0:
            print ('Zadej kladne cislo!')
        elif cislo_policka>19:
            print ('Vyber si policko od 0 do 19!')
        elif '-' not in pole[:cislo_policka]:
            print('Pole je obsazeno. Hrej znovu.')
        else:
            return tah(pole,cislo_policka,'x')

#samotna hra
def piskvorky1d():
    pole='-'*20
    while '-' in pole:
        print(pole)
        pole = tah_hrace(pole, 'Vyber si policko od 0 do 19:')
        pole = tah_pocitace(pole)
        vysledek = vyhodnot(pole)
        if vysledek != '\'-\'':
            print(vysledek)
            break
    if "xxx" in pole:
        print('Vyhrala jsi')
    elif "ooo"in pole:
        print('Vyhral pocitac')
    else:
        print('Remiza')