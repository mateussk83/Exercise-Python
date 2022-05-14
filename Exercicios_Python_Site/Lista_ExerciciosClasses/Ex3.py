class Retangulo :

    area = 0
    def __init__(self,comprimento,altura):
        self.__comprimento = comprimento
        self.__altura = altura
        Retangulo.area = self.__altura * self.__comprimento

    def alterar_lado(self): 

        resposta = input("Deseja modificar a altura ou comprimento: ")

        if resposta.lower() == "altura":
            altura = float(input("Informe a altura em centímetros: "))
            self.__altura = altura
        elif resposta.lower() == "comprimento":
            comprimento = float(input("Informe o comprimento em cm: "))
            self.__comprimento = comprimento

    def mostrar_valores(self):
        print("A altura do retângulo é {0}".format(Retangulo.altura))
        print("O comprimento do retângulo é {0}".format(Retangulo.comprimento))
        area = Retangulo.altura * Retangulo.comprimento
        print("A área do retângulo é: {0}".format(area))
        perimetro = (Retangulo.altura * 2) + (Retangulo.comprimento * 2)
        print("O perímetro do retângulo é:{0}".format(perimetro))

    def cacular_piso(self):
        comprimento_piso = float(input("informe o comprimento do piso(em metros): "))
        altura_piso = float(input("informe a altura do piso(em metros): "))
        tamanho_rodape = float(input("Informe o tamanho do roda-pé(em metros): "))
        metro_piso = comprimento_piso * altura_piso
        metros_rodape = (tamanho_rodape * self.__comprimento) + (tamanho_rodape * self.__altura) * 2
        print("A quantidade de pisos necessarias é: {0}".format(int((Retangulo.area / metro_piso) * 1.10)))
        print("A quantidade de roda-pé necessarios é: {0}".format(int((Retangulo.area / metros_rodape) * 1.10)))

comprimento = float(input("Informe o comprimento do local: "))
altura = float(input("Informe a altura do local: "))

casa1 = Retangulo(comprimento, altura)


Retangulo.cacular_piso(casa1)