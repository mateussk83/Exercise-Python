#Entradas
altura = float(input("Informe sua altura: "))
sexo = input("Informe o seu sexo m/f:  ")

#Processamentos
if sexo.lower() == 'm':
    peso_ideal = (72.7 * altura) - 58
elif sexo.lower() == 'f':
    peso_ideal = (62.1 * altura) - 44.7
else:
    peso_ideal = 0
    sexo = input("Informe o seu sexo m/f:  ")

print("Seu peso ideal é {0}".format(peso_ideal))
