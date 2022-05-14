
operacao = "s"
respostas = []
gabarito = ["a","b","c","d","e","e","d","c","b","a"]
cont = 0
notas = []
nota = 0


while operacao.lower() == "s":
    for n in range(1,11):
        resposta = input("Informe qual alternativa você assinalou na {0}ª Questão: ".format(n))
        respostas.append(resposta)
    for resposta in respostas:
        if respostas[cont] == gabarito[cont]:
            nota = nota + 1
        cont = cont + 1
    notas.append(nota)
    print("Responda com S - SIM ou N - NAO")
    operacao = input("Proximo aluno?: ")
    cont = 0
    nota = 0
    respostas = []
menor_nota = notas.index(min(notas))
maior_nota = notas.index(max(notas))
media = sum(notas) / len(notas)
print("A maior nota da classe foi: {0} \n A menor nota da classe foi: {1}".format(notas[maior_nota],notas[menor_nota]))
print("O Total de alunos que realizaram a prova foi: {0}".format(len(notas)))
print("A Média geral da sala foi: {0:.1f}".format(media))