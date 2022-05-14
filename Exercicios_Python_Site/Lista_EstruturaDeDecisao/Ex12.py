"""
Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto, mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os descontos. O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
Desconto do IR:
Salário Bruto até 900 (inclusive) - isento
Salário Bruto até 1500 (inclusive) - desconto de 5%
Salário Bruto até 2500 (inclusive) - desconto de 10%
Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, dispostas conforme o exemplo abaixo. No exemplo o valor da hora é 5 e a quantidade de hora é 220.
"""
numero_hora = int(input("Informe o número de horas trabalhadas: "))
valor_hora = float(input("Informe o valor da hora trabalhada: "))

salario_bruto = valor_hora * numero_hora

if salario_bruto <= 900:
    empresa = 0
    IR = salario_bruto *0.05
    INSS = salario_bruto * 0.10
    FGTS = salario_bruto * 0.11
if salario_bruto > 900 and salario_bruto <= 1500:
    empresa = 0.05
    IR = salario_bruto * 0.05
    INSS = salario_bruto * 0.10
    FGTS = salario_bruto * 0.11
if salario_bruto > 1500 and salario_bruto <= 2500:
    empresa = 0.10
    IR = salario_bruto * 0.05
    INSS = salario_bruto * 0.10
    FGTS = salario_bruto * 0.11
if salario_bruto > 2500:
    empresa = 0.20
    IR = salario_bruto * 0.05
    INSS = salario_bruto * 0.10
    FGTS = salario_bruto * 0.11

desconto = salario_bruto * empresa
desconto_total = IR + INSS + desconto
salario_liquido = salario_bruto - desconto_total

print("Salário Bruto: ({0} * {1})       : R$ {2:.2f} ".format(numero_hora,valor_hora,salario_bruto))
print("(-) IR (5%)                      : R$ {0:.2f}".format(IR))
print("(-) INSS (10%)                   : R$ {0:.2f}".format(INSS))
print("(-) desconto ({0}%)              : R$ {1:.2f}".format(empresa*100, desconto))
print("FGTS (11%)                       : R$ {0:.2f}".format(FGTS))
print("Total de descontos               : R$ {0:.2f}".format(desconto_total))
print("Salário Liquido                  : R${0:.2f}".format(salario_liquido))
