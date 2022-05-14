opcao = 0
while opcao != 5:
    print("Opção 1: adição")
    print("Opção 2: subtração")
    print("Opção 3: multiplicação")
    print("Opção 4: divisão")
    print("Opção 5: saida\n")
    opcao = int(input("Informe a Opção desejada:"))
    if(opcao == 1):
        num1 = int(input("Informe o 1º numero: "))
        num2 = int(input("Informe o 2º numero: "))
        soma = num1 + num2
        print("A soma dos numeros digitados é {0}!\n".format(soma))
    if(opcao == 2):
        num1 = int(input("Informe o 1º numero: "))
        num2 = int(input("Informe o 2º numero: "))
        subtracao = num1 - num2
        print("A subtração dos numeros digitados é {0}!\n".format(subtracao))
    if(opcao == 3):
        num1 = int(input("Informe o 1º numero: "))
        num2 = int(input("Informe o 2º numero: "))
        multiplicacao = num1 * num2
        print("A multiplicação dos numeros digitados é {0}!\n".format(multiplicacao))
    if(opcao == 4):
        num1 = int(input("Informe o 1º numero: "))
        num2 = int(input("Informe o 2º numero: "))
        divisao = num1 + num2
        print("A divisão dos numeros digitados é {0}!\n".format(divisao))
    if(opcao == 5):
        print("Obrigado por utilizar o Programa!!\n")
        break
    if(opcao != 1 or 2 or 3 or 4 or 5):
        print("Por favor escolha uma opção \n")
        