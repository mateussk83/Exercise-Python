nota = float(input("Informe uma nota de 0 a 10: "))

while nota < 0 or nota > 10:
    print("Por favor informe um número valido!!")
    nota = int(input("Informe uma nota de 0 a 10: "))
    
print("Nota: {0:.1f}!!".format(nota))
    