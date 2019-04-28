#pro git
import random

def sibenice():
  
  # Nastavime policko pro slovo, ktere musime uhodnout 
  # mame 10 pokusu
  pomlcky = "-" * len(tajne_slovo)
  zivoty = 10
  
  # Dokud slovo neni uhodnoto a mame prazdna policka:
  while zivoty > -1 and not pomlcky == tajne_slovo:
    
    # Kolik pismenek(pomlcek) musime uhodnout
    print(pomlcky)
    print (str(zivoty))
    
    # Zeptej se ktere pismenko si vybereme
    pokus = input("Vyber pismenko:")
    
    # Pokud bude zadano neco jineho nez jedno pismenko
    if len(pokus) != 1:
      print ("Musis vybrat presne jedno pismenko!")
      
    # pokud uhodneme pismenko, zmizi pomlcka
    elif pokus in tajne_slovo:
      print ("Vybrane pismenko je v tajnem slovu!")
      pomlcky = update_pomlcky(tajne_slovo, pomlcky, pokus)
      
    # pokud neuhodneme pismenko, snizi se pocet pokusu
    else:
      print ("Vybrane pismenko neni v tajnem slovu!")
      zivoty -= 1
    
  if zivoty < 0:
    print ("Prohrala jsi. Slovo je: " + str(tajne_slovo))
  
  # pokud zmizi pomlcky a uhodneme vsechna pismenka, vyhrajeme
  else:
    print ("Gratuluju! Vyhrala jsi! Slovo je: " + str(tajne_slovo))
    
# meni se pocet a misto pomlcek
def update_pomlcky(secret, soucasne_pomlcky, opak_pokus):
  vysledek = ""
  
  for i in range(len(secret)):
    if secret[i] == opak_pokus:
      vysledek = vysledek + opak_pokus    #pomlcka se meni na pismenko, pokud je uhodnuto
      
    else:
      # pokud neuhodneme pismenko
      vysledek = vysledek + soucasne_pomlcky[i]
      
  return vysledek
    
slovo = ["bila", "zelena", "cervena"]

tajne_slovo = random.choice(slovo)
sibenice()
