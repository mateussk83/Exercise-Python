vetorA = []
vetorB = []
vetorC = []
vetorD = []

for n in range(1,11):
    num = int(input("Informe o {0}º número para armazenar no Vetor A: ".format(n)))
    vetorA.append(num)
for n in range(1,11):
    num = int(input("Informe o {0}º número para armazenar no Vetor B: ".format(n)))
    vetorB.append(num)
for n in range(1,11):
    num = int(input("Informe o {0}º número para armazenar no Vetor B: ".format(n)))
    vetorC.append(num)

for n in range(0,10):
    vetorD.append(vetorA[n])
    vetorD.append(vetorB[n])
    vetorD.append(vetorC[n])
print("Vetor A: {0}".format(vetorA))
print("Vetor B: {0}".format(vetorB))
print("Vetor C: {0}".format(vetorC))
print("Vetor D: {0}".format(vetorD))
