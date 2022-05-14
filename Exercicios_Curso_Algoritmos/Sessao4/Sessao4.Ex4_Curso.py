"""
Construa um algoritmo que leia 10 valores inteiros e positivos e:
a) encontre o menor valor
b) encontre o maior valor
c) calcule a media dos números lidos
"""
#variaveis
maior = -999
menor = 999
soma = 0
#entradas
#processamentos
for n in range(1,11):
    n = int(input("Informe um numero:"))
    if n > maior:
        maior = n
    if n < menor:
        menor = n
    soma = soma + n
media = soma / 10
print("Maior numero é {0}".format(maior))
print("O Menor numero é {0}".format(menor))
print("A media dos numero é {0}".format(media))
