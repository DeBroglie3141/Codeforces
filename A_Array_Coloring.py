t = int(input())

for _ in range(t):
    n, nbrs = int(input()), sum(map(int, input().split()))
    if n >= 2 and nbrs%2 == 0:
        print("YES")
    else:
        print("NO")