num1 = input("Informe o primeiro número: ")
num2 = input("Informe o segundo número: ")

print("Operações Disponíveis: \n a - par ou ímpar; \n b - positivo ou negativo; \n c - inteiro ou decimal.")

operacao = input("Informe com a,b,c: ")
a = "."
if operacao.lower() == "a":
    num1 = int(num1)
    num2 = int(num2)
    if num1 % 2 == 0:
        print("O {0} número é par!!".format(num1))
    if num2 % 2 == 0:
        print("O {0} número é impar!!".format(num2))
    if num1 % 2 != 0:
        print("O {0} número é impar!!".format(num1))
    if num2 % 2 != 0:
        print("O {0} número é impar!!".format(num2))
if operacao.lower() == "b":
    num1 = int(num1)
    num2 = int(num2)
    if num1 >= 0:
        print("O {0} número é positivo!!".format(num1))
    if num2 >= 0:
        print("O {0} número é positivo!!".format(num2))
    if num1 < 0:
        print("O {0} número é negativo!!".format(num1))
    if num2 < 0:
        print("O {0} número é negativo!!".format(num2))
if operacao.lower() == "c":
    if a in num1:
        print("O {0} número é Decimal".format(num1))
    else: 
        print("O {0} número é Inteiro".format(num1))
    if a in num2:
        print("O {0} número é Decimal".format(num2))
    else: 
        print("O {0} número é Inteiro".format(num2))
elif operacao.lower() != "a" and operacao.lower() != "b" and operacao.lower() != "c":
    print("Lamentamos não temos esta operação")
    
