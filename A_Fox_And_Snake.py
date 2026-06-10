n, m = map(int, input().split())

truc = ""
for i in range(n//2):
    truc += "#"*m + "\n"
    if i%2 == 0:
        truc += "."*(m-1) + "#\n"
    else:
        truc += "#" + "."*(m-1) + "\n"

truc += "#"*m

print(truc)