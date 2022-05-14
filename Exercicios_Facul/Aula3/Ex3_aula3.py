"""
Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa só ira parar quando informar uma idade negativa. No final, mostre:
A media de pessoas sendo menor ou igual de 25, se a media for entre 26 e 60 pertence ao grupo Adulto e se a media de idades for maior que 60 entao fara parte do grupo idoso.
"""
idade = int(input("Informe a sua idade: "))
idades = [idade]
geral = 0
while idade >= 0:
    idade = float(input("Informe sua idade (para sair informe sua idade negativa): "))
    idades.append(idade)
    geral = geral + idade
media = geral / len(idades)
if media >= 0 and media <= 25:
        print("A media de pessoas pertencem ao grupo Jovem!!")
if media >= 26 and media <= 60:
        print("A media de pessoas pertencem ao grupo Adulto!!")
if media >= 60:
        print("A media de pessoas pertencem ao grupo idoso!!")