print("Responda com SIM ou NAO!!")
pergunta1 = input("Telefonou para a vítima?")
pergunta2 = input("Esteve no local do crime?")
pergunta3 = input("Mora perto da vítima?")
pergunta4 = input("Devia para a vítima?")
pergunta5 = input("Já trabalhou com a vítima?")

indice = 0
if pergunta1.lower() == "sim":
    indice = indice + 1 
if pergunta2.lower() == "sim":
    indice = indice + 1 
if pergunta3.lower() == "sim":
    indice = indice + 1 
if pergunta4.lower() == "sim":
    indice = indice + 1 
if pergunta5.lower() == "sim":
    indice = indice + 1 
if indice == 2:
    print("A pessoa é Suspeita!!")
if indice == 3 or indice == 4:
    print("A pessoa é Cúmplice!!")
if indice == 5:
    print("A pessoa é Assassina!!")
elif indice != 2 and indice != 3 and indice != 4 and indice != 5:
    print("A pessoa é Inocente")

