"""
Faça um sistema que peça ao usuário o nome, slaario_fixo e a total de vendas, se o usuario informar qualquer valor sem ser numeros mostrar ao usuario "apenas numeros são aceitos."
"""
try:
    nome = input("Informe o nome: ")
    salario_fixo = float(input("Informe o seu salario fixo: "))
    total_vendas = float(input("Informe o total de vendas: "))

    salario_extra = total_vendas * 0.15
    salario_total = salario_extra + salario_fixo

    print("Nome: {0}".format(nome))
    print("Salario fixo: {0: .2f}".format(salario_fixo))
    print("Salario: {0: .2f}".format(salario_total))
except:
    print("apenas numeros sao aceitos")
