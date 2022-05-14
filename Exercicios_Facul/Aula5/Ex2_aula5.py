num = int(input("Informe um numero"))

if num > 10:
    print("o numero tem q ser menor que 10")
    num = int(input("Informe um numero"))
print("A tabela do {0} é".format(num))
if num < 10:
    for n in range(1, 11):
        multiplicacao = n * num
        print("{0} x {1} = {2}".format(n, num, multiplicacao))