n = int(input("Informe o valor de n: "))
def piramide(n):
    x = 1
    for n in range(1, n + 1):
        p = (str(x) + " ") * n
        print(p)
        x = x + 1
    
piramide(n)