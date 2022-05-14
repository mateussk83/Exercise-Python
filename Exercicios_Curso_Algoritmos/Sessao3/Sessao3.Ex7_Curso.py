#entradas
n1 = int(input("Informe o primeiro numero:"))
n2 = int(input("Informe o segundo numero:"))
n3 = int(input("Informe o terceiro numero:"))
n4 = int(input("Informe o quarto numero:"))

#processamentos
q1 = n1 * n1
q2 = n2 * n2
q3 = n3 * n3
q4 = n4 * n4

if q3 >= 1000:
    print("o quadrado do numero {0} é {1}".format(n3, q3))
else:
    print("o quadrado do numero {0} é {1}".format(n1, q1))
    print("o quadrado do numero {0} é {1}".format(n2, q2))
    print("o quadrado do numero {0} é {1}".format(n3, q3))
    print("o quadrado do numero {0} é {1}".format(n4, q4))
