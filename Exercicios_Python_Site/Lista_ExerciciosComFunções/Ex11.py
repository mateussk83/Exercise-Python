def validarMes(data):
    lista = data.split("/")   
    if lista[2] < "1" or lista[2] >= "2022":
        return("NULL")
    elif lista[1] <= "0" or lista[1] >"12":
        return("NULL")

    elif lista[1] == "4" or lista[1] == "6" or lista[1] == "9" or lista[1] == "11":
        if lista[0] <= "0" or lista[0] > "30":
              return("NULL")
        else:
             return(lista)
    elif lista[1] == "1" or lista[1] == "3" or lista[1] == "5" or lista[1] == "7" or lista[1] == "8" or lista[1] == "10" or lista[1] == "12":
        if lista[0] <= "0" or lista[0] > "31":
            return("NULL")
        else:
             return(lista)
    elif lista[1] == "2":
        if int(lista[2]) % 4 == 0:
            if lista[0] <= "0" or lista[0] > "29":
                return("NULL")
            else:
                 return(lista)
        elif int(lista[2]) % 4 != 0:
            if lista[0] <= "0" or lista[0] > "28":
                return("NULL")
            else:
                return(lista)

def formatarData(data):
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
    return(lista)

print("Formato data DD/MM/AAAA")
data = input("Informe uma data: ")

validacao = validarMes(data)

if validacao != "NULL":
    dataExtenso = formatarData(data)
    print("{0} de {1} de {2}".format(dataExtenso [0],dataExtenso [1],dataExtenso [2]))
else:
    print("Data Invalida!!")
