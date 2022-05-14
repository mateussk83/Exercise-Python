print("Para finalizar o programa informe uma idade negativa!!")
idade = int(input("Informe a 1ª idade: "))
numeros = [0]
n = 0
media = 0
while idade > 0:
    n = n + 1
    numeros.append(idade)
    idade = int(input("Informe a {0}ª idade:  ".format(len(numeros))))

media = sum(numeros) / n
print("A média das idades digitados é: {0:.2f}".format(media))
if media > 0 and media <= 25:
    print("Pertence ao grupo Jovem!!")
if media > 25 and media <= 60:
    print("Pertence ao grupo Adulto!!")
if media > 60: 
    print("Pertence ao grupo Idoso!!")

