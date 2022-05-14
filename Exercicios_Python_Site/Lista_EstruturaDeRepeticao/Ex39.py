alunos = []
altura = []

for n in range(1,11):
    nome = input("Informe o nome do {0}º aluno: ".format(n))
    tamanho = int(input("Informe a altura do {0}º aluno em centimetros: ".format(n)))
    alunos.append(nome)
    altura.append(tamanho)
menor_indice = altura.index(min(altura))
maior_indice = altura.index(max(altura))

print("O maior aluno é {0} com a altura de: {1}cm".format(maior_indice, altura[maior_indice]))
print("O menor aluno é {0} com a altura de: {1}cm\n".format(menor_indice, altura[menor_indice]))
