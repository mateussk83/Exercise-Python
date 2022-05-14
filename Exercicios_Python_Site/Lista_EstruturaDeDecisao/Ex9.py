numeros = []

num1 = int(input("Informe o primeiro número: "))
num2 = int(input("Informe o segundo número: "))
num3 = int(input("Informe o terceiro número: "))

numeros.append(num1)
numeros.append(num2)
numeros.append(num3)

numeros.sort()
print("A ordem dos números digitado do menor para o maior é: {0}".format(numeros[::-1]))
