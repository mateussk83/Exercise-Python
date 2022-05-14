#variaveis
vetor = []

#entradass
for n in range(1, 11):
    num1 = int(input("Informe um numero: "))
    vetor.append(num1)
vetor.reverse()
for n in vetor:
    print(n)
    