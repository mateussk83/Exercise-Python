"""
Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
Para homens: (72.7*h) - 58
Para mulheres: (62.1*h) - 44.7
"""
sexo = input("Informe seu sexo(com 'f' ou 'm'): ")
altura = float(input("Informe a sua altura: "))

if sexo.lower() == "f":
    peso_ideal = (62.1 * altura) - 44.7
elif sexo.lower() == "m":
    peso_ideal = (72.7 * altura) - 58

print("O seu peso ideal é: {0}".format(peso_ideal))


