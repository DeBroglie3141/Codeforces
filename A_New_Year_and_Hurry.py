n, k = map(int, input().split())

free_time = 240 - k
count = 0

while free_time - 5*count*(count + 1)//2 >= 0 and count <= n:
    count += 1

print(count -1)