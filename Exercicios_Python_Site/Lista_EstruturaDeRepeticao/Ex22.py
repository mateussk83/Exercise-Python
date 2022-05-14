num = int(input("Informe um número: "))
multiplos = []
multiplo = 0

for n in range(2,num):
    if num % n == 0:
        multiplo = multiplo + 1
        multiplos.append(n)
if multiplo == 0: 
    print("O número {0} é primo!!!".format(num))
else:
    print("O número {0} não é primo!!!\n Ele é Divisivel por {1}".format(num, multiplos))