t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    truc = list(map(int, input().split()))
    if k == 1 and truc != sorted(truc):
        print("NO")
    else:
        print("YES")