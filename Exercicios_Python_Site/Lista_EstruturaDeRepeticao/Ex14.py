pares = []
impares = []

for n in range(1,11):
    num = int(input("Informe o {0}º numero: ".format(n)))
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)
print("Os numeros impares são: {0}".format(len(impares)))
print("Os numeros pares são: {0}".format(len(pares)))