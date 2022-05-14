frase = input("Informe a frase: ")

contEspacos = 0
contVogal = 0

for letra in frase:
    if letra == " ":
        contEspacos = contEspacos + 1
    elif letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u":
        contVogal = contVogal + 1
print("Frase:{0}".format(frase))
print("Sua frase tem {0} espaços!!".format(contEspacos))
print("Sua frase tem {0} vogais!!".format(contVogal))