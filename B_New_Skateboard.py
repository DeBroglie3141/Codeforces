nombre = input()
n = 0

for i in range(len(nombre)-1):
    if int((nombre[i:i+2]))%4 == 0:
        n += i + 1

for chiffre in nombre:
    if int(chiffre)%4 == 0:
        n +=1
        
print(n)