class Funcionario:

    def __init__(self,nome,salario):
        self.__nome = nome
        self.__salario = salario

    def retornarFuncionario(self):
        return "Funcionario\n----------------\nNome: {0}\nSalario: {1:.2f}R$".format(self.__nome,self.__salario)

    def aumentarSalario(self,porcentagem):

        porcentagem = porcentagem / 100
        self.__salario = self.__salario + (self.__salario * porcentagem)


harry = Funcionario("Harry",25000)

harry.aumentarSalario(10)

print(harry.retornarFuncionario())