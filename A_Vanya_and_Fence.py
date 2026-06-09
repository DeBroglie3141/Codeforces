n, h = map(int, input().split())
persons = list(map(int, input().split()))
count = n

for i in range(n):
    if persons[i] > h:
        count += 1

print(count)