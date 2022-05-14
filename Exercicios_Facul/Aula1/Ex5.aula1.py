"""
Faça um Programa que peça o nome do aluno e as 3 notas bimestrais e mostre a média.
"""

nome = input("informe o seu nome:")
prova1 = float(input("Informe o valor da primeira prova:"))
prova2 = float(input("Informe o valor da segunda prova:"))
prova3 = float(input("Informe o valor da terceira prova:"))

media = (prova1 + prova2 + prova3) / 3

print("Nome: {0}".format(nome))
print("Media: {0}".format(media))