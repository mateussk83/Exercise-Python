"""
crie um algoritmo que leia um numero e mostre se o numero é par ou impar.
"""
#Entradas
n = int(input("Informe um numero: "))

#Processamentos
if n % 2 == 0:
    print("Numero {0} é par".format(n))
else:
    print("Numero {0} é impar".format(n))
