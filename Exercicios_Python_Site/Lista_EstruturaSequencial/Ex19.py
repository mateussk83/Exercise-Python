data = input("Informe a data(DD/MM/AAAA: ")

lista = data.split('/')

if lista[0] > "31" and lista[1] == "01":
    print("Esta data não existe!!")
elif lista[0] > "31" and lista[1] == "03":
    print("Esta data não existe!!")
elif lista[0] > "31" and lista[1] == "05":
    print("Esta data não existe!!")
elif lista[0] > "31" and lista[1] == "07":
    print("Esta data não existe!!")
elif lista[0] > "31" and lista[1] == "08":
    print("Esta data não existe!!")
elif lista[0] > "31" and lista[1] == "10":
    print("Esta data não existe!!")
elif lista[0] > "31" and lista[1] == "12":
    print("Esta data não existe!!")
elif lista[0] > "30" and lista[1] == "04":
    print("Esta data não existe!!")
elif lista[0] > "30" and lista[1] == "06":
    print("Esta data não existe!!")
elif lista[0] > "30" and lista[1] == "09":
    print("Esta data não existe!!")
elif lista[0] > "30" and lista[1] == "11":
    print("Esta data não existe!!")
elif int(lista[2]) % 4 == 0:
        if lista[1] == 2 and lista[0] > 29:
            print("Esta data não existe!!")
elif lista[1] == "2" and lista[0] > "28":
    print("Esta data não existe!!")
elif lista[2] < "0" or lista[2] > "2021" or lista[1] > "12":
    print("Esta data não existe!!")
else: 
    print("Esta data Existe!!")


