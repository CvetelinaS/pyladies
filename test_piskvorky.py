import piskvorky
import util
import ai

def test_tah():
    pole = "-"*20
    assert len(pole) == 20
    assert pole.count('x') == 1
    assert pole.count('-') == 19
#tah hrace

def tah_hrace(pole):
    while True:
        try:
            cislo_policka = int(input('Vyber si policko od 0 do 19!'))
        except ValueError:
            print('To není číslo!')
        else:
            if pozice < 0 or cislo_policka >= len(pole):
                print('Pole je obsazeno. Hrej znovu.')
            elif pole[cislo_policka] != '-':
                print('Tam není volno!')
            else:
                break

    pole = pole[:cislo_policka] + symbol + pole[cislo_policka + 1:]
    return pole
