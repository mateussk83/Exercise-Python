x = []
y = []
soma = []
multiplicacao = []
diferenca = []
intersecao = []
uniao = []

for n in range(1,6):
    num1 = int(input("Informe o {0}º numero para o vetor x: ".format(n)))
    x.append(num1)
    num2 = int(input("\nInforme o {0}º numero para o vetor y: ".format(n)))
    y.append(num2)
    adicao = num1 + num2
    soma.append(adicao)
    vezes = num1 * num2
    multiplicacao.append(vezes)
uniao = x.copy()
for n in range(0,5):
    if x[n] in y:
        intersecao.append(x[n])
        uniao.append(x[n])
    else:
        diferenca.append(x[n])

        

print("Os valores do vetor x é: {0}".format(x))
print("Os valores do vetor y é: {0}".format(y))
print("Os valores da soma entre y e x é: {0}".format(soma))
print("Os valores da multiplicação entre y e x é: {0}".format(multiplicacao))
print("Os valores que estao em x que não existem em y é: {0}".format(diferenca))
print("Os valores que estao nos dois vetores é: {0}".format(intersecao))
print("A união dos dois vetores é: {0}".format(uniao))



