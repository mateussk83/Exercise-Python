import math

a = float(input("Informe o valor A: "))
b = float(input("Informe o valor B: "))
c = float(input("Informe o valor C: "))

if a == 0:
    print("Isto não é uma equação de segundo grau")
else:
    b = int( input('Coeficiente b: ') )
    c = int( input('Coeficiente c: ') )
    delta = b * b - (4 * a * c)
    if delta < 0:
        print("Delta menor que 0. Raízes inexistente.")
    elif delta == 0:
        raiz = -b / (2 * a)
        print("Delta é 0 , raiz: {0}".format(raiz))
    else:
        raiz1 = (-b + math.sqrt(delta) ) / (2 * a)
        raiz2 = (-b - math.sqrt(delta) ) / (2 * a)
        print("Raizes: {0} e {1}".format(raiz1,raiz2))