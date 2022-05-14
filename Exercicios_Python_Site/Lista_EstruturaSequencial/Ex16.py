"""
Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.
"""
tamanho = float(input("Informe o tamanho em metros quadrados da área a ser pintada: "))

litro = tamanho / 3
QTDLata = litro / 18
RESTOLata = litro % 18

if QTDLata < 1: 
    QTDLata = 1
if RESTOLata != 0:
    QTDLata = QTDLata + 1

ValorLata = QTDLata * 80
RESTOValor = ValorLata % 80
print(RESTOValor)
if RESTOValor != 0:
    ValorLata = ValorLata - RESTOValor
    ValorLata = ValorLata + 80


print("A quantidade de Latas de 18 litros a comprar é:{0} o valor a ser pago é: R${1:.2f} ".format(int(QTDLata),ValorLata))