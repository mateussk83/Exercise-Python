try:
    cpf = input("Informe seu CPF: ")
    ponto = "."
    hifen = "-"
    verificacao = cpf.index(ponto)
    cont = 0
    for num in cpf:
        if num == "0" or num == "1" or num == "2" or num == "3" or num == "4" or num == "5" or num == "6" or num == "7" or num == "8" or num == "9":
            cont = cont + 1
    if cont == 11:
        if verificacao == 3:
            verificacao = cpf.index(ponto,4)
            if verificacao == 7:
                verificacao = cpf.index(hifen)
                if verificacao == 11:
                    print("CPF Valido!!")
except:
    print("CPF Invalido!!")
