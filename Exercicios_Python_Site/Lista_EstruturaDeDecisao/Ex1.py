"""
Faça um Programa que peça dois números e imprima o maior deles.
"""
num1 = int(input("Informe o primeiro número: "))
num2 = int(input("Informe o segundo número: "))
numeros = []

numeros.append(num1)
numeros.append(num2)

print("O maior numero é: {0}".format(max(numeros)))

