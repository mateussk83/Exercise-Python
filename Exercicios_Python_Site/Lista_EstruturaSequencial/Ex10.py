"""
Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.
"""
c = float(input("Informe a temperatura em graus Celsius:"))

f = (c * 9/5) + 32 

print("{0} em graus Celsius é igual a {1} em graus Fahrenheit".format(c,f))