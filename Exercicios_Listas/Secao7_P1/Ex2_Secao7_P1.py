pares = []
impares = []

for n in range(1,7):
    num = int(input("Informe o {0}º numero: ".format(n)))
    if(num % 2 == 0):
        pares.append(num)
    else:
        impares.append(num)
print("Os numeros pares digitados são:{0}".format(pares))
print("A soma dos numeros pares digitados são:{0}".format(sum(pares)))
print("Os numeros impares digitados são:{0}".format(impares))
print("A soma dos numeros impares digitados são:{0}".format(sum(impares)))
    