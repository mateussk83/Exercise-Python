salario_inicial = float(input("Informe o salario inicial: "))

ano = 1997
aumento = 0.015
salario = salario_inicial + (salario_inicial * aumento)
while ano < 2022:
    salario = salario + (salario * (aumento * 2))
    ano = ano + 1
print("O salário no ano de 2021 é de: R${0:.2f}".format(salario))

