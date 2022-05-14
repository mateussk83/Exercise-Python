"""
Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes.
"""
consoantes = []
vogais = []

for n in range (1, 11):
    letras = (input("Informe um caracter: ").lower())
    if letras == 'a' or letras == 'e' or letras == 'i' or letras == 'o' or letras == 'u':
        vogais.append(letras)
    else:
        consoantes.append(letras)
print("Os caracteres q são consoantes são: {0}".format(consoantes))