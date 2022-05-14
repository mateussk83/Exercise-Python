alturas = []
pesos = []
codigos = []
n = 0

codigo = int(input("Informe o código: "))
while codigo != 0:
    altura = float(input("Informe a sua altura: "))
    peso = float(input("Informe a seu peso: "))
    n = n + 1
    codigos.append(codigo)
    alturas.append(altura)
    pesos.append(peso)
    codigo = int(input("Informe o código: "))

media_peso = sum(pesos) / n
media_altura = sum(alturas) / n
indice_alto = alturas.index(max(alturas))
indice_baixo = alturas.index(min(alturas))
indice_gordo = pesos.index(max(pesos))
indice_magro = pesos.index(min(pesos))

print("O cliente com codigo {0} tem o maior peso!! \n pesando: {1}".format(codigos[indice_gordo],pesos[indice_gordo]))
print("O cliente com codigo {0} tem o menor peso!! \n pesando: {1}".format(codigos[indice_magro],pesos[indice_magro]))
print("O cliente com codigo {0} tem a maior altura!! \n medindo: {1}".format(codigos[indice_alto],alturas[indice_alto]))
print("O cliente com codigo {0} tem a menor altura!! \n medindo: {1}".format(codigos[indice_baixo],alturas[indice_baixo]))
print("A media do peso dos clientes é de: {0:.2f}".format(media_peso))
print("A media da altura dos clientes é de: {0:.2f}".format(media_altura))