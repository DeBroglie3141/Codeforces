k, l, m, n, d = int(input()), int(input()), int(input()), int(input()), int(input())

count = 0

for i in range(d):
    if not ( (i+1)%k and (i+1)%l and (i+1)%m and (i+1)%n):
        count += 1
print(count) 