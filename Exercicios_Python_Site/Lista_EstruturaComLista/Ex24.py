import random

lancamentos = []
def lancar_dado():
    return(random.randrange(1,7))

for n in range(1,100):
    lancar = lancar_dado()
    lancamentos.append(lancar)

lado1 = lancamentos.index(1)
lado2 = lancamentos.index(2)
lado3 = lancamentos.index(3)
lado4 = lancamentos.index(4)
lado5 = lancamentos.index(5)
lado6 = lancamentos.index(6)

print("Lado1: {0}".format(lado1))
print("Lado2: {0}".format(lado2))
print("Lado3: {0}".format(lado3))
print("Lado4: {0}".format(lado4))
print("Lado5: {0}".format(lado5))
print("Lado6: {0}".format(lado6))



