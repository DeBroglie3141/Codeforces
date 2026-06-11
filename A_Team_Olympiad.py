n = int(input())
childrens = list(map(int, input().split()))
a, b, d = [], [], []

for i in range(n):
    c = childrens[i]
    if c == 1:
        a.append(i+1)
    elif c== 2:
        b.append(i+1)
    else:
        d.append(i+1)
truc = min(len(a), len(b), len(d))
print(truc)
for j in range(truc):
    print(a[j], b[j], d[j])
