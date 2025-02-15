n = int(input())
for _ in range(n):
    mot = input()
    if len(mot) > 10:
        sortie = mot[0] + str(len(mot)-2) + mot[-1]
        print(sortie)
    else:
        print(mot)