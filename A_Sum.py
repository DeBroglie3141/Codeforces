t = int(input())

for _ in range(t):
    truc = sorted(list(map(int, input().split())))
    if truc[2] == truc[1] + truc[0]:
        print("YES")
    else:
        print("NO")
