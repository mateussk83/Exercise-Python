import random

palavra = input("Informe a palavra para embaralhar: ")

palavra = list(palavra)

def embaralhar(palavra):
    resposta = random.sample(palavra,len(palavra))
    resposta = "".join(resposta)
    return(resposta)

print(embaralhar(palavra))