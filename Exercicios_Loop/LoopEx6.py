soma = 0
for n in range(1,11):
    numero = int(input("Informe o {0}º numero: ".format(n)))
    while numero<0:
        print("Por favor insira um numero positivo")
        numero = int(input("Informe o {0}º numero: ".format(n)))
    else:
        soma = soma + numero
media = soma/10
print("A media dos numeros listados é :{0}".format(media))
