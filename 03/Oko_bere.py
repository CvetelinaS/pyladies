#pocitac
import random
from random import randrange
tah_pocitace = random.randint(13, 25)
tah_cloveka = random.randint(1, 11)
pocet_bodu = 0
karta_cloveka = random.randint(1,11)
#tah počítače
print ('Počítač má', tah_pocitace, 'bodů.')
#vybírám kartu
#pokud je počet bodů menší než 21
while pocet_bodu < 21:
    pocet_bodu = pocet_bodu + karta_cloveka
    print('Máš kartu číslo', karta_cloveka, 'a', pocet_bodu, 'bodů')
    odpoved = input('Chces dalsi kartu nebo ne?')
if odpoved == 'ano':
    karta2 = random.randint(1, 11)
    print('Teď máš', pocet_bodu + karta2)
#pokud se počet bodů rovná 21
elif pocet_bodu == 21:
    print('Vyhrála jsi!')
#pokud se počet bodů vyšší než 21
elif pocet_bodu >= 21:
    print('Prohrála jsi!')
elif odpoved == 'ne':
    print('Konec hry.') 