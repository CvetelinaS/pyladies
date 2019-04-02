zaznamy = ['pepa novák', 'Jiří Sládek', 'Ivo navrátil', 'Jan poledník']

spravny_zaznam = []
spatne = []

for zaznam in zaznamy:
    jmeno, prijmeni = zaznam.split()
    if not jmeno[0].islower() and not prijmeni[0].islower():
        spravny_zaznam.append(zaznamy)

print(spravny_zaznam)

for zaznam in zaznamy:
    jmeno, prijmeni = zaznam.split()
    if jmeno[0].islower() or prijmeni[0].islower():
        spravny_zaznam.append(zaznamy)

print(spatne)

#for zaznam in zaznamy:
#jmeno, prijmeni = zaznam.split()
#if not jmeno[0].islower() or prijmeni[0].islower():
#spravny_zaznam.append(zaznamy)
#else:
    #spatne.append(zaznam)