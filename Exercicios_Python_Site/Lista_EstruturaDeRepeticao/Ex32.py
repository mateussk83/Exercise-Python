
num = int(input("Digite o valor de n: "))
fatorial = 1
i = 2
expoentes = []
if num <= 16:
    while i <= num:
        fatorial = fatorial * i
        expoentes.append(str(i))
        i = i + 1

expoentes.reverse()
numeros = " . ".join(expoentes)
print("O valor de {0}! = {1} = {2}".format(num,numeros,fatorial))