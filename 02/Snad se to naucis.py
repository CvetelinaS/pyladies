
def paty_pad(jmeno):
    if jmeno == 'Hubert':
        return 'Huberte'
    elif jmeno[-1] =='a':
        return jmeno [:-1] + 'o'
    else:
        return jmeno

print(paty_pad('Hubert'))
print(paty_pad('Sona'))
print(paty_pad('Tereza'))
print(paty_pad('Xavier'))
def pozdrav(jmeno):
  print('Vitam te, ' + paty_pad(jmeno))
  if jmeno == 'Cveti':
      print ('Snad se to naucis!')

pozdrav('ANA')
pozdrav('Cveti')
