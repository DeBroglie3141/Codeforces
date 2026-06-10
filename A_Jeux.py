n = int(input())
couleurs = {}
trucs = []
count = 0

for _ in range(n):
    a, b = map(int, input().split())
    if b in couleurs :
        couleurs[b]+=1
    else:
        couleurs[b]=1
    trucs.append(a)

# print(couleurs)
for couleur in trucs :
    if couleur in couleurs:
        count += couleurs[couleur]

print(count)