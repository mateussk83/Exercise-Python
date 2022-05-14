import turtle 
from turtle import * 
pen = turtle.Pen()
class Bola:
    pen = pen
    raio = 0

    def __init__(self,cor, circuferencia, material):
        self.__cor = cor 
        self.__circuferencia = circuferencia
        self.__material = material
        Bola.raio = self.__circuferencia

    def troca_cor(self,cor):
        self.__cor = cor
    
    def mostra_cor(self):
        self.__bola = Bola.pen.dot(Bola.raio,self.__cor)
        return self.__bola


bola = Bola("blue",300,"madeira")



print(Bola.troca_cor(bola,"yellow"))

print(Bola.mostra_cor(bola))



        
