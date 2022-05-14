valor_divida = float(input("Informe o valor da divida: R$"))
print("Quantidade de Parcelas % de Juros sobre o valor inicial da dívida")
print("1    0\n3    10\n6   15\n9   20\n12  15") 
qtd_parcela = int(input("Informe quantas vezes você irá querer passar (maximo 12 vezes): "))

while qtd_parcela > 13:
    print("Infelizmente você informou quantidade de parcelas acima do limite")
    qtd_parcela = int(input("Informe novamente quantas vezes você irá querer passar (maximo 12 vezes): "))

if qtd_parcela > 0 and qtd_parcela < 3:
    juros = 0
elif qtd_parcela >= 3 and qtd_parcela < 6:
    juros = 0.10
elif qtd_parcela >= 6 and qtd_parcela < 9:
    juros = 0.15
elif qtd_parcela >= 9 and qtd_parcela < 12:
    juros = 0.20
elif qtd_parcela == 12:
    juros = 0.25

for n in range(1,13):
    if qtd_parcela == n:
        juros_total = valor_divida * juros
        valor_parcela = (valor_divida / qtd_parcela) + (juros_total / qtd_parcela)

print("Valor da Divida Valor dos Juros Quantidade de Parcelas Valor da Parcela")
print("R${0}           R${1}           {2}                    R${3:.2f}".format(valor_divida, juros_total, qtd_parcela,valor_parcela))