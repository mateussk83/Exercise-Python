data = input("Informe a data de nascimento: ")

lista = data.split("/") 
if lista[1] == "01":
    lista[1] = "Janeiro"
elif lista[1] == "02":
    lista[1] = "Fevereiro"
elif lista[1] == "03":
    lista[1] = "Março"
elif lista[1] == "04":
    lista[1] = "Abril"
elif lista[1] == "05":
    lista[1] = "Maio"
elif lista[1] == "06":
    lista[1] = "Junho"
elif lista[1] == "07":
    lista[1] = "Julho"
elif lista[1] == "08":
    lista[1] = "Agosto"
elif lista[1] == "09":
    lista[1] = "Setembro"
elif lista[1] == "10":
    lista[1] = "Outubro"
elif lista[1] == "11":
    lista[1] = "Novembro"
elif lista[1] == "12":
    lista[1] = "Dezembro"

print("Você nasceu em {0} de {1} de {2}".format(lista[0],lista[1],lista[2]))