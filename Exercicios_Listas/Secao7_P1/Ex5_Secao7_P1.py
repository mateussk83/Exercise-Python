numeros = []

for n in range(1,11):
    num = int(input("Informe o {0}º numero: ".format(n)))
    numeros.append(num)
numeros.sort()
print("Os numeros em forma decrescente são: {0}".format(numeros))