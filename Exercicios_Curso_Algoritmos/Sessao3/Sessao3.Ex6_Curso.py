#entradas
c = int(input("Informe o Codigo do funcionario: "))
horas_trabalhadas = int(input("Informe as horas trabalhadas do funcionario: "))

#processamentos
if horas_trabalhadas > 50:
    salario_extra = float((horas_trabalhadas - 50) * 20)
    salario = float((50 * 10) + salario_extra)
    print("Salario: R${0: .2f}".format(salario))
    print("Salario_extra: R${0: .2f}".format(salario_extra))
else:
    salario = float(horas_trabalhadas * 10)
    salario_extra = 0
    print("Salario: R${0: .2f}".format(salario))
    print("Salario_extra: R${0: .2f}".format(salario_extra))