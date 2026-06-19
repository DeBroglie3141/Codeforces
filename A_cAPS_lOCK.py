mot = input()

if all(c.isupper() for c in mot[1:]):
    print(mot.swapcase())
else:
    print(mot)