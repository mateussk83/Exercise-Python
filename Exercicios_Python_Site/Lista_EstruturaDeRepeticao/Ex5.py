populacaoA = int(input("Informe a população A: "))
populacaoB = int(input("Informe a populaçao B: "))
crescimentoA = float(input("Informe o crescimento da população A em porcentagem: "))
crescimentoB = float(input("Informe o crescimento da população B em porcentagem: "))
operacao = "sim"
while operacao == "sim":
    if populacaoA > 0 and populacaoB > 0 and populacaoA > 0 and populacaoA > 0:
        anos = 0
        while populacaoA < populacaoB:
            anos = anos + 1
            populacaoA = populacaoA + (populacaoA * (crescimentoA / 100))
            populacaoB = populacaoB + (populacaoB * (crescimentoB / 100))
    else:
        print("Por favor informe os valores positivos.")
    print("Os anos necessarios para a população A passar a população B é de : {0}".format(anos))
    print("Responda com sim ou não")
    operacao = input("Desejar repetir o processo?  ")
    if operacao == "sim":
        populacaoA = int(input("Informe a população A: "))
        populacaoB = int(input("Informe a populaçao B: "))
        crescimentoA = float(input("Informe o crescimento da população A em porcentagem: "))
        crescimentoB = float(input("Informe o crescimento da população B em porcentagem: "))
    else:
        print("Obrigado por usar nosso Programa!!!")
    
