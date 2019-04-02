pole = 20*"-"
print (pole)
while ("xxx" not in pole) and ("ooo" not in pole) and ("-" in pole):
    pozice = int(input ("Zadej pozici (hráč 1): "))
    while pozice not in range(0, 19) and not "x" and not "o":
        print ('Zadej pozici v rozsahu 1-20 která již není obsazená znakem "x" nebo "o".')
        print (pole)
        pozice = int(input ("Zadej pozici (hráč 1): "))
        pole = pole [:pozice]+"x"+pole [pozice+1:]
    print (pole)
    pozice = int(input ("Zadej pozici (hráč 2): "))
    #pole = pole [:pozice]+"x"+pole [pozice+1:]
    while pozice not in range(0, 19):
        print ('Zadej pozici v rozsahu 1-20 která již není obsazená znakem "x" nebo "o".')
        print (pole)
        pozice = int(input ("Zadej pozici (hráč 2): "))
    #pozice = int(input ("Zadej pozici (hráč 2): "))
    pole = pole [:pozice]+"o"+pole [pozice+1:]
    print (pole)
if "xxx" in pole:
    print("Vzhrál hráč 1 (x)")
elif "ooo"in pole:
    print("Vyhrál hráč 2 (o)")
else:
    print("Remíza")
