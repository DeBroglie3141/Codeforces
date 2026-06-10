n = int(input())
count = 1
prev = int(input())

for _ in range(n-1):
    now = int(input())
    if prev != now:
        count += 1
        prev = now
    
print(count)