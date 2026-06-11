t = int(input())

for _ in range(t):
    a, b =map(int, input().split())
    count = abs((a // 10) - (b // 10))
    if (a%10 < b%10 and a < b) or (a%10 > b%10 and b < a):
        count += 1
    print(count)