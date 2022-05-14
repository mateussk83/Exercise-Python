"""
As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o programa que calculará os reajustes.
Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
salários até R$ 280,00 (incluindo) : aumento de 20%
salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
o salário antes do reajuste;
o percentual de aumento aplicado;
o valor do aumento;
o novo salário, após o aumento.
"""
salarioAntigo = float(input("Informe o seu salário para o reajuste: "))
percentual = 0
if salarioAntigo < 281.00:
    percentual = 0.20
    aumento = salarioAntigo * percentual
elif salarioAntigo > 280.00 and salarioAntigo < 701.00:
    percentual = 0.15
    aumento = salarioAntigo * percentual
elif salarioAntigo > 700.00 and salarioAntigo < 1500.00:
    percentual = 0.10
    aumento = salarioAntigo * percentual
elif salarioAntigo > 1499:
    percentual = 0.05
    aumento = salarioAntigo * percentual

salario = aumento + salarioAntigo

print("O salario antes do reajuste: R${0}".format(salarioAntigo))
print("O percentual a receber no salario: {0}%".format(percentual * 100))
print("O aumento do valor: R${0}".format(aumento))
print("O novo salário após o aumento: R${0}".format(salario))



