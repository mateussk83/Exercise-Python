class Tv:

    def __init__(self):
        self.__volume = 100
        self.__canal = 2

    def mudarVolume(self, volume):
        while volume < 0 or volume > 100:
            print("Informe um volume dentro de 0 a 100")
            volume = int(input("Informe o volume novamente: "))
        self.__volume = volume

    def numeroCanal(self, canal):
        while canal < 0:
            print("Informe o numero do canal positivo!!")
            canal = int(input("Informe o canal"))
        self.__canal = canal

    def mostrarTv(self):
        return "Canal: {0}\nVolume {1}\n".format(self.__canal, self.__volume)


tv1 = Tv()
print(Tv.mostrarTv(tv1))
Tv.mudarVolume(tv1,80)
Tv.numeroCanal(tv1,4)

print(Tv.mostrarTv(tv1))