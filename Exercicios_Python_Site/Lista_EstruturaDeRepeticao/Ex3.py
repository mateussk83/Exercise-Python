print("Pré-Requisitos:\nNome: maior que 3 caracteres;\nIdade: entre 0 e 150;\nSalário: maior que zero;\n Sexo: 'f' ou 'm';\nEstado Civil: 's', 'c', 'v', 'd';")
nome = input("Informe o nome: ")
idade = int(input("Informe a idade: "))
salario = float(input("Informe a sálario: "))
sexo = input("Informe o sexo: ")
estado = input("Informe o estado: ")

if len(nome) > 3:
    print("Nome não compriu o Pré-Requisito") 
if idade < 0 and idade > 150:
    print("Idade não compriu o Pré-Requisito")
if salario > 0:
    print("O sálario não compriu o Pré-Requisito")
if sexo.lower() != "m" or sexo.lower() != "f":
    print("O sexo não compriu o Pré-Requisito")
if estado.lower() != "s" or estado.lower() != "c" or estado.lower() != "v" or estado.lower() != "d":
    print("O Estado Civil não compriu o Pré-Requisito")
else:
    print("Os dados são validos!!")