hora = 1
print("Para Sair do programa basta informar um horario igual a 0!!")

def siglaHora(hora):
    listahora = hora.split(":")
    valor = listahora[0]
    if int(valor) >= 12:
        siglas = "P.M"
    else: 
        siglas = "A.M"
    return(siglas)

def conversaoHora(hora):
    listahora = hora.split(":")
    valor = listahora[0]
    if int(valor) >= 12:
        valor = int(valor) - 12
    listahora[0] = str(valor)
    listahora = ":".join(listahora)
    return(listahora)

while hora != "0":
    hora = input("Informe as horas: ")
    if hora != "0":
        print("Transformação: {1} {0}".format(siglaHora(hora),conversaoHora(hora)))
    else:
        print("Obrigado por usar nosso Programa.")
