t = int(input())

for _ in range(t):
    n, x = map(int, input().split())
    stations = list(map(int, input().split()))
    min_volume = 1
    for i in range(n-1):
        min_volume = max(min_volume, stations[i+1] - stations[i])
    min_volume = max(min_volume, stations[0], 2*(x - stations[-1]))
    print(min_volume)