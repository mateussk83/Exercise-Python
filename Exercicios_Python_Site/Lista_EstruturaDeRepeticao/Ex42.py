numeros25 = []
numeros50 = []
numeros75 = []
numeros100 = []

cont = 1
num = int(input("Informe o {0}º número: ".format(cont)))

while num > 0 :
    if num > 0 and num <= 26:
        numeros25.append(num)
    elif num > 25 and num <= 50:
        numeros50.append(num)
    elif num > 50 and num <= 75:
        numeros75.append(num)
    elif num > 75 and num <= 100:
        numeros100.append(num)
    if num > 100:
        print("Informe números de 0 a 100")
    cont = cont + 1
    num = int(input("Informe o {0}º número: ".format(cont)))

print("Os números digitados que são entre 0 - 25 é: {0}".format(numeros25))
print("Os números digitados que são entre 26 - 50 é: {0}".format(numeros50))
print("Os números digitados que são entre 51 - 75 é: {0}".format(numeros75))
print("Os números digitados que são entre 76 - 100 é: {0}".format(numeros100))