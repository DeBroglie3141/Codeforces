t = int(input())

for _ in range(t):
    n = int(input())
    nbrs = set(map(int, input().split()))
    if n == 1 or len(nbrs) == (max(nbrs)-min(nbrs)+1):
        print("YES")
    else:
        print("NO")
