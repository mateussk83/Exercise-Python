alturas = []
pesos = []
maior = -999
menor = 999
menor_peso = 999
maior_peso = -999
codigo_magro = 0
codigo_gordo = 0
codigo_maior = 0
codigo_menor = 0
peso_cliente = float(input("Informe seu peso: "))
altura_cliente = float(input("Informe sua altura: "))
cod = int(input("Informe o codigo do cliente: "))
while cod != 0:
    if peso_cliente < menor_peso:
        menor_peso = peso_cliente
        codigo_magro = cod
    if peso_cliente > maior_peso:
        maior_peso = peso_cliente
        codigo_gordo = cod
    if altura_cliente < menor:
        menor = altura_cliente
        codigo_menor = cod
    if altura_cliente > maior:
        maior = altura_cliente
        codigo_maior = cod
    alturas.append(altura_cliente)
    pesos.append(peso_cliente)
    peso_cliente = float(input("Informe seu peso: "))
    altura_cliente = float(input("Informe sua altura: "))
    cod = int(input("Informe o codigo do cliente(Informe 0 para Sair!!!): "))
media_altura = sum(alturas) / len(alturas)
media_peso = sum(pesos) / len(pesos)

print("O maior é: {0}".format(maior))
print("O codigo do maior é: {0}".format(codigo_maior))
print("O menor é: {0}".format(menor))
print("O codigo do menor é: {0}".format(codigo_menor))
print("O menor peso é: {0}".format(menor_peso))
print("O codigo da pessoa com menor peso é: {0}".format(codigo_magro))
print("O maior peso é: {0}".format(maior_peso))
print("O codigo da pessoa com maior peso é: {0}".format(codigo_gordo))
print("A media das alturas: {0}".format(media_altura))
print("A media dos pesos: {0}".format(media_peso))