t = int(input())

for _ in range(t):
    n = int(input())
    towers = list(map(int, input().split()))

    count = towers[0]
    pre = towers[0]

    for i in range(n-1):
        pre = min(pre, towers[i+1])
        count += pre

    print(count)
