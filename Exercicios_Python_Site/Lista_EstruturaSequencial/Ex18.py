"""
Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps),
calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).
"""
MB = float(input("Informe a quantidade de MB em seu arquivo: "))
Velocidade = float(input("Informe a velocidade da rede em Mbps: "))

VelocidadeSegundo = MB / Velocidade
VelocidadeMinuto = VelocidadeSegundo / 60
RESTO = VelocidadeSegundo % 60 
if VelocidadeMinuto < 1:
    VelocidadeMinuto = 0
print("O tempo restante para concluir seu download é: {0} minutos e {1} segundos".format(int(VelocidadeMinuto),int(VelocidadeSegundo)))