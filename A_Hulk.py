n = int(input())
msg = "I hate "

for i in range(n-1):
    if i%2 == 0:
        msg += "that I love "
    else:
        msg += "that I hate "
msg += "it"

print(msg)