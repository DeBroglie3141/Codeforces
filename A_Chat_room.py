s = input()
count = 0
mot = "hellooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo"

for c in s:
    if c == mot[count]:
        count += 1

print("YES" if count >= 5 else "NO")