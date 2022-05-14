numeros = []

for n in range(1,6):
    num = int(input("Informe o {0}º número: ".format(n)))
    numeros.append(num)
print("O maior número é: {0} ".format(max(numeros)))
