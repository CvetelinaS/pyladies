
def pole(pomlcka):
    return 20 * (pomlcka)
print(pole("-"))

def tah(pole, cislo_policka, symbol):
    #Vrati 'x' nebo 'o' podle uzivatele
    while True:
        cislo_policka = input(symbol)
        if cislo_policka == 'x':
            return True
        if cislo_policka == 'o':
            return True
        else:
            print("Mela by sis vybrat cislo policka a zadat 'x' nebo 'o'.")

def tah_hrace(pole, pozice):
    while ("xxx" not in pole) and ("ooo" not in pole) and ("-" in pole):
        pozice = int(input ("Zadej pozici (hráč 1): "))
    while pozice not in range(0, 19) and not "x" and not "o":
        print ('Zadej pozici v rozsahu 1-20 která již není obsazená znakem "x" nebo "o".')
        print (pole)
        pozice = int(input ("Zadej pozici (hráč 1): "))
        pole = pole [:pozice]+"x"+pole [pozice+1:]
    print (pole)
    pozice = int(input ("Zadej pozici (hráč 2): "))

 #   cislo_policka in range(0.19)
  #  symbol = 'x' or 'o'
#if pole[cislo_policka] == symbol:
#return True
import random  # (příp. import jiných věci, které budou potřeba)

def tah(pole, cislo_policka, symbol):
    """Vrátí pole s daným symbolem umístěným na danou pozici"""
    ...

def tah_hrace(pole):
    """Zeptá se hráče kam chce hrát a vrátí pole se zaznamenaným tahem"""
    ...
    input('Kam chceš hrát? ')
    ...

def piskvorky1d():
    """Spustí hru

    Vytvoří hrací pole a střídavě volá tah_hrace a tah_pocitace
    dokud někdo nevyhraje"""
    while ...:
        ...
        tah_hrace(...)
        ...

# Puštění hry!
piskvorky1d()
