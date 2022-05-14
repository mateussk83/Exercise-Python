class Macaco:

    def __init__(self, nome):
        self.__nome = nome
        self.__bucho = []

    def comer(self, comida):
        self.__bucho.append(comida)
    

    def verBucho(self):
        return self.__bucho
    
    def digerir(self):
        self.__bucho = []
    


macaco1 = Macaco("macaquinho come come")
macaco2 = Macaco("macaquinho comido")

Macaco.comer(macaco1,"banana")
print(Macaco.verBucho(macaco1))
Macaco.comer(macaco1,"maça")
print(Macaco.verBucho(macaco1))
Macaco.comer(macaco1,"abacaxi")
print(Macaco.verBucho(macaco1))

Macaco.digerir(macaco1)
print(Macaco.verBucho(macaco1))

Macaco.comer(macaco2,macaco1)
print(Macaco.verBucho(macaco2))
Macaco.comer(macaco2,"coxa")
print(Macaco.verBucho(macaco2))
Macaco.comer(macaco2,"costela")
print(Macaco.verBucho(macaco2))
print(Macaco.verBucho(macaco2))