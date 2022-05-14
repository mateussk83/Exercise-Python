nome = input("Informe o Nome do atleta: ")
saltos = []
while nome != None:
    for n in range(1, 8):
        print("{0}º".format(n))
        salto = float(input("Informe a distancia do {0}º salto: ".format(n)))
        saltos.append(salto)
        count = 0
    for n in range(1, 8):
        print("{0}º salto: {1}".format(n, saltos[count]))
        count = count + 1
    print("Atleta: {0}".format(nome))
    print("Melhor salto: {0}".format(max(saltos)))
    print("O pior salto: {0}".format(min(saltos)))
    
    nome = input("Informe o Nome do atleta: ")