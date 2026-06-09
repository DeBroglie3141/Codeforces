n = input()
count = 0

for chiffre in n:
    if chiffre == "4" or chiffre == "7":
        count += 1

def truc(count):
    for chiffre in str(count):
        if chiffre != "4" and chiffre != "7":
            return "NO"
    return "YES"

print(truc(count))