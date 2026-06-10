n, t = map(int, input().split())
file = input()

for _ in range(t):
    file = file.replace("BG", "GB")

print(file)