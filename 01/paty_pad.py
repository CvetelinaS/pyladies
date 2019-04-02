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
