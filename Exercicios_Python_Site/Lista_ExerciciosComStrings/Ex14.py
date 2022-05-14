p = input("Informe a palavra: ")
palavra_leet = ""
palavra = []
cont = 0

palavra = list(p.lower())

for letra in palavra:
    if letra == "a":
        palavra[cont] = "4, /\, @, /-\, ^, ä, ª, aye"
    if letra == "b":
        palavra[cont] = "8, 6, |3, ß, P>, |:"
    if letra == "c":
        palavra[cont] = "[, ¢, <, ("
    if letra == "d":
        palavra[cont] = "|)), o|, [), I>, |>, ?"
    if letra == "e":
        palavra[cont] = "3, &, £, ë, [-, €, ê, |=-"
    if letra == "f":
        palavra[cont] = "|=, ph, |#"
    if letra == "g":
        palavra[cont] = "6, &, (_+, 9, C-, gee (,"
    if letra == "h":
        palavra[cont] = "#, /-/, [-], {=}, <~>, |-|, ]~[, }{, ]-[, ?, 8, }-{"
    if letra == "i":
        palavra[cont] = "1, !, |, &, eye, 3y3, ï, ][, []"
    if letra == "j":
        palavra[cont] = "j, ;, _/, </, (/"
    if letra == "k":
        palavra[cont] = "X, |<, |{, ]{, }<, |("
    if letra == "l":
        palavra[cont] = "1, 1_, |, |_, #, ¬, £"
    if letra == "m":
        palavra[cont] = "//., ^^, |v|, [V], {V}, |\/|, /\/\, (u), []V[], (V), /|\, IVI"
    if letra == "n":
        palavra[cont] = "//, ^/, |\|, /\/, [\], , <\>, {\}, []\[], n, /V, ₪"
    if letra == "o":
        palavra[cont] = "0, (), ?p, , *, ö"
    if letra == "p":
        palavra[cont] = '|^, |*, |o, |^(o), |>, |", 9, []D, |̊, |7'
    if letra == "q":
        palavra[cont] = "q, 9, (_,) o,"
    if letra == "r":
        palavra[cont] = "|2, P\, |?, |^, lz, [z, 12, Я"
    if letra == "s":
        palavra[cont] = "5, $, z, §, ehs"
    if letra == "t":
        palavra[cont] = "7, +, -|-, 1, '][', """
    if letra == "u":
        palavra[cont] = "(_), |_|, v, ü"
    if letra == "v":
        palavra[cont] = "V"
    if letra == "w":
        palavra[cont] = "\/\/, vv, '//, \^/, (n), \V/, \//, \X/, \|/"
    if letra == "x":
        palavra[cont] = ")("
    if letra == "y":
        palavra[cont] = "Y, j, `/, ¥"
    if letra == "z":
        palavra[cont] = "2, z, ~\_, ~/_, %"
    cont = cont + 1
palavra_leet = "".join(palavra)

print("A palavra traduzida para o leet é: {0}".format(palavra_leet))
    