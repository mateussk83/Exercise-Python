#print ('Informe 10 numeros')
pares = 0
impares = 0
NumPares=[]
NumImpares=[]
for i in range(1, 11): 
    numero = int(input('Informe um numero: '))
    if (numero % 2 == 0):
        pares += 1
        NumPares.append(numero)
    else:
        impares += 1
        NumImpares.append(numero)

print ('Numeros pares:', pares)
print ('Os numeros pares são: ', NumPares)
print ('Numeros impares:', impares)
print('Os numeros impares são:', NumImpares)