soma = 0
for n in range(1,11):
    numero = int(input("Informe o {0} numero:".format(n)))
    soma = numero + soma
print("A soma de todos os numeros é :{0}".format(soma))