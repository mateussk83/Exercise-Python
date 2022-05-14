termo = 0
while(termo <= 0):
    termo = int(input("Informe o fatorial que você quer: "))
    if termo <= 0:
        print("O termo tem que ser positivo!!")
#importante
fatorial = 1
for i in range(termo,0,-1):
    fatorial = fatorial * i

print(fatorial)