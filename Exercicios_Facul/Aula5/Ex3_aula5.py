pares = []
impares = []

for n in range(1, 11):
    num = int(input("Informe um numero: "))
    if num % 2 == 0:
        pares.append(num)
    elif num % 2 != 0:
        impares.append(num)
print("Os pares são: {0}".format(pares))
print("Os impares são: {0}".format(impares))