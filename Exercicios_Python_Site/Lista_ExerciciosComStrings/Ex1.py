string1 = input("Informe a primeira frase: ")
string2 = input("Informe a segunda frase: ")


print("Compara duas strings")
print("String 1: {0}".format(string1))
print("String 2: {0}".format(string2))
print('Tamanho de "{0}": {1} caracteres'.format(string1,len(string1)))
print('Tamanho de "{0}": {1} caracteres'.format(string2,len(string2)))

if len(string1) == len(string2):
    print("As duas strings são do mesmo tamanho.")
else:
    print("As duas strings são de tamanho diferentes.")
if string1 == string2:
    print("As duas strings possuem o mesmo conteúdo.")
else:
    print("As duas strings possuem conteúdo diferente.")
