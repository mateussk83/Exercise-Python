turno = input("Informe qual periodo você estuda(M-matutino ou V-Vespertino ou N-Noturno): ")

if turno.lower() == 'm':
    print("Bom Dia!")
elif turno.lower() == 'v':
    print("Boa Tarde!")
elif turno.lower() == 'n':
    print("Boa Noite!")
else:
    print("Valor Inválido!")