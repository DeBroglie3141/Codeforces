n = int(input())
x, y = list(map(int, input().split())), list(map(int, input().split()))

def truc(x, y, n):
    if x[0] + y[0] < n :
        return "Oh, my keyboard!"
    x.pop(0)
    y.pop(0)
    levels = set(x)
    levels.update(y)
    if len(levels) == n :
        return "I become the guy."
    return "Oh, my keyboard!"
    
print(truc(x,y,n))