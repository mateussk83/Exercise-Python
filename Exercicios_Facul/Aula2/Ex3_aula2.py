"""
Faça um algoritmo que peça o número ao usuário e realize a raiz 
deste número caso numero for negativo imprima na tela "número invalido".
"""

num1 = int(input("Informe um numero: "))

if num1 > 0:
    raiz = num1 ** (1/2)
    print("A raiz do numero {0} é {1}".format(num1, raiz))
if num1 < 0:
    print("Numero invalido:")