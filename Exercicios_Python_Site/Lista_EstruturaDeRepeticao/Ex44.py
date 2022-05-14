joao = 0
pedro = 0
mateus = 0
maria = 0
nulo = 0
branco = 0
total = 0

print("Candidatos: \n1 - João\n2 - Pedro\n3 - Mateus\n4 - Maria\n5 - Voto Nulo\n6 - Voto em Branco")
voto = int(input("Informe qual candidato quer votar: "))

while voto != 0:
    if voto == 1:
        joao = joao + 1
    elif voto == 2:
        pedro = pedro + 1
    elif voto == 3:
        mateus = mateus + 1
    elif voto == 4:
        maria = maria + 1
    elif voto == 5:
        nulo = nulo + 1
    elif voto == 6:
        branco = branco + 1
    total = total + 1
    voto = int(input("Informe qual candidato quer votar: "))
    

print("A quantidade de votos para o Candidato João foi: {0}".format(joao))
print("A quantidade de votos para o Candidato Pedro foi: {0}".format(pedro))
print("A quantidade de votos para o Candidato Mateus foi: {0}".format(mateus))
print("A quantidade de votos para o Candidato Maria foi: {0}".format(maria))
print("A quantidade de votos nulo foi: {0}".format(nulo))
print("A quantidade de votos em branco foi: {0}".format(branco))

percentual_nulo = (100*nulo) / total
percentual_branco = (100*branco) / total
print("O percentual de votos nulos em relação ao total é: {0}%".format(int(percentual_nulo)))
print("O percentual de votos brancos em relação ao total é: {0}%".format(int(percentual_branco)))