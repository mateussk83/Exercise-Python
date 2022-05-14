"""
Faça uma aplicação que peça 2 números e o tipo de operação basica(+,-,*,/)que o usuário quer realizar com os dois números,
depois mostre ao usuário o resultado da operação realizada. 
"""
num1 = float(input("Informe um numero: "))
num2 = float(input("Informe um numero: "))
simbolo = input("Informe o tipo de operação(+, -, *, /): ")

if simbolo == '*':
    resultado = num1 * num2
    print("A multiplição dos numeros é: {0}".format(resultado))
if simbolo == '+':
    resultado = num1 + num2
    print("A soma dos numeros é: {0}".format(resultado))
if simbolo == '-':
    print("A subtração dos numeros é: {0}".format(resultado))
if simbolo == '/':
    print("A divisão dos numeros é: {0}".format(resultado))    
