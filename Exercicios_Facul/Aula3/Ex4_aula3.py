"""
Crie um algoritmo para uma urna eleitoral que deve conter 3 cantidados e no final imprima a quantidade de votos que cada candidatos tem.
"""
cont_A = 0
cont_B = 0
cont_C = 0
votu = input("Informe o seu voto (A, B, C): ")

while votu == 'a' or votu == 'b' or votu == 'c':
    if votu == "a":
        cont_A = cont_A + 1
    elif votu == "b":
        cont_B = cont_B + 1
    elif votu == "c":
        cont_C = cont_C + 1
    votu = input("Informe o seu voto (A, B, C): ")
print("Candidato A tem {0} votos".format(cont_A))
print("Candidato B tem {0} votos".format(cont_B))
print("Candidato C tem {0} votos".format(cont_C))