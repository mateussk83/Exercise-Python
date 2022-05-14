"""
Faça um algoritmo que determina o maior entre N numeros. A condição de parada é a entrada do valor 0, 
Ou seja  
"""
#variaveis
maior = 0

#Entradas
numero = int(input("Informe um numero:"))

#processamentos
while numero != 0:
    if numero > maior:
        maior = numero
    numero = int(input("Informe um numero:"))
print("o maior numero é {0}".format(maior))