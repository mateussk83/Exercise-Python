nomes = []
megas = []
with open('usuarios.txt','r') as arquivo:
    for valor in arquivo:
        valores = valor.split()
        nomes.append(valores[0])
        kilo = int(valores[1]) / 1024
        mega = kilo / 1024
        megas.append(mega)
arquivo.close()
def percentual_num(numero_perc,total_numero):
    x = (100*numero_perc) / total_numero
    return(x)

media = sum(megas) / len(megas)
with open('relatorio.txt','w') as relatorio:
    relatorio.write("ACME Inc.          Uso do espaco em disco pelos usuários\n")
    relatorio.write("---------------------------------------------------------------------\n")
    relatorio.write("Nr.    Usuario          Espaco utilizado       % do uso\n\n")
    for n in range(0,6):
        relatorio.write("{0:<3}    {1:<9} {2:>14.2f} MB {3:>18.2f} %\n".format(n + 1,nomes[n],megas[n],percentual_num(sum(megas),megas[n])))
    relatorio.write("\nEspaco total ocupado: {0:.2f} MB\n".format(sum(megas)))
    relatorio.write("Espaco medio ocupado: {0:.2f} MB".format(media))
relatorio.close()