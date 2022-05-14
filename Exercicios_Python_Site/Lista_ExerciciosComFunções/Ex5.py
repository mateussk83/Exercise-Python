taxa = float(input("Informe em porcentagem a taxa do imposto: %"))
custo = float(input("Informe o valor do custo sobre a venda: "))
def somaImposto(taxaImposto, custo):
    custo = custo + (custo *(taxaImposto / 100))
    return(custo)

print(somaImposto(taxa,custo))
