vetorA = []
vetorB = []
vetorC = []

for n in range(1,11):
    num = int(input("Informe o {0}º número para armazenar no Vetor A: ".format(n)))
    vetorA.append(num)
for n in range(1,11):
    num = int(input("Informe o {0}º número para armazenar no Vetor B: ".format(n)))
    vetorB.append(num)
for n in range(0,10):
    vetorC.append(vetorA[n])
    vetorC.append(vetorB[n])
print("Vetor A: {0}".format(vetorA))
print("Vetor B: {0}".format(vetorB))
print("Vetor C: {0}".format(vetorC))
