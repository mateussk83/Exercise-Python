num = int(input("Informe o número: "))
def positivo_negativo(num):
    if num <= 0:
        return("N")
    else:
        return("P")

print(positivo_negativo(num))