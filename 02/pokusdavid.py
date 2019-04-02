stastna = input('Jsi šťastná?')
bohata = input('Jsi bohatá? ')

if bohata == 'ano':
    d= True
    s= False

elif stastna == 'ano':
    e= True
    w= False

elif bohata == 'ne':
    s= True
    d= False

elif stastna == 'ne':
    w= True
    e= False
else:
    print("chybka")

if e== False:
    print("To je mi líto")
elif d== True:
    print("zkus se vic usmivat")
elif e== True:
    print("mene utracej")
else:
    print("gratuluji")