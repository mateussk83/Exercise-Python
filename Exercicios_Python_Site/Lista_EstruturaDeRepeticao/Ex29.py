
produto = 1.99
print("Lojas quase Dois - Tabela de preços")
for n in range(1,51):
    print("{0} - R${1:.2f}".format(n, produto * n))
