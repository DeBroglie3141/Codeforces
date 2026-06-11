import sys

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    s = input().strip()

    l, r = 0, n - 1

    while l < r and s[l] != s[r]:
        l += 1
        r -= 1

    print(max(0, r - l + 1))