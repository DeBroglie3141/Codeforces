def convertir(nombre_str, base):
    chiffres = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    resultat = 0

    for c in nombre_str:
        resultat = resultat * base + chiffres.index(c.upper())

    return resultat

# Test rapide
print(convertir(input(), int(input())))