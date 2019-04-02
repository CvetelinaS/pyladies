key = int(input ('Vyber si celé kladné číslo pro klíč:'))
text = input('Uveďte text, který chcete zašifrovat:')
p_text = list(text)
c_text = []
velka_pismena = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
mala_pismena = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

for pismenko in p_text:
    if pismenko in velka_pismena:
    index = uppercase.index(eachLetter)
			crypting = (index + key) % 26
			velka_pismen.append(crypting)
			newLetter = uppercase[crypting]
			c_text.append(newLetter)
		elif pismenko in mala_pismena:
			index = mala_pismena.index(eachLetter)
			crypting = (index + key) % 26
			c_text.append(crypting)
			newLetter = mala_pismena[crypting]
			c_text.append(newLetter)
	return c_text

code = caesar_encrypt('abc', 2)
print()
print(code)
print()
