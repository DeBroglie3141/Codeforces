t = int(input())

for _ in range(t):
    n, a = int(input()),list(map(int, input().split()))

    if a[0] == a[1]:
        common = a[0]
    else:
        common = a[0] if a[0] == a[2] else a[1]

    for i in range(n):
        if a[i] != common:
            print(i + 1)
            break