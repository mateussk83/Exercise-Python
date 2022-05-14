litro = 2.25
nomes = []
kms = []
km_litros = []
valor_km = []
for n in range(1,6):
    print("Veículo {0}".format(n))
    nome = input("Informe o nome do {0}º Veículo: ".format(n))
    nomes.append(nome)
    km = float(input("Informe quanto o carro anda com um litro de Gasolina: "))
    kms.append(km)
    km_por_litro = 1000 / km 
    km_litros.append(km_por_litro)
    gasto = km_por_litro * litro
    valor_km.append(gasto)
print("Relatório Final")

for n in range(1,6):
    print("{0} - {1:<2} - {2:<2} - {3:<6.2f} litros - R${4:.2f}".format(n,nomes[n - 1],kms[n - 1],km_litros[n - 1],valor_km[n - 1]))

index = km_litros.index(min(km_litros))
print("O menor consumo é do {0}".format(nomes[index]))
