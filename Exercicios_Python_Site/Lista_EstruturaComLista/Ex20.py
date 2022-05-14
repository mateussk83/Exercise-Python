salarios = []
abonos = []
salario = 1
abono_minimo = 0
while salario != 0:
    salario = float(input("Informe o sálario atual para o abono: R$"))
    if salario <= 0:
        break
    salarios.append(salario)
    abono = salario * 0.20
    if abono < 100:
        abono = 100
        abono_minimo = abono_minimo + 1
    abonos.append(abono)
x = 0
print("Projeção de Gastos com Abono")
print("============================\n")
for salario in salarios:
    print("Salário: {0}".format(salario))
print("Salário      - Abono")
for salario in salarios:
    print("R$ {0:<9} - R$ {1:}".format(salarios[x], abonos[x]))
    x = x + 1
print("Foram processados {0} colaboradores".format(len(salarios)))
print("Total gasto com abonos: R${0:.2f}".format(sum(abonos)))
print("Valor minimo pago a {0} calaboradores".format(abono_minimo))
print("Maior valor de abono pago: R${0:.2f}".format(max(abonos)))



