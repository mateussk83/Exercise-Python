"""
Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.
"""

valor_hora = float(input("Informe quanto ganha por hora: "))
numero_hora = int(input("Informe o numero de horas trabalhas: "))

salario = valor_hora * numero_hora

print("O salario ganha por mês é: {0}".format(salario))