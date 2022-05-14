numeros = []

resultado = 0
num1 = 1
multiplo = 3
contagem = 0

while contagem<5:
    if num1 > 0:
        resultado = num1 * multiplo
        num1 = num1 + 1
        contagem = contagem + 1
        numeros.append(resultado)

print("os 5 primeiros multiplos de 3 são: {0}".format(numeros))
