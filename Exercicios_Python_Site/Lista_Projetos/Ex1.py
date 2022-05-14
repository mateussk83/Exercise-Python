nomes = []
megas = []

usuarios = open("usuarios.txt","w")
usuarios.write("alexandre       456123789\n")
usuarios.write("anderson        1245698456\n")
usuarios.write("antonio         123456456\n")
usuarios.write("carlos          91257581\n")
usuarios.write("cesar           987458\n")
usuarios.write("rosemary        789456125\n")

usuarios.close()


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
megas = sorted(megas)
megas.reverse()
media = sum(megas) / len(megas)
with open('relatorio.txt','w') as relatorio:
    relatorio.write("ACME Inc.          Uso do espaco em disco pelos usuários\n")
    relatorio.write("---------------------------------------------------------------------\n")
    relatorio.write("Nr.    Usuario          Espaco utilizado       % do uso\n\n")
    for n in range(0,6):
        relatorio.write("{0:<3}    {1:<9} {2:>14.2f} MB {3:>18.2f} %\n".format(n + 1,nomes[n],megas[n],percentual_num(megas[n],sum(megas))))
    relatorio.write("\nEspaco total ocupado: {0:.2f} MB\n".format(sum(megas)))
    relatorio.write("Espaco medio ocupado: {0:.2f} MB".format(media))
relatorio.close()