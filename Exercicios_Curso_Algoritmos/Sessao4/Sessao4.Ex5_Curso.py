"""
Faça um programa que leia um nome de usuário e a senha e não aceita senha igual ao nome de usuário, mostrando 
uma mensagem de erro e voltando a pedir as informações.
"""
nome = input("Informe o seu nome de usuario: ")
senha = input("Informe uma senha: ")

while nome == senha:
    print("Senha igual ao nome!!")
    nome = input("Informe o seu nome de usuario: ")
    senha = input("Informe uma senha ")
