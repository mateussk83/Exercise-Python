num = int(input("Informe um número de 0 a 10 para mostrar a taboada dele: "))
if num > 0 and num < 11:
    for n in range(1, 11):
        resposta = n * num
        print("{0} X {1} = {2}".format(num,n,resposta))
else:
    print("Infelizmente só utilizamos números de 0 a 10")
