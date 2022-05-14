alturas = []
idades = []

for n in range(1,6):
    idade = int(input("Informe a {0}ª idade: ".format(n)))
    altura = int(input("Informe a {0}ª altura: ".format(n)))
    idades.append(idade)
    alturas.append(altura)
alturas.reverse()
idades.reverse()
print("A altura invertida é: {0}".format(alturas))
print("A idade invertida é: {0}".format(idades))
