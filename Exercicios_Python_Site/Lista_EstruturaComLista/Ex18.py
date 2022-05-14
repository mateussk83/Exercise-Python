votos = []
numero_votos = []
voto = int(input("Informe o 1º voto: "))
votos.append(voto)
x = 1
while voto != 0:
    x = x + 1
    voto = int(input("Informe o {0}º voto: ".format(x)))
    if voto > 0 and voto < 24:
        votos.append(voto)
    else:
        print("Infelizmente o camisa {0} não está na participação".format(voto))
        print("Informe um número entre 1 e 23 Por Favor!")
        voto = int(input("Informe o {0}º voto novamente:  ".format(x)))    
    
print("Total de Votos: {0}".format(len(votos)))

#FUNÇÂO
def percentual_num(numero_voto,total_voto):
    x = (100*numero_voto) / total_voto
    return(x)

for n in range(1,24):
    if votos.count(n) != 0:
        print("Numero {0}: {1:.2f} votos com {2:.2f}% dos votos".format(n,votos.count(n), percentual_num(votos.count(n),len(votos))))
    numero_votos.append(votos.count(n))
    if votos.count(n) == max(numero_votos):
        voto_maior = votos[n]
print("O número do jogador escolhido foi {0} com {1:.2f}% dos votos".format(voto_maior,percentual_num(max(numero_votos),len(votos))))