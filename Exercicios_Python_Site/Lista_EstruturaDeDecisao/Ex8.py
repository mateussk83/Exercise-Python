"""
Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.
"""
valores = []
nomes = []

produto1 = input("Nome do primeiro produto: ")
valorProduto1 = float(input("Informe o Valor do primeiro produto: "))
produto2 = input("Nome do segundo produto: ")
valorProduto2 = float(input("Informe o Valor do segundo produto: "))
produto3 = input("Nome do terceiro produto: ")
valorProduto3 = float(input("Informe o Valor do terceiro produto: "))

valores.append(valorProduto1)
valores.append(valorProduto2)
valores.append(valorProduto3)
nomes.append(produto1)
nomes.append(produto2)
nomes.append(produto3)

max = max(valores)
index = valores.index(max)

print("O melhor produto é: {0}".format(nomes[index]))
