saltos = []
nomes = []
cont = 1
contagem = 0

nome = input("Informe o nome completo do {0}º competidor: ".format(cont))  

while nome != "":  
    for n in range(1,6):
        salto = float(input("Informe o {0}º salto: ".format(n)))
        saltos.append(salto)

    nomes.append(nome)
    print("Atleta: {0}\n".format(nomes[contagem]))
    print("Primeiro Salto: {0}m".format(saltos[0]))
    print(" Segundo Salto: {0}m".format(saltos[1]))
    print(" Terceiro Salto: {0}m".format(saltos[2]))
    print("Quarto Salto: {0}m".format(saltos[3]))
    print("Quinto Salto: {0}m\n".format(saltos[4]))

    melhor = max(saltos)
    pior = min(saltos)
    saltos.remove(max(saltos))
    saltos.remove(min(saltos))
    media = sum(saltos) / len(saltos)

    print("Melhor salto: {0:.1f}m".format(melhor))
    print("Pior salto: {0:.1f}m".format(pior))
    print("Média dos demais saltos: {0:.1f}m".format(media))
    print("Resultado final: \n {0}: {1}m".format(nome, media))
    cont = cont + 1

    print("Para sair basta não informar nada no nome!!!")
    nome = input("Informe o nome completo do {0}º competidor: ".format(cont))  
print("Obrigado por usar nosso Programa!")  

 