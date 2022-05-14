numeros = []
operacao = "s"

while operacao.lower() == "s":
    num = int(input("Informe um número: "))
    if num > 0 and num < 1000:
        numeros.append(num)
    else:
        print("Por favor informe um número entre 0 e 1000")
        num = int(input("Informe um número: "))
    print("Responda com S ou N")
    operacao = input("Deseja Continuar a operação?: ")
    if operacao.lower() != "s" or operacao.lower() != "n":
        print("Finalizaremos o programa pois a resposta foi diferente de sim ou não!!!!")
print("O maior número digitado foi: {0}".format(max(numeros)))
print("O menor número digitado foi: {0}".format(min(numeros)))
print("A soma dos números digitado foi: {0}".format(sum(numeros)))