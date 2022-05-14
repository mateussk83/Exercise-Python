soma = 0

for n in range(1,11):
    num = int(input("Informe o {0}º numero:".format(n)))
    soma = soma + num
media = soma / 10
print("A media da soma dos numeros é:{0}".format(media))