qtd_temperaturas = int(input("Informe a quantidade de temperaturas que seráo avaliadas: "))
temperaturas = []
h = 0
for n in range(1, qtd_temperaturas + 1):
    temperatura = float(input("Informe a {0}ª temperatura: ".format(n)))
    temperaturas.append(temperatura)
    h = h + 1
print("A maior temperatura informada foi: {0}".format(max(temperaturas)))
print("A menor temperatura informada foi: {0}".format(min(temperaturas)))
print("A media de temperaturas informada foi: {0:.2f}".format(sum(temperaturas) / n ))

