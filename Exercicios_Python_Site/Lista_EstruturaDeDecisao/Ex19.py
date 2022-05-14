num = int(input("Informe um número menor que 1000: "))

if num < 1000:
    centenas = num / 100
    centenas = int(centenas)
    dezenas = num - (centenas * 100)
    dezenas = dezenas / 10
    dezenas = int(dezenas)
    unidades = num - ((centenas*100) + (dezenas*10))
    if centenas >= 1: 
        print("O numero {0} = {1:.0f} centenas, {2:.0f} dezenas e {3:.0f} unidades".format(num,centenas,dezenas,unidades))
    elif dezenas >= 1:
        print("O numero {0} = {1:.0f} dezenas e {2:.0f} unidades".format(num,dezenas,unidades))
    else:
        print("O numero {0} =  {1:.0f} unidades".format(num,unidades))

