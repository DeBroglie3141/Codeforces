a, b = input().lower(), input().lower()

if a == b:
    print(0)
else:
    for i in range(len(a)):
        if a[i] != b[i]:
            if a[i] < b[i]:
                print(-1)
            else:
                print(1)
            break