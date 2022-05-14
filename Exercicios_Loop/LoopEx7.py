maior = -9999999
menor = 9999999
for n in range(1,11):
    numero = int(input("Informe o {0}º numero: ".format(n)))
    if(numero < menor):
        menor = numero
    if(numero > maior):
        maior = numero
print("O maior numero digitado é {0} e o menor numero digitado é {1}!".format(maior,menor))