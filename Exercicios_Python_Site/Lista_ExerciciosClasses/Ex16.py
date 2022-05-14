class BichinhoVirtual:

    def __init__(self,nome,fome,saude,idade):
        self.__nome = nome
        self.__fome = fome
        self.__saude = saude
        self.__idade = idade
        self.__humor = (self.__saude + self.__fome) / 2

    def alterarNome(self, nome):
        self.__nome = nome

    def str(self):

        return "!!Bichinho Online!!\nNome: {0}\nFome: {1}\nSaúde: {2}\nIdade: {3}\nHumor: {4}\n".format(self.__nome,self.__fome,self.__saude,self.__idade,self.__humor )

    def brincar(self,quantidade):
        while quantidade < 0 or quantidade > 100:
            print("Informe um valor para saude dentro de 0 a 100")
            quantidade = int(input("Informe novamente o valor: "))
        self.__humor = self.__humor + quantidade
        if self.__humor > 99:
            self.__humor = 100
        self.__fome = self.__fome - (quantidade / 2)
    
    def comer(self,quantidade):
        while quantidade < 0 or quantidade > 100:
            print("Informe um valor para saude dentro de 0 a 100")
            quantidade = int(input("Informe novamente o valor: "))
        self.__fome = self.__fome + quantidade
        if self.__fome > 99:
            self.__fome = 100


bichinho1 = BichinhoVirtual("Maggie", 80, 90, 80)

bichinho1.comer(10)

bichinho1.brincar(5)

print(bichinho1.portaSecreta())
