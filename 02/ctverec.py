#tento program pocita obvod a osah ctverce

a = float(input ('Zadej cislo'))
cislo_je_spravne = a > 0

if cislo_je_spravne:
        O = 4*a
        S = a*a
        print (O, "cm")
        print (S, "cm")
else:
    print('Zadej kladne cislo.')

# print ('Ovod ctverce se stranou', a, 'je', a*4, 'cm')
