"""
Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
o produto do dobro do primeiro com metade do segundo .
a soma do triplo do primeiro com o terceiro.
o terceiro elevado ao cubo.
"""
num1 = int(input("Informe o primeiro número: "))
num2 = int(input("Informe o segundo número: "))
num3 = float(input("Informe o terceiro número: "))

a = (num1 * 2) * (num2 / 2)
b = (num1 * 3) + num3
c = num3 ** 3

print("O produto do dobro do primeiro com metade do segundo é: {0}".format(a))
print("A soma do triplo do primeiro com o terceiro é: {0}".format(b))
print("O terceiro elevado ao cubo é: {0}".format(c))