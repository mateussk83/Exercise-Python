
quantidade_turmas = int(input("Informe quantas turmas tem em sua escola?: "))
alunos = []
x = 0
print("Quantidade de alunos maxima por sala é de 40 alunos!!")
for n in range(1, quantidade_turmas + 1):
    
    aluno = int(input("Informe a quantidade de alunos da {0}ª turma: ".format(n)))
    while aluno > 40:
        aluno = int(input("Informe novamente a quantidade de alunos da {0}ª turma: ".format(n)))
    alunos.append(aluno)
    x = x + 1 
media = sum(alunos) / x

print("A média de alunos por classe é: {0:.2f}".format(media))

