"""
Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer numero inteiro entre 1 e 10.
O usuario deve informar de qual numero ele deseja ver a tabuada. A saida deve ser conforme o Exemplo abaixo:
 Tabuada do 5:
 5 x 1 = 5
 5 x 2 = 10 
 ...
 5 x 10 = 50
"""
num = int(input("Informe um numero"))

if num > 10:
    print("o numero tem q ser menor que 10")
    num = int(input("Informe um numero"))
print("A tabela do {0} é".format(num))
if num < 10:
    for n in range(1, 11):
        multiplicacao = n * num
        print("{0} x {1} = {2}".format(n, num, multiplicacao))

          
