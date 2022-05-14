"""
"Faça um programa que pede tres notas de um aluno. Em seguida ele deve calcular a média do aluno e dar o seguinte resultado:  
A mensagem "Aprovado", se a média alcançada for maior ou igual a sete; 
A mensagem "Reprovado", se a média for menor do que sete; 
A mensagem "Aprovado com Distinção", se a média for igual a dez.
"""

prova1 = float(input("Informe o valor da primeira prova: "))
prova2 = float(input("Informe o valor da segunda prova: "))
prova3 = float(input("Informe o valor da terceira prova: "))

media = (prova1 + prova2 + prova3) / 3

if media <= 7:
    print("Aluno reprovado")
    print("Media {0}".format(media))
if media >= 7:
    print("Aluno aprovado")
    print("Media {0}".format(media))
if media == 10:
    print("Aluno aprovado com Distinção")
    print("Media {0}".format(media))