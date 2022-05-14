produto = int(input("Informe a quantidade de produtos: "))
valores = []

for n in range(1, produto + 1):
    valor = int(input("Informe o valor do {0}º produto: ".format(n)))
    if valor == 0:
        break
    else:
        valores.append(valor)
if valor != 0:
    dinheiro = int(input("Informe o valor em dinheiro que o cliente forneceu: "))
    troco = dinheiro - sum(valores)
    print("Lojas Tabajara")
    for i in range(0, produto):
        print("Produto {0}: R$ {1:.2f}".format(i + 1, valores[i]))
    print("Total: R$ {0:.2f} \nDinheiro: R$ {1:.2f} \nTroco:R${2:.2f}".format(sum(valores),dinheiro,troco))
