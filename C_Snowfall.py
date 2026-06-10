t = int(input())

for _ in range(t):
    n = int(input())
    elems = list(map(int, input().split()))
    a, b, c, d = [], [], [], []
    for elem in elems:
        if elem%6 == 0:
            a.append(elem)
        elif elem%3 == 0:
            b.append(elem)
        elif elem%2 == 0:
            c.append(elem)
        else:
            d.append(elem)
    print(*a, *c, *d, *b)