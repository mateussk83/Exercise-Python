#variaveis
vetor = []
soma = 0

#entradas
for n in range(1, 21):
    num = int(input("Informe um numero: "))
    vetor.append(num)
    print("A soma dos vetores é {0}".format(sum(vetor)))
