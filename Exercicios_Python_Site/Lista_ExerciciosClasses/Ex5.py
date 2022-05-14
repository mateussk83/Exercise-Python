class ContaCorrente:


    def __init__(self, numeroConta, nome):
        self.__numeroConta = numeroConta
        self.__nome = nome
        self.__saldo = 0

    def alterarNome(self, nome):
        self.__nome = nome
    
    def deposito(self, valor):
        while valor <= 0:
            print("Valor de deposito negativo por favor informe um valor Positivo!!")
            valor = float(input("Informe o valor: "))
        self.__saldo = self.__saldo + valor
        print("Transferencia Realizada com Sucesso")
        return "Saldo atual de {0}R$".format(self.__saldo)
    
    def saque(self, valor):
        while valor <= 0:
            print("Valor de deposito negativo por favor informe um valor Positivo!!")
            valor = float(input("Informe o valor novamente: "))
        while valor > self.__saldo:
            print("Valor informado maior que o saldo de {0}".format(self.__saldo))
            valor = float(input("Informe um valor entre 0 e {0}: ".format(self.__saldo)))
        self.__saldo = self.__saldo - valor
        return "Saldo restante de {0} R$".format(self.__saldo)


conta1 = ContaCorrente(123, "Mateus")

print(ContaCorrente.deposito(conta1, 1000))

print(ContaCorrente.saque(conta1, 0))

         
