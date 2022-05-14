caracteres = []
consoantes = []
for n in range(1,11):
    caracter = input("Informe o {0} caracter: ".format(n))
    caracteres.append(caracter)
for caracter in caracteres:
    if caracter != "a" and caracter != "e" and caracter != "i" and caracter != "o" and caracter != "u":
         consoantes.append(caracter)

print("As Concoantes foi: {0}".format(consoantes))