numero = int(input("Informe o número: "))

lista = list(str(numero))

lista.reverse()
numero_invertido = ''.join(lista)

print("=> {0}".format(numero_invertido))