n = int(input("Informe o numero para o termo: "))
divisao = []
mostrar = ["1"]
soma = 0
cont = 1
cont1 = 1
for n in range(1,n):
    cont = cont + cont1
    divisao.append(str(cont1))
    divisao.append(str(cont))
    soma = soma + cont1 / cont
    divisinha = "/".join(divisao)
    mostrar.append(divisinha)
    divisao = []
transformou = " + ".join(mostrar)

print("{0:.2f} = {1}".format(soma + 1,transformou))
    