stastna = input('Jsi šťastná?')
bohata = input('Jsi bohatá? ')

if bohata == 'ano':
    if stastna == 'ano':
    # Je bohatá a zároveň štǎstná, ta se má.
        print('Gratuluji!')
if stastna == 'ne':
    if bohata == 'ano':
    # Tady musí být jen šťastná
                print('Zkus se víc usmívat.')
if bohata == 'ne':
    if stastna == 'ano':
    # Je bohatá, ale není „bohatá a zároveň šťastná“,
    # takže musí být jen bohatá..
                print('Zkus míň utrácet.')
if bohata == 'ne':
    if stastna == 'ne':
    # A tady víme, že není ani šťastná, ani bohatá.
                print('To je mi líto.')
    