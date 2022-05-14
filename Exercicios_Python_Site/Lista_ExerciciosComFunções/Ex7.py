def valorPagamento(valorPrestacao,diasAtraso):
    juros = 0.03
    dia = 0.001
    if diasAtraso <= 0:
        valorTotal = valorPrestacao
    else:
        valorTotal = valorPrestacao + (valorPrestacao * juros) + (diasAtraso * (valorPrestacao * dia))
    return(valorTotal)

valor = 1
while valor != 0:
    valor = float(input("Informe o valor da prestação: "))
    if valor == 0:
        print("Obrigado por usar nosso programa")
        break
    dia = int(input("Informe os dias em atraso da divida: "))
    print("O valor a ser pago é: R${0:.2f}".format(valorPagamento(valor,dia)))
