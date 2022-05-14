import random

def lancar_dado():
    return(random.randrange(1,7))
jogar = "sim"
x = 1
while jogar == "sim":
    while x == 1:
        lancamento = lancar_dado() + lancar_dado()
        print("lançamento: {0}".format(lancamento))
        if lancamento ==7 or lancamento == 11:
            print("Você é um natural e venceu!!!")
            break
        elif lancamento == 2 or lancamento == 3 or lancamento == 12:
            print("Você é um craps e perdeu!!!")
            break
        elif lancamento == 4 or lancamento == 5 or lancamento == 6 or lancamento == 8 or lancamento == 9 or lancamento == 10:
            print("Você é um ponto continue a jogar")
            meta = lancamento 
            while lancamento != 7:
                lancamento = lancar_dado() + lancar_dado()
                print("lançamento: {0}".format(lancamento))
                if meta == lancamento:
                    print("Parabéns você tirou o número: {0} de novo então você ganhou!!!!".format(meta))
                    break
                elif lancamento == 7:
                    print("Você tirou um 7 e perdeu!!!")
                    break
            break
    print("Responda com sim ou nao:")
    jogar = input("Deseja jogar novamente: ")


