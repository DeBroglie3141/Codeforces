t = int(input())
truc = "codeforces"

for _ in range(t):
    a = input()
    count = 0
    for i in range(10):
        if a[i] != truc[i]:
            count += 1

    print(count)