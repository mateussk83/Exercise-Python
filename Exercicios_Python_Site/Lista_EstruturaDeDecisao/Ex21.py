quantia = float(input("Informe a quantia: "))

if quantia >= 10 and quantia <= 600:
    nota100 = quantia / 100
    nota100 = int(nota100)
    nota50 = quantia - (nota100 * 100)
    nota50 = nota50 / 50 
    nota50 = int(nota50)
    nota10 = quantia - ((nota100 * 100) + (nota50 * 50))
    nota10 = nota10 / 10
    nota10 = int(nota10)
    nota5 = quantia - ((nota100 * 100) + (nota50 * 50) + (nota10 * 10)) 
    nota5 = nota5 / 5
    nota5 = int(nota5)
    nota1 = quantia - ((nota100 * 100) + (nota50 * 50) + (nota10 * 10) + (nota5 * 5)) 
    nota1 = int(nota1)
    if nota100 == 0:
         print("O valor de R${0:.2f}: será dividido em  {1} notas de 50, {2} notas de 10, {3} notas de 5 e {4} notas de 1 ".format(quantia, nota50, nota10, nota5, nota1))
    elif nota50 == 0:
        print("O valor de R${0:.2f}: será dividido em {1} notas de 100, {2} notas de 10, {3} notas de 5 e {4} notas de 1 ".format(quantia, nota100, nota50, nota10, nota5, nota1))
    elif nota10 == 0:
         print("O valor de R${0:.2f}: será dividido em {1} notas de 100, {2} notas de 50, {3} notas de 5 e {4} notas de 1 ".format(quantia, nota100, nota50, nota5, nota1))
    elif nota5 == 0:
         print("O valor de R${0:.2f}: será dividido em {1} notas de 100, {2} notas de 50, {3} notas de 10, {4} notas de 1 ".format(quantia, nota100, nota50, nota10, nota1))
    elif nota1 == 0:
         print("O valor de R${0:.2f}: será dividido em {1} notas de 100, {2} notas de 50, {3} notas de 10, {4} notas de 5".format(quantia, nota100, nota50, nota10, nota5))


else:
    print("Valor invalido!!")

