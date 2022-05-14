soma = 0 #Variável criada para armazenar a soma dos valores da lista
mult = 1 #Variável criada para armazenar a multiplicação dos valores
numero=[] #lista vazia 
for i in range(0, 5):
    numero.append(int(input('Informe um numero: ')))
    soma += numero[i]
    mult *= numero[i]

print ('A soma dos numeros digitados é:', soma)
print ('A multiplicação dos numeros digitados é:', mult)
print ('Os números informados foram:', numero)