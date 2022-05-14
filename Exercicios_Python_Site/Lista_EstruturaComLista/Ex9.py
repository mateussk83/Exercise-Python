A = []

for n in range(1,11):
    num = int(input("Informe o {0}º número: ".format(n)))
    num = num ** 2
    A.append(num)
print("A soma do quadrado de cada número digitado: {0}".format(sum(A)))
