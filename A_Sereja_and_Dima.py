n = int(input())
cards = list(map(int, input().split()))

sereja, dima = 0, 0

for _ in range(n//2):
    if cards[0] > cards[-1]:
        sereja += cards[0]
        cards.pop(0)
    else:
        sereja += cards[-1]
        cards.pop(-1)
    if cards[0] > cards[-1]:
        dima += cards[0]
        cards.pop(0)
    else:
        dima += cards[-1]
        cards.pop(-1)
if cards:
    if cards[0] > cards[-1]:
        sereja += cards[0]
    else:
        sereja += cards[-1]
print(sereja, dima)