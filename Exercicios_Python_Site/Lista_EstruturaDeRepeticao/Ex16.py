n = 0
ultimo=1
penultimo=1
termo = 0
print("1")
print("1")
numero = 1
while termo < 500:
    termo = ultimo + penultimo
    penultimo = ultimo
    ultimo = termo
    numero = numero +  1
    print(termo)