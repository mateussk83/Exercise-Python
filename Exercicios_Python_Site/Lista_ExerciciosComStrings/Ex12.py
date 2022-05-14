
try:
    print("Valida e corrige o número de telefone")
    numeroLista = []
    numero = input("Telefone: ")
    numeroSemFormatacao = ""
    numeroLista = numero.split("-")
    numeroSemFormatacao = "".join(numeroLista)
    if len(numeroSemFormatacao) == 7:
        numero = "3" + numero
        numeroSemFormatacao = "3" + numeroSemFormatacao
        print("Telefone possui 7 digitos. Vou acrescentar o digito três na frente")
    print("Telefone corrigido sem formatação: {0}".format(numeroSemFormatacao))
    print("Telefone corrigido com formatação: {0}".format(numero))
except:
    print("Número de Telefone Invalido")

