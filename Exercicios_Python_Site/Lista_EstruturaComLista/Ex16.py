"""
Utilize uma lista para resolver o problema a seguir. Uma empresa paga seus vendedores com base em comissões.
O vendedor recebe $200 por semana mais 9 por cento de suas vendas brutas daquela semana. 
Por exemplo, um vendedor que teve vendas brutas de $3000 em uma semana recebe $200 mais 9 por cento de $3000,
ou seja, um total de $470. Escreva um programa (usando um array de contadores) que determine quantos
vendedores receberam salários nos seguintes intervalos de valores:
a - $200 - $299
b - $300 - $399
c - $400 - $499
d - $500 - $599
e - $600 - $699
f - $700 - $799
g - $800 - $899
h - $900 - $999
i - $1000 em diante
"""
salario_base = 200

salarios = []
salario = 1
cont = 0
x = 0
a = 0
b = 0
c = 0
d = 0
e = 0
f = 0
g = 0
h = 0
i = 0

while salario != 0:
    x = x + 1
    comissao = float(input("Informe a {0}º comissão: ".format(x)))
    comissao = (comissao * 0.09)
    if comissao == 0:
        break
    salario = comissao + salario_base
    salarios.append(salario)
for salario in salarios:
    if salario >= 200 and salario <= 299:
        a = a + 1
    if salario >= 300 and salario <= 399:
        b = b + 1
    if salario >= 400 and salario <= 499:
        c = c + 1
    if salario >= 500 and salario <= 599:
        d = d + 1
    if salario >= 600 and salario <= 699:
        e = e + 1
    if salario >= 700 and salario <= 799:
        f = f + 1
    if salario >= 800 and salario <= 899:
        g = g + 1
    if salario >= 900 and salario <= 999:
        h = h + 1
    if salario > 999:
        i = i + 1
print("O número de funcionarios que recebem entre R$200,00 e R$299,00 é: {0}".format(a))
print("O número de funcionarios que recebem entre R$300,00 e R$399,00 é: {0}".format(b))
print("O número de funcionarios que recebem entre R$400,00 e R$499,00 é: {0}".format(c))
print("O número de funcionarios que recebem entre R$500,00 e R$599,00 é: {0}".format(d))
print("O número de funcionarios que recebem entre R$600,00 e R$699,00 é: {0}".format(e))
print("O número de funcionarios que recebem entre R$700,00 e R$799,00 é: {0}".format(f))
print("O número de funcionarios que recebem entre R$800,00 e R$899,00 é: {0}".format(g))
print("O número de funcionarios que recebem entre R$900,00 e R$999,00 é: {0}".format(h))
print("O número de funcionarios que recebem mais de R$1000,00 é: {0}".format(i))    
    