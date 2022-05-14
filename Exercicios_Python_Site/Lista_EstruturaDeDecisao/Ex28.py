print("                     Até 5 Kg        Acima de 5 Kg")
print("File Duplo:    R$ 4.90 por Kg       R$ 5.80 por Kg")
print("Alcatra:       R$ 5.90 por Kg       R$ 6.80 por Kg")
print("Picanha:       R$ 6.90 por Kg       R$ 7.80 por Kg")
print("Apenas um tipo de carne pode ser comprada")

nome = input("Informe o nome da carne a ser comprada: ")
quantidade = float(input("Informe a quantidade em Kg: "))

print("Tipos de Pagamentos Disponiveis: \n Cartão de Débito. \n Cartão de Crédito. \n Dinheiro. \n Cartão Tabajara")
tipo_pagamento = input("Informe o tipo de pagamento:")
valor_desconto = 0

if nome.lower() == "file duplo":
    valor = 5.80 * quantidade
    if quantidade <= 5:
        valor_desconto_total = 4.90 * quantidade
        valor_desconto = valor - valor_desconto_total
if nome.lower() == "alcatra":
    valor = 6.80 * quantidade
    if quantidade <= 5:
        valor_desconto_total = 5.90 * quantidade
        valor_desconto = valor - valor_desconto_total
if nome.lower() == "picanha":
    valor = 7.80 * quantidade
    if quantidade <= 5:
        valor_desconto_total = 6.90 * quantidade
        valor_desconto = valor - valor_desconto_total

if tipo_pagamento.lower() == "cartao tabajara":
    desconto_pagamento = valor * 0.05
    valor_desconto = valor_desconto + desconto_pagamento
valor_total = valor - valor_desconto

print("O tipo de carne Escolhida: {0} Kg".format(nome))
print("A quantidade a ser comprada: {0:.2f}".format(quantidade))
print("O total a ser pago: R${0:.2f}".format(valor))
print("O tipo de pagamento: {0} ".format(tipo_pagamento))
print("O valor do desconto: R${0:.2f}".format(valor_desconto))
print("O valor com Desconto: R${0:.2f}".format(valor_total))
