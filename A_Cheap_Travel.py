n, m, a, b = map(int, input().split())

if b < m*a :
    truc, reste = (n // m) * b, n%m
    if reste*a < b:
        truc += reste*a
    else:
        truc += b
    print(truc)
else:
    print(n*a)