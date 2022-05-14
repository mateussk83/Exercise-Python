frase_1 = input("Informe a primeira frase: ")
frase_2 = input("Informe a segunda frase")

print("Comparando as duas strings")
print("Frase 1: {0} : {1} caracteres".format(frase_1, len(frase_1)))
print("Frase 2: {0} : {1} caracteres".format(frase_2, len(frase_2)))
if len(frase_1) != len(frase_2):
    print("As duas frases são de tamanhos diferentes!")
else:
    print("As duas frases são iguais!")