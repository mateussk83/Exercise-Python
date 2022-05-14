n = int(input("Informe o valor de n: "))
def piramide(n):
    x = 1
    p = (str(x) + " ")
    print(p)
    for n in range(1, n):
        x = x + 1
        p = p + str(x) + " "
        print(p)
piramide(n)