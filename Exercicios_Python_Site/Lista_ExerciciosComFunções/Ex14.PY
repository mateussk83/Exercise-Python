import random

vetor = [1,2,3,4,5,6,7,8,9]

vetor = random.sample(vetor,9)


def quadradoMagico(vetor):
    if vetor[0] + vetor[1] + vetor[2] == vetor[3] + vetor[4] + vetor[5] == vetor[6] + vetor[7] + vetor[8] == vetor[0] + vetor[3] + vetor[6] == vetor[1] + vetor[4] + vetor[7] == vetor[2] + vetor[5] + vetor[8] == vetor[0] + vetor[4] + vetor[8] == vetor[2] + vetor[4] + vetor[6]:
       return("É um quadrado mágico")
    else:
        return("Não é um quadrado mágico")

contagem = 0
while contagem != 10:
    teste = "Não é um quadrado mágico"
    while teste == "Não é um quadrado mágico":
         vetor = random.sample(vetor,9)
         teste = quadradoMagico(vetor)
         if teste != "Não é um quadrado mágico":
            print(vetor)
    contagem = contagem + 1