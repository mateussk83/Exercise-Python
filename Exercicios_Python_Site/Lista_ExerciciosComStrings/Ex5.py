nome = input("Informe um nome: ")
lista = []
palavra=""
for n in nome:
    palavra = palavra + n 
    lista.append(palavra)

for n in range(len(nome) - 1,-1,-1):
    print(lista[n])