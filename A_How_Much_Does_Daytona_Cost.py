t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    nbrs = list(map(int, input().split()))
    if k in nbrs:
        print("YES")
    else:
        print("NO")