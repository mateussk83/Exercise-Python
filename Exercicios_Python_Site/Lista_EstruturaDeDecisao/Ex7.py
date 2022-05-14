numeros = []

num1 = int(input("Informe o primeiro número: "))
num2 = int(input("Informe o segundo número: "))
num3 = int(input("Informe o terceiro número: "))

numeros.append(num1)
numeros.append(num2)
numeros.append(num3)

print("O maior número deles é: {0}".format(max(numeros)))
print("O menor número deles é: {0}".format(min(numeros)))