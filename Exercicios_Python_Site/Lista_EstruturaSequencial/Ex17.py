"""
Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
comprar apenas latas de 18 litros;
comprar apenas galões de 3,6 litros;
misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.
"""
import math 

tamanho = float(input("Informe o tamanho em tamanho quadrados da área a ser pintada: "))

latas = tamanho / 6
if (latas <=0):
    latas = 1
 
QTDLatas = math.floor(latas / 18+(18*0.10)) 
QTDGaloes = math.floor(latas / 3.6+(3.6*0.10)) 
QTDLatas = latas / 18 
RESTO = latas % 18

if (RESTO > 0 and RESTO<= 3.6):
    QTDGaloes = 1
elif  (RESTO==0):
    QTDGaloes = 0
else:
    QTDGaloes = math.floor(RESTO / 3.6+(3.6*0.10))

if (QTDLatas  < 1 or QTDGaloes < 1 or QTDGaloes < 1):
    QTDGaloes=1
    QTDLatas=1
    QTDGaloes=1
 
ValorLatas = QTDLatas * 80
ValorGaloes = QTDGaloes * 25

MelhorValor = ValorLatas + ValorGaloes

print("Comprando apenas latas de 18 litros você terá que comprar: {0} com o valor de: R${1:.2f}".format(int(QTDLatas),ValorLatas,))
print("Comprando apenas galões de 3.6 litros você terá que comprar: {0} com o valor de: R${1:.2f}".format(int(QTDGaloes),ValorGaloes))
print("Agora misturando latas e galões você terá que comprar: {0} galões e {1} Latas com o valor de: R${2:.2f} ".format(int(QTDGaloes),int(QTDLatas),MelhorValor))
 
 