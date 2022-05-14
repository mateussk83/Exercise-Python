numeros = []
operacao = "s"

while operacao.lower() == "s":
    num = int(input("Informe um número: "))
    numeros.append(num)
    print("Responda com S ou N")
    operacao = input("Deseja Continuar a operação?: ")
print("O maior número digitado foi: {0}".format(max(numeros)))
print("O menor número digitado foi: {0}".format(min(numeros)))
print("A soma dos números digitado foi: {0}".format(sum(numeros)))
