def moldura(linha, coluna):
    linhas = "-"
    espacos = ""
    while coluna > 20 or coluna < 1 or linha > 20 or linha < 1:
        if linha > 20 or linha < 1:
            print("Valor Invalido por favor informe um valor entre 1 e 20!!")
            linha = int(input("Informe o valor da linha: "))
        if coluna > 20 or coluna < 1:
             print("Valor Invalido por favor informe um valor entre 1 e 20!!")
             coluna = int(input("Informe o valor da coluna: "))
    for n in range(1,linha):
        linhas = linhas + '-'
    print(linhas)
    espacos = " " * (len(linhas) - 2)
    for n in range(1,coluna):
        print("|{0}|".format(espacos))
    print(linhas)

moldura(10,4)