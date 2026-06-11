t = int(input())
kliste = [int(input()) for _ in range(t)]
maxk = max(kliste)
nbrs = [1 for _ in range(maxk)]
i, j = 1, 0

while nbrs[-1] == 1:
    if i%3 != 0 and i%10 != 3:
        nbrs[j] = i
        j += 1
    i += 1

for k in kliste:
    print(nbrs[k-1])