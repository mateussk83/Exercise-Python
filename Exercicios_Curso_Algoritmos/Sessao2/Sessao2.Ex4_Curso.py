#entradas
horas_trabalhadas = int(input("Informe a quantidade de horas trabalhadas: "))
valor_hora = int(input("Informe o valor da hora trabalhada: "))

#processamentos
salario = valor_hora * horas_trabalhadas

#saidas
print("O seu salario é: R${0}".format(salario))
