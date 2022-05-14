class Carro:

    def __init__(self, consumoCombustivel):
        self.__quantidadeCombustivel = 0
        self.__consumo = consumoCombustivel


    def andar(self, distancia):
        self.__quantidadeCombustivel = self.__quantidadeCombustivel - (distancia / self.__consumo)
    
    def obterGasolina(self):
        return "Quantidade de gasolina: {0:.2f}".format(self.__quantidadeCombustivel)

    def adicionarGasolina(self,combustivel):
        self.__quantidadeCombustivel = self.__quantidadeCombustivel + combustivel


meuFusca = Carro(15)

meuFusca.adicionarGasolina(20)

meuFusca.andar(100)

print(meuFusca.obterGasolina())