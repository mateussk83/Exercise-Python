A = int(input("Informe o primeiro número: "))
B = int(input("Informe o segundo número: "))
numeros = []
for n in range(A + 1,B):
    print(n)
    numeros.append(n)
print("A soma dos números é: {0}".format(sum(numeros)))
    