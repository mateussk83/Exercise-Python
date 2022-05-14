medias = []
notas = []
for n in range(1,11):
    print("Informe as notas do {0} aluno: ".format(n))
    for n in range(1,5):
        nota = int(input("Informe o {0}ª nota: ".format(n)))
        notas.append(nota)
    media = sum(notas) / len(notas)
    if media >= 7:
        medias.append(media)
        notas = []
print("O número de alunos aprovado foi: {0}".format(len(medias)))