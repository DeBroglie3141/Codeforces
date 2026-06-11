t = int(input())

for _ in range(t):
    max_blankspace = 0
    n = int(input())
    sequence = list(map(int, input().split()))
    blankspace = 0
    for t in sequence:
        if t == 0:
            blankspace += 1
        elif blankspace:
            max_blankspace = max(max_blankspace, blankspace)
            blankspace = 0
    if blankspace:
        max_blankspace = max(max_blankspace, blankspace)

    print(max_blankspace)