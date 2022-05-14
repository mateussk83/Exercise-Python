operacao = "s"
while operacao.lower() == "s":
    num = int(input("Digite o valor de n: "))
    fatorial = 1
    i = 2
    if num <= 16:
        while i <= num:
            fatorial = fatorial * i
            i = i + 1
        print("O valor de {0}! é: {1}".format(num,fatorial))
    else:
        print("O programa suporta até o 16 fatorial")
    
    print("\n Informe com S - SIM ou N - Não ")
    operacao = input("Deseja Continuar esta operação?: ")
    if operacao.lower() != "s" or operacao.lower() != "n":
        print("Finalizaremos o programa pois a resposta foi diferente de sim ou não!!!!")