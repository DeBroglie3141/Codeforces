t = int(input())

for _ in range(t):
    count = 0
    grille = [input() for _ in range(10)]
    for i in range(10):
        for j in range(10):
            if grille[i][j] == "X":
                count += min(i, 9-i, j, 9-j) + 1
    print(count)