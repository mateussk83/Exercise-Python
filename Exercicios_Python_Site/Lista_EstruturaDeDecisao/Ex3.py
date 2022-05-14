sexo = "sla"

while sexo.lower() != "m" or sexo.lower() != "f":
    sexo = input("informe o sexo: ")
    if sexo.lower() == "f":
        print("O sexo é Feminino!!")
        break
    if sexo.lower() == "m":
        print("O sexo é Masculino!!")
        break
    else:
        print("Sexo Invalido!!")
        sexo = input("informe o sexo: ")

