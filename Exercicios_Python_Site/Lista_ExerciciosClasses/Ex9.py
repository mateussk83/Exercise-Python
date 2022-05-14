class Ponto:

    def __init__(self,x, y):
        self.x = x
        self.y = y

    def imprimirPonto(self):
        return "x: {0}\ny: {1}".format(self.x,self.y)


class Retangulo:

    def __init__(self,largura,altura):
        self.__largura = largura
        self.__altura = altura

    def calcularCentro(self):
        x_centro = (self.__altura.x + self.__altura.x) / 2
        y_centro = (self.__largura.x + self.__largura.y) / 2
        return "O centro do retangulo é: {0} altura e {1} largura\n".format(x_centro, y_centro)

    def alterarAltura(self,altura):
        self.__altura = altura

    def alterarLargura(self,largura):
        self.__largura = largura

altura1 = int(input("Informe o primeiro ponto da altura: ")) 
altura2 = int(input("Informe o segundo ponto da altura: \n"))

altura = Ponto(altura1,altura2)

largura1 = int(input("Informe o primeiro ponto da largura: "))
largura2 = int(input("Informe o segundo ponto da largura: \n"))

largura = Ponto(largura1,largura2)

retangulo = Retangulo(altura,largura)

saida = "n"
while saida != "s":
    print(Retangulo.calcularCentro(retangulo))
    
    resposta = input("Deseja modificar a altura[s/n]: ")
    if resposta.lower() == "s":
        altura1 = int(input("Informe o primeiro ponto da altura: ")) 
        altura2 = int(input("Informe o segundo ponto da altura: \n"))

        Retangulo.alterarAltura(retangulo,Ponto(altura1,altura2))
    
    resposta = input("Deseja modificar a largura[s/n]: ")
    if resposta.lower() == "s":
        largura1 = int(input("Informe o primeiro ponto da largura: "))
        largura2 = int(input("Informe o segundo ponto da largura: \n"))
        Retangulo.alterarAltura(retangulo,Ponto(largura1,largura2))
    
    saida = input("Deseja finalizar o Programa[s/n]: \n")

print("Obrigado por Usar o Programa!!!!")