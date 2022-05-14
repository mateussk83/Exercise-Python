print("Valor por litro do Álcool: R$1.90")
print("Valor por litro da Gasolina: R$2.50")
print("PROMOÇÂO!!")
print("Álcool: \n Até 20 litros, desconto de 3% por litro \n Acima de 20 litros, desconto de 5% por litro")
print("Gasolina: \n Até 20 litros, desconto de 4% por litro \n Acima de 20 litros, desconto de 6% por litro")
print("Temos Disponiveis : \n A - Álcool \n G - Gasolina ")

combustivel = input("Informe o tipo de Combustível com A ou G: ")
litro = float(input("Informe a quantidade em Litros a ser comprada: "))

if combustivel.lower() == "a":
    if litro <= 20:
        valor = litro * 1.90
        valor_desconto = valor * 0.03
        valor_total = valor_desconto + valor
    else: 
        valor = litro * 1.90
        valor_desconto = valor * 0.04
        valor_total = valor_desconto + valor
    print("O valor total a ser pago é : R${0:.2f}".format(valor_total))
elif combustivel.lower() == "g":
    if litro <= 20:
        valor = litro * 2.50
        valor_desconto = valor * 0.04
        valor_total = valor_desconto + valor
    else: 
        valor = litro * 2.50
        valor_desconto = valor * 0.06
        valor_total = valor_desconto + valor
    print("O valor total a ser pago é : R${0:.2f}".format(valor_total))
