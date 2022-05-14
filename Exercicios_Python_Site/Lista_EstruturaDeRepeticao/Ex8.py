numeros = []

for n in range(1,6):
    num = int(input("Informe o {0}º número: ".format(n)))
    numeros.append(num)
print("A soma dos números é: {0} ".format(sum(numeros)))
print("A média dos números é: {0} ".format(sum(numeros) / 5))
