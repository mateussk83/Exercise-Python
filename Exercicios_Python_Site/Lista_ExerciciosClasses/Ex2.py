
class Quadrado:
    
    tamanho = 0

    def __init__(self,tamanho):
        self.__tamanho = tamanho

    def trocar_lado(self, tamanho):
        self.__tamanho = tamanho


    def calcular_area(self):
        print("O valor do lado é: {0}".format(self.__tamanho))
        return "A área do quadrado é: {0}".format(self.__tamanho * 2)


quadrado = Quadrado(4)

print(Quadrado.calcular_area(quadrado))
    
        
    

