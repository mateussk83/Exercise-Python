letra = input("informe a letra: ")

if letra.lower() == "a" or letra.lower() == "e" or letra.lower() == "i" or letra.lower() == "o" or letra.lower() == "u":
    print("A letra {0} é uma vogal!!!".format(letra))
else:
    print("A letra {0} é uma consoante!!!".format(letra))