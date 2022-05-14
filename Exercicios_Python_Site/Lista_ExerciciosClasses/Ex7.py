class BichinhoVirtual:

    def __init__(self,nome,fome,saude,idade):
        self.__nome = nome
        self.__fome = fome
        self.__saude = saude
        self.__idade = idade

    def alterarNome(self, nome):
        self.__nome = nome
    
    def alterarFome(self, fome):
        while fome < 0 or fome > 100:
            print("Informe um valor para fome dentro de 0 a 100")
            fome = int(input("Informe novamente o valor: "))
        self.__fome = fome

    def alterarSaude(self, saude):
        while fome < 0 or fome > 100:
            print("Informe um valor para saude dentro de 0 a 100")
            fome = int(input("Informe novamente o valor: "))
        self.__saude = saude
    
    def alterarIdade(self, idade):
        self.__idade = idade

    def mostrarStatus(self):

        return "!!Bichinho Online!!\nNome: {0}\nFome: {1}\nSaúde: {2}\nIdade: {3}\nHumor: {4}".format(self.__nome,self.__fome,self.__saude,self.__idade,(self.__saude + self.__fome) / 2 )


bichinho1 = BichinhoVirtual("Maggie", 80, 90, 80)

print(BichinhoVirtual.mostrarStatus(bichinho1))