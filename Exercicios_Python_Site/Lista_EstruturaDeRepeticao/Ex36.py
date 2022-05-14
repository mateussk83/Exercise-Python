tabuada = int(input("Informe o número para montar a tabuada: "))
comecar = int(input("Informe o número que irá a tabuada: "))
terminar = int(input("Informe o número que irá terminar a tabuada: "))
print("Montar a tabuada de: {0}".format(tabuada))
print("Começar por: {0}".format(comecar))
print("Terminar por: {0}".format(terminar))
print("\nVou montar a tabuade de {0} começando em {1} e terminando em {2}:".format(tabuada,comecar,terminar))
for n in range(comecar, terminar + 1):
    print("{0} X {1} = {2}".format(tabuada,n,n*tabuada))