alturas = []
idades = []
pequeno_media = 0
for n in range(1,31):
    idade = int(input("Informe a {0}ª idade: ".format(n)))
    altura = int(input("Informe a {0}ª altura: ".format(n)))
    idades.append(idade)
    alturas.append(altura)
media = sum(alturas) / len(alturas)
contagem = 0
for idade in idades:
    if idade > 13 and alturas[contagem] < media:
        pequeno_media= pequeno_media + 1
    contagem = contagem + 1
print("Os alunos com mais de 13 anos e altura inferior à média é: {0}".format(pequeno_media))
