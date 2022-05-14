"""
Crie um programa que calcule a media de várias notas e a condição de parada será informar uma nota negativa.
"""
nota = float(input("Informe uma nota: "))
geral = 0
notas = [nota]
while nota >= 0:
    nota = float(input("Informe uma nota (para sair informe uma nota negativa): "))
    notas.append(nota)
    geral = geral + nota
media = geral / len(notas)
print("Media dos numeros é: {0}".format(media))

