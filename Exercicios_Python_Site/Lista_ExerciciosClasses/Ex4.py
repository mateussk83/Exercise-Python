class Pessoa:

    def __init__(self, nome, idade, peso, altura):
        self.__nome = nome
        self.__idade = idade
        self.__peso = peso
        self.__altura = altura

    def envelhecer(self, idade_velho):
        while idade_velho < self.__idade:
            print("{0} já é mais velha do que a idade Inserida então não pode Envelhecer".format(self.__nome))
            idade_velho = int(input("Informe a idade Novamente: "))
        while self.__idade != idade_velho:
            if self.__idade < 21:
                self.__altura = self.__altura + 0.05
            self.__idade = self.__idade + 1
        return "\nNome: {0}\nIdade: {1}\nPeso: {2}\nAltura: {3}".format(self.__nome,self.__idade,self.__peso,self.__altura)
    
    def engordar(self, peso):
        while peso < self.__peso:
            print("{0} já tem um peso maior do que o Inserido então não pode Engordar".format(self.__nome))
            peso = float(input("Informe o peso Novamente: "))
        if peso >= self.__peso:
            self.__peso = peso
        return "\nNome: {0}\nIdade: {1}\nPeso: {2}\nAltura: {3}".format(self.__nome,self.__idade,self.__peso,self.__altura)

    def emagrecer(self, peso):
        while peso > self.__peso:
            print("{0} já tem um peso menor do que o Inserido então não pode Emagrecer".format(self.__nome))
            peso = float(input("Informe o peso Novamente: "))
        if peso <= self.__peso:
            self.__peso = peso
        return "\nNome: {0}\nIdade: {1}\nPeso: {2}\nAltura: {3}".format(self.__nome,self.__idade,self.__peso,self.__altura)
    
    def crescer(self, tamanho):
        while tamanho >= self.__tamanho:
            print("{0} tem um tamanho menor do que o Inserido então não pode Crescer".format(self.__nome))
            tamanho = float(input("Informe o tamanho Novamente: "))
        if tamanho > self.__tamanho:
            self.__tamanho = tamanho
        return "\nNome: {0}\nIdade: {1}\nPeso:{2}\nAltura:{3}".format(self.__nome,self.__idade,self.__peso,self.__altura)
    


pessoa1 = Pessoa("João Pé De Feijão",18,80,1.65)

print(Pessoa.envelhecer(pessoa1, 21))

print(Pessoa.engordar(pessoa1, 60))