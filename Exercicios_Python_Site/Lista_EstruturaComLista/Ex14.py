perguntas = ["Telefonou para a vítima?", "Esteve no local do crime?", "Mora perto da vítima?","Devia para a vítima?","Já trabalhou com a vítima?"]
respostas = []

print("Responda com SIM ou NAO!!")
for n in range(0,5):
    resposta = input(perguntas[n])
    respostas.append(resposta.lower())
indice = respostas.count("sim")

if indice == 2:
    print("A pessoa é Suspeita!!")
if indice == 3 or indice == 4:
    print("A pessoa é Cúmplice!!")
if indice == 5:
    print("A pessoa é Assassina!!")
elif indice != 2 and indice != 3 and indice != 4 and indice != 5:
    print("A pessoa é Inocente")
