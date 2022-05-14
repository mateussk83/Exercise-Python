print("                 Até 5 Kg        Acima de 5 Kg")
print("Morango:   R$ 2.50 por Kg       R$ 2.20 por Kg")
print("Maçã:      R$ 1.80 por Kg       R$ 1.50 por Kg")
print("PROMOÇÂO: Se comprar mais de 8 kilos ou passar o total da compra o valor de R$ 25,00 receberá um desconto de 10%")

morango = float(input("Informe a quantidade de morangos em Kg: "))
maca = float(input("Informe a quantidade de maçã em Kg: "))

kilo = morango + maca

if morango > 5:
    valor_morango = morango * 2.20
if morango <= 5:
    valor_morango = morango * 2.50
if maca > 5:
    valor_maca = maca * 1.50
if maca <= 5:
    valor_maca = maca * 1.80

valor_total = valor_maca + valor_morango

if valor_total > 25 or kilo > 8:
    valor_total = valor_total - (valor_total * 0.10)

print("O valor total é de: R${0:.2f}".format(valor_total))
 
