termo = 0
while (termo <= 0):
    termo = int(input('Voce quer o fatorial de qual termo: '))
    if (termo <= 0):
        print ('O termo deve ser positivo!')

fatorial = 1
for i in range(termo,0,-1):
    fatorial *= i

print (fatorial)





















































