base = int(input("Informe a base da exponenciação:"))
expoente = int(input("Informe o expoente da exponenciação:"))

base2 = base * base
for n in range(1, expoente):
    base2 = base2 * base
print("O resultado da exponenciação é: {0}".format(base2))