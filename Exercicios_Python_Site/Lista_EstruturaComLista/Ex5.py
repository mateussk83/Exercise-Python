numeros = []
par = []
impar = []

for n in range(1,21):
    num = int(input("Informe o {0}º numero: ".format(n)))
    numeros.append(num)

for n in numeros:
    if n % 2 == 0:
        par.append(n)
    elif n % 2 != 0:
        impar.append(n)

print("Os números pares é: {0}".format(par))
print("Os números impares é: {0}".format(impar))
