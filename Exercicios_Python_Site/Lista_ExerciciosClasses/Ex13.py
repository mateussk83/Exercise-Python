class Funcionario:

    def __init__(self,nome,salario):
        self.__nome = nome
        self.__salario = salario

    def retornarFuncionario(self):
        return "Funcionario\n----------------\nNome: {0}\nSalario: {1:.2f}R$".format(self.__nome,self.__salario)



funcionario1 = Funcionario("mateus",1500)

print(funcionario1.retornarFuncionario())