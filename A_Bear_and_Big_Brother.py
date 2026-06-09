L, B = map(int, input().split())
i = 0

while L <= B :
    L *= 3
    B *= 2
    i += 1

print(i)