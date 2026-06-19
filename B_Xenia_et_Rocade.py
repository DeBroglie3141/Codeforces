n, m = map(int, input().split())

tasks = list(map(int, input().split()))
count = 0
prec = 1

for t in tasks:
    if t < prec:
        count += n - prec + t
    else:
        count += t - prec
    prec = t

print(count)