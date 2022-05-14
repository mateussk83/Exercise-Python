
def piramide(n):
    for i in range(n):
        i = i + 1
        print(str(i) * i)


n = int(input('Digite um número: '))
piramide(n)