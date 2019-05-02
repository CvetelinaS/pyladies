from math import pi
def obsah_elipsy(a, b):
    return pi*a*b
 print(obsah_elipsy(3, 5))

def objem_valce(a, b, vyska):
    return obsah_elipsy(a, b) * vyska

print(objem_elipsy(3, 5, 3))
