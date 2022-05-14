class Bomba:

    def __init__(self, valorLitro, tipoCombustivel,quantidadeCombustivel):
        self.__valorLitro = valorLitro
        self.__tipoCombustivel = tipoCombustivel
        self.__quantidadeCombustivel = quantidadeCombustivel
        self.__valorTotal = quantidadeCombustivel * valorLitro


    def abastecerPorValor(self,valorTotal):
        quantidade = valorTotal / self.__valorLitro
        self.__quantidadeCombustivel = self.__quantidadeCombustivel - quantidade
        return"A quantidade de combustivel posto no veiculo é: R${0:.2f}\nResta na bomba: {1} litros".format(self.__quantidadeCombustivel, self.__quantidadeCombustivel)
    
    def abastecerPorLitro(self,quantidadeCombustivel):
        self.__valorTotal = quantidadeCombustivel * self.__valorLitro
        self.__quantidadeCombustivel = self.__quantidadeCombustivel - quantidadeCombustivel
        return"O valor total a ser pago é: R${0:.2f}\nResta na bomba: {1} litros".format(self.__valorTotal,self.__quantidadeCombustivel)
    
    def alterarValor(self,valor):
        self.__valorLitro = valor
    
    def alterarCombustivel(self,tipo):
        self.__tipoCombustivel = tipo
    
    def alterarQuantidadeCombustivel(self,quantidade):
        self.__quantidadeCombustivel = quantidade



bomba1 = Bomba(1.95,"alcool",60)

print(Bomba.abastecerPorLitro(bomba1,30))