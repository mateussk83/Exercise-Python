numeros = []

for n in range(1,11):
    num = int(input("Informe o {0}º número: ".format(n)))
    numeros.append(str(num))
numeros.reverse()

print("A ordem inversa dos números foi: {0}".format(numeros))