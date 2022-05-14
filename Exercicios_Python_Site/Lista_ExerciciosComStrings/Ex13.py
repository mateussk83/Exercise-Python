import random
arquivo = open("arquivo.txt","r")
lista = []
vida = 0
listaPalavra = []
p = []

for linha in arquivo:
    linha = linha[:-1]
    lista.append(linha.lower())

palavra = lista[random.randrange(0,len(lista))]
listaPalavra = list(palavra)
random.shuffle(listaPalavra)
palavra_embaralhada = "".join(listaPalavra)
print("A palavra é: {0}".format(palavra_embaralhada))
resposta = input("Informe a palavra Desembaralhada: ")

while resposta != palavra and vida < 6:
    if resposta != palavra:
        vida = vida + 1
        print("Você errou pela {0}ª vez. Tente novamente!!".format(vida))
    if resposta == palavra:
        break
    if vida == 6:
        break
    resposta = input("Informe a palavra Desembaralhada: ")
if resposta == palavra:
    print("Parabens você ganhou o jogo!!")
    print("A palavra era {0}".format(palavra))
if vida == 6:
    print("Infelizmente você perdeu o jogo!!")
    print("A palavra era {0}".format(palavra))