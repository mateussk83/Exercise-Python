empresas = ["Windows Server","Unix","Linux","Netware","Mac OS","Outro"]
votos = []
numero_votos = []
voto = 1
x = 0
while voto != 0:
    x = x + 1
    voto = int(input("Informe o {0}º voto: ".format(x)))
    if voto > -1 and voto < 7:
        votos.append(voto)   
    else:
        print("Infelizmente Você informou um número inválido".format(voto))
        print("Informe um número entre 1 e 6 Por Favor!")
        voto = int(input("Informe o {0}º voto novamente:  ".format(x)))   

#FUNÇÂO
def percentual_num(numero_voto,total_voto):
    x = (100*numero_voto) / total_voto
    return(x)


print("Sistema Operacional      Votos     %")
print("-------------------      -----     ---")
for n in range(1,6):
    print("{0:<25}{1:<10}{2:.0f}% ".format(empresas[n],votos.count(n), percentual_num(votos.count(n),len(votos))))
    numero_votos.append(votos.count(n))
    if votos.count(n) == max(numero_votos):
        voto_maior = votos[n] - 1

        
print("-------------------      -----     ---")
print("Total                    {0}\n".format(len(votos)))

print("O Sistema Operacional mais votado foi o {0}, com {1} votos, correspondendo a {2:.2f}% dos votos.".format(empresas[voto_maior],max(numero_votos),percentual_num(max(numero_votos),len(votos))))