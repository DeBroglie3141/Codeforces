n = int(input())
capacity = 0
nb_passengers = 0

for _ in range(n):
    a, b = map(int, input().split())
    nb_passengers += b - a
    capacity = max(capacity, nb_passengers)

print(capacity)