numero = int(input("Informe até qual numero quer saber se é primo: "))
primos = []
contagem = 0
for n in range(2,numero + 1):
    num = n
    multiplo = 0

    for n in range(2,num):
        if num % n == 0:
            multiplo = multiplo + 1
    if multiplo == 0: 
        primos.append(num)
print("Os números primos são: {0}".format(primos))