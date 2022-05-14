lado1 = float(input("Informe o lado A: "))
lado2= float(input("Informe o lado B: "))
lado3 = float(input("Informe o lado C: "))

if lado1 + lado2 < lado3:
    print("Infelizmente essas medidas não são de um triângulo!!")
elif lado1 + lado3 < lado2:
    print("Infelizmente essas medidas não são de um triângulo!!")    
elif lado2 + lado3 < lado1:
    print("Infelizmente essas medidas não são de um triângulo!!")
elif lado2 == lado3 == lado1:
    print("As medidas são de um triângulo Equilátero!!")
elif lado1 == lado2 or lado2 == lado3 or lado1 == lado3:
    print("As medidas são de um trângulo Isósceles!!")
elif lado1 != lado2 != lado3:
    print("As medidas são de um triângulo Escaleno!!")
