import util

from random import randrange

def tah_pocitace(pole):
    while True:
        cislo_policka=randrange(19)
        if '-' in pole[:cislo_policka]:
            return tah(pole,cislo_policka,'o')