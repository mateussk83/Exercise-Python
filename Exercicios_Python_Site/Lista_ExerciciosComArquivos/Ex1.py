listaIP = open("listaIP.txt","w")

listaIP.write("200.135.80.9\n192.168.1.1\n8.35.67.74\n257.32.4.5\n85.345.1.2\n1.2.3.4\n9.8.234.5\n192.168.0.256")

listaIP.close()
cont1 = 0
cont2 = 0

ipValido = []
contNegativo1 = 0
contNegativo2 = 0
ip = []
valida = ""
ipInvalido = []
arquivo = open("listaIP.txt","r")
valor = 0
valorAnterior = 0
for linha in arquivo:
    ip = linha.split(".")
    for n in range(0,3):
        if int(ip[n]) <= int(ip[n + 1]):
            cont1 = cont1 + 1
        if int(ip[n]) >= int(ip[n + 1]):
            cont2 = cont2 + 1
        if cont1 == 3 or cont2 == 3: 
            valida = ".".join(ip)
            ipValido.append(valida)
    if valida == "":
        ipInvalido.append(linha)
    valida = ""
    cont1 = 0
    cont2 = 0
    contNegativo1 = 0
    contNegativo2 = 0






relatorio = open("relatorio.txt","w")

relatorio.write("[Endereços válidos:]\n")
for valor in ipValido:
    relatorio.write(valor)
relatorio.write("\n")

relatorio.write("[Endereços inválidos:]\n")
for valor in ipInvalido:
    relatorio.write(valor)
relatorio.write("\n")

relatorio.close()