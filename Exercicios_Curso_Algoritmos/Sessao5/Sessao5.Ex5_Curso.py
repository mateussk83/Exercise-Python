#variaveis
vetor = []
posicao = 0
tem_maior_50 = False

#Entradas
for n in range (1, 11):
    num = int(input("Informe os valores para o vetor:"))
    vetor.append(num)
for n in vetor:
    if num >= 50:
        print("O numero {0} estara na posição {1} do vetor".format(n, posicao))
        tem_maior_50 = True
    posicao = posicao + 1
if tem_maior_50 == False:
    print("N existe nenhum numero maior que 50!!")