#Entradas
quantidade_minima = int(input("Informe a quantidade minima: "))
quantidade_maxima = int(input("Informe a quantidade maxima: ")) 

#processamentos
estoque_medio = (quantidade_minima + quantidade_maxima) / 2

#saidas
print("A media do estoque é {0}".format(estoque_medio))
