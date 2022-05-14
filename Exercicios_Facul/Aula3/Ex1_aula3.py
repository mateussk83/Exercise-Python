"""
Faça um programa que leia uma quantidade
indeterminada de números positivos e conte quantos
deles estão nos seguintes intervalos:
[0-25], [26-50], [51-75] e [76-100].
A entrada de dados deverá terminar quando for lido um
número negativo.
"""
num = int(input("Informe um numero: "))
grupo1 = 0
grupo2 = 0
grupo3 = 0
grupo4 = 0
while num >= 0:
    num = int(input("Informe um numero para sair informe um numero negativo: "))
    if num >= 0 and num <= 25:
        grupo1 = grupo1 + 1
    if num >= 26 and num <= 50:
        grupo2 = grupo2 + 1
    if num >= 51 and num <= 75:
        grupo3 = grupo3 + 1
    if num >= 76 and num <= 100:
        grupo4 = grupo4 + 1
print("Quantidade de numeros entre 0 e 25: {0}".format(grupo1))
print("Quantidade de numeros entre 26 e 50: {0}".format(grupo2))
print("Quantidade de numeros entre 51 e 75: {0}".format(grupo3))
print("Quantidade de numeros entre 76 e 100: {0}".format(grupo4))