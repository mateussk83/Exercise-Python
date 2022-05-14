def reverter(numero):
    numero = ''.join(reversed(numero))
    return(numero)
num = int(input("Informe um número: "))
num = str(num)
print(reverter(num))