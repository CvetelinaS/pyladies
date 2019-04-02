print("kamen nuzky...")
tah_pocitace = 1
if tah_pocitace== 1:
    kamen= True
    nuzky= False
    papir= False
elif tah_pocitace== 2:
    kamen= False
    papir= False
    nuzky= True
elif tah_pocitace== 3:
    kamen= False
    nuzky= False
    papir= True
else:
    print("chyba v matrixu")
tah_cloveka = input('kámen, nůžky, nebo papír? ')
if tah_cloveka == 'kámen' and tah_pocitace== 1 or tah_cloveka== "nůžky" and tah_pocitace== 2 or tah_cloveka== "papír" and tah_pocitace== 3:
    plichta= True
    vyhra= False
    prohra= False
elif tah_cloveka == 'nůžky' and tah_pocitace== 1 or tah_cloveka == 'papír' and tah_pocitace== 2 or tah_cloveka == 'kámen' and tah_pocitace== 3 or tah_pocitace == 1 and tah_cloveka== "papír" or tah_pocitace == 2 and tah_cloveka== "kámen" or tah_pocitace == 3 and tah_cloveka== "kámen":
    vyhra= False
    plichta= False
    prohra= True
elif tah_cloveka == 'papír' and tah_pocitace== 1 or tah_cloveka == 'nůžky' and tah_pocitace== 3 or tah_cloveka == 'kámen' and tah_pocitace== 2 or tah_pocitace == 1 and tah_cloveka== "nůžky" or tah_pocitace == 2 and tah_cloveka== "papír" or tah_pocitace == 3 and tah_cloveka== "nůžky":
    vyhra= True
    prohra= False
    plichta= False
else:
    print ("napiš jednu z možností")
if plichta:
    print("plichta")
elif prohra:
    print("prohrala jsi")
elif vyhra:
    print("vyhrala jsi")
else:
    print("neco mezi nebem a zemi")
