frase = input("Informe a frase: ")
fraseInversa = ""
caracter = " "
for n in range(len(caracter)):
    frase = frase.replace(caracter[n],"")
fraseInversa = frase[::-1]

if fraseInversa == frase:
    print('A frase é um palíndromo!!'.format(frase))
else: 
    print('A frase não é um palíndromo!!'.format(frase)) 