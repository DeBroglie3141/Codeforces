t = int(input())

for _ in range(t):
    a, b, c = map(int, input().split())
    if a == b:
        print(c)
    else:
        print(a if b == c else b)