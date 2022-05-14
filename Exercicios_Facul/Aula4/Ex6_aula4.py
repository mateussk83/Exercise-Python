"""
Faça um programa que receba a temperatura média de cada mês do ano, e depois calcule a media do ano inteiro.
"""
temperaturas_anos = []
media_final = 0
media_janeiro = 0
media_fevereiro = 0
media_marco = 0
media_abril = 0
media_maio = 0
media_junho = 0
media_julho = 0
media_setembro = 0
media_outubro = 0
media_novembro = 0
media_dezembro = 0

for n in range(0,12):
    mes_ano = int(input("informe o mês(1,2,3...):"))
    if mes_ano == 1:
        media_janeiro = float(input("Informe a média da temperatura do mês de janeiro:"))
        Media_final = media_final + media_janeiro
    if mes_ano == 2:
        media_fevereiro = float(input("Informe a média do mês de Fevereiro:"))
        media_final = media_final + media_fevereiro
    if mes_ano == 3:
        media_marco = float(input("Informe a média do mês de Março:"))
        media_final = media_final + media_marco
    if mes_ano == 4:
        media_abril = float(input("Informe a média do mês de Abril:"))
        media_final = media_final + media_abril
    if mes_ano == 5:
        media_maio = float(input("Informe a média do mês de Maio:"))
        media_final = media_final + media_maio
    if mes_ano == 6:
        media_junho = float(input("Informe a média do mês de Junho:"))
        media_final = media_final + media_junho
    if mes_ano == 7:
        media_julho = float(input("Informe a média do mês de Julho:"))
        media_final = media_final + media_julho
    if mes_ano == 8:
        media_agosto = float(input("Informe a média do mês de Agosto:"))
        media_final = media_final + media_agosto
    if mes_ano == 9:
        media_setembro = float(input("Informe a média do mês de Setembro:"))
        media_final = media_final + media_setembro
    if mes_ano == 10:
        media_outubro = float(input("Informe a média do mês de Outubro:"))
        media_final = media_final + media_outubro
    if mes_ano == 11:
        media_novembro= float(input("Informe a média do mês de Novembro:"))
        media_final = media_final + media_novembro
    if mes_ano == 12:
        media_dezembro = float(input("Informe a média do mês de Dezembro:"))
        media_final = media_final + media_dezembro
media_final = media_final / 12
print("A média do mês de janeiro é {0}".format(media_janeiro))
print("A média do mês de fevereiro é {0}".format(media_fevereiro))
print("A média do mês de março é {0}".format(media_marco))
print("A média do mês de abril é {0}".format(media_abril))
print("A média do mês de maio é {0}".format(media_maio))
print("A média do mês de junho é {0}".format(media_junho))
print("A média do mês de julho é {0}".format(media_julho))
print("A média do mês de agosto é {0}".format(media_agosto))
print("A média do mês de setembro é {0}".format(media_setembro))
print("A média do mês de outubro é {0}".format(media_outubro))
print("A média do mês de novembro é {0}".format(media_novembro))
print("A média do mês de dezembro é {0}".format(media_dezembro))
print("A média geral é {0}".format(media_final))