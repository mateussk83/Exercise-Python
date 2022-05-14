n = int(input("Informe o numero para o termo: "))
divisao = []
mostrar = []
soma = 0
cont1 = 1

cont2 = 1  
for n in range(1,n + 1):
    cont1 = cont1 + 1
    cont2 = cont2 + 2
    divisao.append(str(cont1))
    divisao.append(str(cont2))
    soma = soma + cont1/cont2
    divisinha = "/".join(divisao)
    mostrar.append(divisinha)
    divisao = []
transformou = " + ".join(mostrar)

print("{0:.2f} = {1}".format(soma,transformou))
    