n = int(input("Que termo deseja encontrar: "))
ultimo=1
penultimo=1

print("1")
print("1")
numero = 1
while numero <= n:
    termo = ultimo + penultimo
    penultimo = ultimo
    ultimo = termo
    numero = numero +  1
    print(termo)