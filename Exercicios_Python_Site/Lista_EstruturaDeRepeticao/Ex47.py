votos = []
nomes = []
cont = 1
contagem = 0

nome = input("Informe o nome completo do {0}º competidor: ".format(cont))  
 
for n in range(1,8):
    voto = float(input("Informe a {0}º nota: ".format(n)))
    votos.append(voto)
nomes.append(nome)
print("Atleta: {0}\n".format(nomes[contagem]))
print("Nota: {0}".format(votos[0]))
print("Nota: {0}".format(votos[1]))
print("Nota: {0}".format(votos[2]))
print("Nota: {0}".format(votos[3]))
print("Nota: {0}".format(votos[4]))
print("Nota: {0}".format(votos[5]))
print("Nota: {0}\n".format(votos[6]))
melhor = max(votos)
pior = min(votos)
votos.remove(max(votos))
votos.remove(min(votos))
media = sum(votos) / len(votos)
print("Resultado final: \nAtleta: {0}".format(nome))
print("Melhor Nota: {0:.1f}m".format(melhor))
print("Pior Nota: {0:.1f}m".format(pior))
print("Média: {0:.1f}m".format(media))