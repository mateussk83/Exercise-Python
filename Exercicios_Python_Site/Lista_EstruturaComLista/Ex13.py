meses = ["Janeiro","Fevereiro","Março","Abril","Maio","Junho","Julho","Agosto","Setembro","Outubro","Novembro","Dezembro"]
temperaturas = []
temperaturas_acima = []

for n in range(0,12):
    temperatura = float(input("Informe a temperatura do mês de {0}: ".format(meses[n])))
    temperaturas.append(temperatura)

media = sum(temperaturas) / 12
cont = 0
cont1 = 0
for temperatura in temperaturas:
    if temperatura > media:
        cont1 = cont1 + 1
        temperaturaP = str(cont1) + " - " +meses[cont] +" : "+ str(temperatura)
        temperaturas_acima.append(temperaturaP)
    cont = cont + 1
print(temperaturas_acima)
sequencia = ' , '.join(temperaturas_acima)

print("Temperaturas Acima da média são: {0}".format(sequencia))
