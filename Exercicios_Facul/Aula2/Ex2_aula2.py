"""
Faça um algoritmo que peça a prova 1 e prova 2 e faça a media das duas provas, 
e informe se o aluno foi aprovado ou reprovado.
OBS: a media da escola é 5.
"""


prova1 = float(input("Informe o valor da primeira prova: "))
prova2 = float(input("Informe o valor da segunda prova: "))

media = (prova1 + prova2) / 2

if media <= 5:
    print("Aluno reprovado")
    print("Media {0}".format(media))
if media >= 5:
    print("Aluno aprovado")
    print("Media {0}".format(media))