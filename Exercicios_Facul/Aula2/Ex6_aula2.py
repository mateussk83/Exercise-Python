"""
As maçãs custam R$ 0,30 cada se forem compradas menos de uma dúzia, e R$ 0,25 se forem compradas pelo menos 12. 
Escreva um programa que leia o número de maçãs compradas, calcule e escreva o custo total da compra.
"""

valor = 0
num = float(input("Informe o numero de maças: "))

if num > 11:
    valor = num * 0.25
    print("O valor a pagar pelas maças é R${0: .2f}".format(valor))
if num < 12:
    valor = num * 0.30
    print("O valor a pagar pelas maças é R${0: .2f}".format(valor))