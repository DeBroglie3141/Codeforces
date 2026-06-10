n = int(input())
events = list(map(int, input().split()))
count = 0
truc = 0

for event in events:
    truc += event
    if truc < 0:
        count += 1
        truc = 0

print(count)