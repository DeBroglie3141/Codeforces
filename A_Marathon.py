t = int(input())

for _ in range(t):
    truc = list(map(int, input().split()))
    timur = truc[0]
    print(sorted(truc)[::-1].index(timur))