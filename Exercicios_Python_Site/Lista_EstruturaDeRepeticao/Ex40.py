codigos = []
veiculos = []
acidentes = []
cont = 5
for n in range(1,6):
    codigo = input("Informe o codigo da {0}ª cidade: ".format(n))
    veiculo = int(input("Informe o número de veículos em sua cidade(em 1999): "))
    acidente = int(input("Informe o número de acidentes de trânsito com vítimas(em 1999): "))
    codigos.append(codigo)
    veiculos.append(veiculo)
    acidentes.append(acidente)


menor_acidente = acidentes.index(min(acidentes)) 
maior_acidente = acidentes.index(max(acidentes)) 
print("O código da cidade com o maior indice de acidentes é {0} com {1} acidentes".format(codigos[maior_acidente],acidentes[maior_acidente]))
print("O código da cidade com o menor indice de acidentes é {0} com {1} acidentes".format(codigos[menor_acidente],acidentes[menor_acidente]))

media = sum(veiculos) / cont

print("A média de veículos das cinco cidades juntas é: {0:.2f}".format(media))


for veiculo in veiculos:
    if veiculo < 2000:
        veiculos.remove(veiculo)
        cont = cont - 1

media_2000 = sum(veiculos) / cont
print("A média de veículos com menos de 2000 veículos é: {0} ".format(media_2000))



