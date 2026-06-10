t = int(input())

for _ in range(t):
    loc = list(map(int, input().split()))
    if loc[0]%2 == loc[1]%2 == 1:
        print("NO")
    else:
        print("YES")