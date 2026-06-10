t = int(input())

for _ in range(t):
    n = int(input())
    s = input()
    if n%2 == 1:
        print("NO")
    else:
        a = 0
        for char in s:
            if char == "(":
                a += 1
        if n//2 == a:
            print("YES")
        else:
            print("NO")