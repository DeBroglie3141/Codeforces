n, citizens = int(input()), list(map(int, input().split()))

count = 0
truc = max(citizens)

for c in citizens:
    count += truc - c

print(count)