#Variaveis
p = 0
i = 0

#Entradas
n = int(input("Informe um numero: "))

#Processamentos
if n % 2 == 0:
    p = n
else:
    i = n

#Saidas
print("i = {0}".format(i))
print("p = {0}".format(p))