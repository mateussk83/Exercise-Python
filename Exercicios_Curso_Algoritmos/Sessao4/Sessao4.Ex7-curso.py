"""
Sua organização acaba de contratar um estagiario para trabalhar no Suporte de informatica, com a intenção 
de fazer um levantamento nas sucatas encontradas nesta area. A primeira tarefa dele é testar todos os cercas
de 200 mouses que se encontra la, testando e anotando o estado de cada um deles, para verificar oq se pode
aproveitar deles.
Foi requisitado que você desenvolva um programa para registrar este levantamento. O programa devera receber
um numero indeterminado de entradas, cada um contendo: um numero  de itentificação do mouse do tipo de defeito
- necessita de esfera:
- necessita de limpeza:
- necessita de troca do cabo ou conector:
- quebrado ou inutilizado:

Uma identificação igual a zero encerra o programa. Ao final o programa devera emitir o seguinte relatorio:
Quantidade de mouse: x

Situação                                   Quantidade Percentual 
- necessita de esfera:                          x         x
- necessita de limpeza:                         x         x             
- necessita de troca do cabo ou conector:       x         x
- quebrado ou inutilizado:                      x         x
"""
"""
esfera = 0
limpeza = 0
cabo_ou_conector = 0
inutilizado = 0
quantidade = 0
perc_esfera = 0
perc_limpeza = 0
perc_cabo_ou_conector = 0
perc_inutilizado = 0
escrever "identifique o defeito"
escrever "1 - Necessita de esfera"
escrever "2 - Necessita de limpeza"
escrever "3 - Necessita de troca do cabo ou conector"
escrever "4 - quebrado ou inutilizado"
receber defeito
se defeito for igual a 1 entao 
    necessita_esfera = necessita_esfera + 1
se defeito for igual a 2 entao
    necessita_limpeza = necessita_limpezza + 1
se defeito for igual a 3 entao
    necessita_troca_cabo = necessita_troca_cabo + 1
se defeito for igual a 4 entao
    quebrado = quebrado + 1 
quantidade = quantidade + 1
perc_esfera = (necessita_esfera * 100) / quantidade
perc_limpeza = (necessita_limpeza * 100) / quantidade
perc_troca_cabo = (necessita_troca_cabo * 100) / quantidade
perc_quebrado = (quebrado * 100) / quantidade
escrever "Quantidade de mouse" + quantidade
escrever "situação  quantidade percentual"
escrever " 1 - Necessita de esfera " + necessita_esfera + perc_esfera 
escrever " 2 - Necessita de limpeza" + necessita_limpeza + perc_limpeza
escrever " 3 - Necessita de troca do cabo ou conector" + necessita_troca_cabo + perc_troca_cabo
escrever " 4 - quebrado ou inutilizado" + quebrado + perc_quebrado
"""  
#Variaveis
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





