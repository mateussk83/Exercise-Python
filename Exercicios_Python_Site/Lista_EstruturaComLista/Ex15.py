lados = []

for n in range(1,3):
    lado = float(input("Informe o {0} lado: ".format(n)))
    lados.append(lado)

if lado[0] + lado[1] < lado[2]:
    print("Infelizmente essas medidas não são de um triângulo!!")
elif lado[0] + lado[2] < lado[1]:
    print("Infelizmente essas medidas não são de um triângulo!!")    
elif lado[1] + lado[2] < lado[0]:
    print("Infelizmente essas medidas não são de um triângulo!!")
elif lado[1] == lado[2] == lado[0]:
    print("As medidas são de um triângulo Equilátero!!")
elif lado[0] == lado[1] or lado[1] == lado[2] or lado[0] == lado[2]:
    print("As medidas são de um trângulo Isósceles!!")
elif lado[0] != lado[1] != lado[2]:
    print("As medidas são de um triângulo Escaleno!!")
