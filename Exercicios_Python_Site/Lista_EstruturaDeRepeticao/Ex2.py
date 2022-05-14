nome = input("Informe o nome do usuário: ")
senha = input("Informe a senha do usuário: ")

while nome == senha:
    print("Nome igual senha!!")
    nome = input("Informe o nome do usuário: ")
    senha = input("Informe a senha do usuário: ")
print("Nome: {0}".format(nome))
print("Senha: {0}".format(senha))
