nota1 = float(input("Informe a primeira nota:"))
nota2 = float(input("Informe a segunda nota: "))

media = (nota1 + nota2) / 2

if media <= 4.0:
    conceito = "E"
    mensagem = "Reprovado"
if media > 4.0 and media <= 6.0:
    conceito = "D"
    mensagem = "Reprovado"
if media > 6.0 and media <= 7.5:
    conceito = "C"
    mensagem = "Aprovado"
if media > 7.5 and media <= 9.0:
    conceito = "B"
    mensagem = "Aprovado"
if media > 9.0:
    conceito = "A"
    mensagem = "Aprovado"
print("A media do aluno é: {0}".format(media))
print("O aluno esta no conceito: {0}".format(conceito))
if mensagem == "Aprovado":
    print("Parabéns Você foi aprovado!!")
if mensagem == "Reprovado":
    print("Infelizmente você foi reprovado!!")