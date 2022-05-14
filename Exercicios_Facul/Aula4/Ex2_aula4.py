"""
Faça um programa que peça ao usúario informar dois numeros e depois imprimir na tela do numero A até o numero B.

Ex: o usuario informou 2 e 6 o sistema deverá mostrar (2,3,4,5,6)
"""
num1 = int(input("informe um valor inicial:"))
num2 = int(input("informe um valor final:"))
for n in range(num1, num2+1):
    print(n)