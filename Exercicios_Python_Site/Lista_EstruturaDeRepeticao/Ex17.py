num = int(input("Digite o valor de n: "))
fatorial = 1
i = 2
while i <= num:
    fatorial = fatorial * i
    i = i + 1
print("O valor de {0}! é: {1}".format(num,fatorial))
