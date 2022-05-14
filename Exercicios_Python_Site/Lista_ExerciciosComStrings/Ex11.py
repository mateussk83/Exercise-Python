import random
arquivo = open("arquivo.txt","r")
lista = []
erro = 1
vida = 0
certo = 0
valor = 0

lista_palavra = []
for linha in arquivo:
    linha = linha[:-1]
    lista.append(linha.lower())
palavra = lista[random.randrange(0,len(lista))]
resposta = 1
escondido = " _" * len(palavra)

letra = input("Digite uma letra: ")
while resposta != len(palavra) and vida < 6:
    for caracter in palavra:
        if letra == caracter:
            numero = palavra.index(caracter)
            lista_palavra = escondido.split(" ")
            lista_palavra[numero + 1] = caracter
            escondido = " ".join(lista_palavra)
            resposta = resposta + 1
            if resposta == len(palavra):
                break
    if valor == resposta:
        vida = vida + 1
        print("Você errou pela {0}ª vez. Tente novamente!!".format(vida))
        if vida == 6:
            break
    print("A palavra é {0}".format(escondido))
    letra = input("Digite uma letra: ")
    valor = resposta
if resposta == len(palavra):
    print("Você Ganhou o Jogo!!")
    print("A palavra era: {0}".format(palavra))
elif vida == 6:
    print("Você Perdeu o Jogo!!")
    print("A palavra era: {0}".format(palavra))


