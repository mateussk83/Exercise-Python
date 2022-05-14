notas = []
for n in range(1,5):
    nota = float(input("Informe a {0}ª nota: ".format(n)))
    notas.append(nota)

for n in range(0,4):
    print("{0}ª nota: {1}".format(n,notas[n]))

media = sum(notas) / len(notas)

print("A média das notas é: {0:.2f}".format(media))