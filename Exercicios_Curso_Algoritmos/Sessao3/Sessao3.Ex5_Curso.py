#variaveis
e = 0
m = 0

#Entradas
peso_peixe = float(input("Informe o peso do peixe: "))

#processamentos
if peso_peixe > 50:
    e = peso_peixe - 50
    m = e * 4
    print("Excesso: {0}".format(e))
    print("Peso: {0}".format(peso_peixe))
    print("Multa: R${0: .2f}".format(m))
else:
    print("Excesso: {0}".format(e))
    print("Peso: {0}".format(peso_peixe))
    print("Multa: R${0: .2f}".format(m))