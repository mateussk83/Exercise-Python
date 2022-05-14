"""
aça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e os números.
"""
numeros = []
soma = 0
multiplicacao = 1
for n in range(1 , 6):
    num1 = int(input("informe um numero"))
    soma = soma + num1
    multiplicacao = multiplicacao * num1
    numeros.append(num1)
print(numeros)
print(" A soma dos números é {0}".format(soma))
print(" A multiplicação dos números é {0}".format(multiplicacao))