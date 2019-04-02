tah_pocitace = ('kámen', 'nůžky', 'papír')
tah_cloveka = input('Kámen, nůžky nebo papír? ')

if tah_cloveka == 'kámen':
    
    print ('Plichta.') 
elif tah_cloveka == 'papír':
    
    print ('Vyhrála.')
elif tah_cloveka == 'nůžky':
    
    print ('Počítač vyhrál.')
else:
    print('Nerozumím!')