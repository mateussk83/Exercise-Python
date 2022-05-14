print("Especificação   Código  Preço \nCachorro Quente 100     R$ 1,20 \nBauru Simples   101     R$ 1,30 \nBauru com ovo   102     R$ 1,50 \nHambúrguer      103     R$ 1,20 \nCheeseburguer   104     R$ 1,30 \nRefrigerante    105     R$ 1,00")

produtos = []
valor = []

operacao = "s"

while operacao.lower() == "s":
    codigo = int(input("Informe o código do produto: "))
    if codigo == 100:
        produto = "Cachorro quente"
        produtos.append(produto)
        preco = 1.20
    elif codigo == 101:
        produto = "Bauru Simples"
        produtos.append(produto)
        preco = 1.30
    elif codigo == 102:
        produto = "Bauru com ovo"
        produtos.append(produto)
        preco = 1.50
    elif codigo == 103:
        produto = "Hambúrguer"
        produtos.append(produto)
        preco = 1.20
    elif codigo == 104:
        produto = "Cheeseburguer"
        produtos.append(produto)
        preco = 1.30
    elif codigo == 105:
        produto = "Refrigerante"
        produtos.append(produto)
        preco = 1.00
    else:   
        print("Informe um produto valido")
    if codigo > 99 and codigo < 106:
        qtd = int(input("Informe a quantidade de {0}: ".format(produto)))
        valor_produto = qtd * preco
        valor.append(valor_produto)
    print("Informe com S - SIM ou N - NAO")
    operacao = input("Deseja continuar o pedido: ")
cont = 0
for produto in produtos:
    print("Produto                - {0}".format(produtos[cont]))
    print("Valor Total do Produto - R${0}\n".format(valor[cont]))
    cont = cont + 1
print("\nmValor Total da compra  - R${0}".format(sum(valor)))