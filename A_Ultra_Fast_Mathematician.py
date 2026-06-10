a = input()
b = input()

resultat = int(a, 2) ^ int(b, 2)

print(format(resultat, f"0{len(a)}b"))