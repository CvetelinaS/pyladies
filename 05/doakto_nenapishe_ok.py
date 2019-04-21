def napis_cislo():
    while True:
        odpoved = input('Zadej cislo:')
        try:
            cislo = int(odpoved)
            return cislo
        except ValueError:
            print('Nebylo to cislo')

    print(napis_cislo())