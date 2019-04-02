tah_pocitace = 'kámen'
tah_cloveka = input('kámen, nůžky, nebo papír? ')

if tah_cloveka == tah_pocitace:
    print("plichta")
elif tah_cloveka =='kámen' and tah_pocitace == 'nůžky' or tah_cloveka == 'nůžky' and tah_pocitace == 'papír' or tah_cloveka == 'papír' and tah_pocitace == 'kámen':
    print("vyhrala jsi")
elif tah_cloveka =='kámen' and tah_pocitace == 'papír' or tah_cloveka == 'nůžky' and tah_pocitace == 'kámen' or tah_cloveka == 'papír' and tah_pocitace == 'nůžky':
    print("prohrala jsi")
else:
    print("neco mezi nebem a zemi")
