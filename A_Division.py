t = int(input())

for _ in range(t):
    rank = int(input())
    if rank <= 1399:
        print("Division 4")
    elif rank <= 1599:
        print("Division 3")
    elif rank <= 1899:
        print("Division 2")
    else:
        print("Division 1")