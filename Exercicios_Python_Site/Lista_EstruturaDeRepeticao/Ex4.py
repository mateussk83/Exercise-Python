populacaoA = 80000
populacaoB = 200000
anos = 0
while populacaoA < populacaoB:
    anos = anos + 1
    populacaoA = populacaoA + (populacaoA * 0.03)
    populacaoB = populacaoB + (populacaoB * 0.015)
print("Os anos necessarios para a população A passar a população B é de : {0}".format(anos))
