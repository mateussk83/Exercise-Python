"""
Faça um vetor que leia 10 numeros e imprima na tela o maior.
"""
numeros = []

for n in range(1, 11):
    num = int(input("Informe um numero: "))
    numeros.append(num)
maior_numero = max(numeros)
print("O maior numero é : {0}".format(maior_numero))