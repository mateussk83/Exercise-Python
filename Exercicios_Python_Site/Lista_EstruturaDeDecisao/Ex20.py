nota1 = float(input("Informe a primeira nota: "))
nota2 = float(input("Informe a segunda nota: "))
nota3 = float(input("Informe a terceira nota: "))

media = (nota1 + nota2 + nota3) / 3

if media >=7 and media <= 9.9:
    print("Aprovado!!")
    print("Media {0}".format(media))
elif media == 10 :
    print("Aprovado com Distinção!!")
    print("Media {0}".format(media))
elif media < 7:
    print("Reprovado!!")
    print("Media {0}".format(media))
else:
    print("Informe as notas de 1 a 10")