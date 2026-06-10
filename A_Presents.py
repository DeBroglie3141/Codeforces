n = int(input())
machins = list(map(int, input().split()))

for i in range(n):
    print(machins.index(i+1)+1, end=" ")