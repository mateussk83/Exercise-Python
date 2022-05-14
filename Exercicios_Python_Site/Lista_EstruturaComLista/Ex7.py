numeros = []
multiplicacao = 1
for n in range(1,6):
    num = int(input("Informe o {0}º número: ".format(n)))
    multiplicacao = multiplicacao * num
    numeros.append(num)
print("Numeros: {0}".format(numeros))
print("Soma: {0}".format(sum(numeros)))
print("Multiplicação: {0}".format(multiplicacao))
