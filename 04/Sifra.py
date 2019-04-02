p_text = input('Zadejte text, který chcete zašifrovat:')
c_text = ''
key = int(input('Zadejtě klíč ve tvaru čísla:'))

# hlavní cyklus
for pismenko in p_text:
    nove_pismenko = pismenko
    if 'a' <= pismenko <= 'z':
        nove_pismenko = chr((ord(pismenko) - 97 + key)%26 + 97 )
        c_text = c_text + nove_pismenko
    print(c_text)