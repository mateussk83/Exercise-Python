#Entradas
idade = int(input("Informe a idade"))

#variaveis
if idade >= 5 and idade <= 7:
    print("Grupo Infantil A")
elif idade >= 8 and idade <= 11:
    print("Grupo Infantil B")
elif idade >= 12 and idade <= 13:
    print("Grupo Juvenil A")
elif idade >= 14 and idade <= 17:
    print("Grupo Juvenil B")
elif idade >= 18:
    print("Grupo Adulto")