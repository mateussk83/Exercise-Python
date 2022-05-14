print("Desse estilo DD/MM/AAAA")
data = input("Informe a data: ")

lista = data.split("/")

if lista[2] < "1" or lista[2] >= "2022":
    print("Data Invalida!!!")
elif lista[1] <= "0" or lista[1] >"12":
    print("Data Invalida!!!")

elif lista[1] == "4" or lista[1] == "6" or lista[1] == "9" or lista[1] == "11":
    if lista[0] <= "0" or lista[0] > "30":
          print("Data Invalida!!!")
    else:
         print("Data valida!!")
elif lista[1] == "1" or lista[1] == "3" or lista[1] == "5" or lista[1] == "7" or lista[1] == "8" or lista[1] == "10" or lista[1] == "12":
    if lista[0] <= "0" or lista[0] > "31":
        print("Data Invalida!!!")
    else:
         print("Data valida!!")
elif lista[1] == "2":
    if int(lista[2]) % 4 == 0:
        if lista[0] <= "0" or lista[0] > "29":
            print("Data Invalida!!!")
        else:
             print("Data valida!!")
    elif int(lista[2]) % 4 != 0:
        if lista[0] <= "0" or lista[0] > "28":
            print("Data Invalida!!!")
        else:
            print("Data valida!!")