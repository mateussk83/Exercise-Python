eleitores = int(input("Informe a quantidade de eleitores que irão votar: "))
candidatoA = 0
candidatoB = 0
candidatoC = 0
for n in range(1, eleitores + 1):
    print("Escolha o candidato com A, B ou C!!\nA - Joáo \nB - Pedro\nC - Maria ")
    voto = input("Informe o seu voto: ")
    if voto.lower() == "a":
        candidatoA = candidatoA + 1
    elif voto.lower() == "b":
        candidatoB = candidatoB + 1
    elif voto.lower() == "c":
        candidatoC = candidatoC + 1
print("A quantidade de votos ao João foi: {0}".format(candidatoA))
print("A quantidade de votos ao Pedro foi: {0}".format(candidatoB))
print("A quantidade de votos a Maria foi: {0}".format(candidatoC))