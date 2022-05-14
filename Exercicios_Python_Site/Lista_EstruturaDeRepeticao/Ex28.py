gastos = []
x = 0
cd = int(input("Informe a quantidade de CDS em sua coleção: "))
for n in range(1, cd + 1):
    gasto = float(input("Informe o valor do {0}º cd: ".format(n)))
    gastos.append(gasto)
    x = x + 1

medio = sum(gastos) / x

print("O valor total investido é de: R${0:.2f}".format(sum(gastos)))
print("O valor médio gasto em cada cd é de: R${0:.2f}".format(medio))
