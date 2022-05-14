"""
Escreva uma aplicação que encontre a media de consumo de um veiculo.
"""

distancia = float(input("Informe a distancia percorrida pelo automavel: "))
combustivel_gasto = float(input("Informe o combustivel gasto pelo automóvel"))

media = combustivel_gasto / distancia

print("A media de consumo é: {0}".format(media))