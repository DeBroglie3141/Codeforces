n = int(input())
games = input()
truc = 0

for i in range(n):
    if games[i] == "A":
        truc += 1

if truc > n/2 :
    print("Anton")
elif truc < n/2 :
    print("Danik")
else:
    print("Friendship")