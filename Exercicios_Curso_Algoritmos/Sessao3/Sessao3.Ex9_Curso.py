#entradas
poluicao = float(input("Informe o nivel de poluição: "))

#processamentos
if poluicao >= 0.3 and poluicao < 0.4:
    print("Grupo 1 suspender as atividades!") 
elif poluicao >= 0.4 and poluicao < 0.5:
    print("Grupo 1 e Grupo 2 suspender as atividades!")
elif poluicao >= 0.5:
    print("Todos os grupos suspender as atividades!")
else:
    print("grupos aceitaveis")