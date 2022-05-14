esfera = 0
limpeza = 0
cabo_ou_conector = 0
inutilizado = 0
quantidade = 0
perc_esfera = 0
perc_limpeza = 0
perc_cabo_ou_conector = 0
perc_inutilizado = 0

#Entradas
identificador = int(input("Informe o codigo do mouse:"))
print("Tipos de defeitos:")
print("1 - Necessita de esfera")
print("2 - Necessita de limpeza")
print("3 - Necessita de troca do cabo ou conector")
print("4 - quebrado ou inutilizado")
defeito = int(input("Informe o defeito(1, 2, 3, 4):"))

while defeito != 0:
    if defeito == 1:
        esfera = esfera + 1
    elif defeito == 2:
        limpeza = limpeza + 1
    elif defeito == 3:
        cabo_ou_conector = cabo_ou_conector + 1
    elif defeito == 4:
        inutilizado = inutilizado + 1
    quantidade = quantidade + 1
    identificador = int(input("Informe o codigo do mouse:"))
    print("Tipos de defeitos:")
    print("1 - Necessita de esfera")
    print("2 - Necessita de limpeza")
    print("3 - Necessita de troca do cabo ou conector")
    print("4 - quebrado ou inutilizado")
    defeito = int(input("Informe o defeito(1, 2, 3, 4):"))
perc_esfera = esfera / quantidade * 100
perc_limpeza = limpeza / quantidade * 100
perc_cabo_ou_conector = cabo_ou_conector / quantidade * 100
perc_inutilizado = inutilizado / quantidade * 100

#saidas
print("Situação                                   Quantidade   Percentual")
print("1 - Necessita de esfera                        {0}          {1: .2f}%".format(esfera, perc_esfera))
print("2 - Necessita de limpeza                       {0}          {1: .2f}%".format(limpeza, perc_limpeza))
print("3 - Necessita de troca do cabo ou conector     {0}          {1: .2f}%".format(cabo_ou_conector, perc_cabo_ou_conector))
print("4 - quebrado ou inutilizado                    {0}          {1: .2f}%".format(inutilizado, perc_inutilizado))
