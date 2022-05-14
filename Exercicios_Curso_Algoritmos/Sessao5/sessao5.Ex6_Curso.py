#variaveis
vetor = []
codigo = int(input("Informe o codigo: "))

#entradas
for n in range(1, 6):
    num = int(input("Informe um numero:"))
    vetor.append(num)
    if codigo == 1:
        print(vetor)
    if codigo == 2:
        vetor.reverse()
        print(vetor)
    if codigo == 0:
        print("Fim do programa")
