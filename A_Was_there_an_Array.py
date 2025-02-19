N = int(input())

for _ in range(N):
    n, array = int(input()), list(map(int, input().split()))
    if all(array[i:i+3] != [1, 0, 1] for i in range(n)):
        print('YES')
    else:
        print('NO')