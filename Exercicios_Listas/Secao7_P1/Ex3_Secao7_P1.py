numeros1 = []
numeros2 = []
numeros = []

for n in range(1,11):
    num1 = int(input("Informe o {0}º numero para o primeiro vetor:").format(n))
    numeros1.append(num1)
    num2 = int(input("Informe o {0}º numero para o segundo vetor:").format(n))
    numeros2.append(num2)
    if(num1 == num2):
        numeros.append(num1)
print("Os numeros digitados no primeiro vetor é: {0}".format(numeros1))
print("Os numeros digitados no segundo vetor é: {0}".format(numeros2))
print("Os numeros digitados que são iguais é: {0}".format(numeros))