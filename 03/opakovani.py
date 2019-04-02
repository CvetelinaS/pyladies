def paty_pad(jmeno):
    if jmeno == 'Hubert':
        return 'Huberte'
    elif jmeno[-1] =='a':
        return jmeno [:-1] + 'o'
    else:
        return jmeno
def pozdrav(jmeno):
    print('Vitam te, ' + paty_pad(jmeno))
    if jmeno == 'Cveti':
        print ('Snad se to naucis!')

jmena = ['Petra','Hanka', 'Marketa' ]
for jmeno in jmena:
    pozdrav(jmeno)
    print('dalsi jmeno...')

for n in range(5):
    pozdrav('xavier')
    print(n)
