operacao = "s"
numeros = []
n = 0
while operacao.lower() == "s":
    num = int(input("Informe o número:  "))
    n = n + 1
    numeros.append(num)
    print("Responda com S - sim ou N - não!!")
    operacao = input("Informe Se quiser prosseguir com a operacao: ")

if operacao.lower() != "n" and operacao.lower() != "s":
    print("Infelizmente finalizaremos a operação pois a resposta não foi Valida!!")
else:
    media = sum(numeros) / n
    print("A média dos números digitados é: {0:.2f}".format(media))
